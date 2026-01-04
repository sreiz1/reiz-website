# app.py - main flask app
# to run: python app.py
# or: gunicorn app:app --workers=4

import os
import subprocess
import time

import flask
import flask_caching
import flask_mail
import whitenoise

MAX_REQ_PER_HOUR=25
CACHE_DIR='/tmp/cache1'
MAIL_EMAIL='info@reiz.nl'

hostname = subprocess.run(["hostname"], capture_output=True).stdout
if isinstance(hostname, bytes):
    hostname = hostname.decode('utf-8')
hostname = hostname.strip().lower()
do_debug = (hostname in {'cooldesk', 'npm1-ubuntu2404'})

root_dir = 'dist/' if do_debug else '.'
app = flask.Flask(__name__)
app.config.from_mapping({
    'MAIL_SERVER': '172.17.0.1', # docker container host IP
    'MAIL_PORT': 25,
    'MAIL_USE_TLS': False,
    'MAIL_DEFAULT_SENDER': MAIL_EMAIL,
})
# we maintain a global cache for DDOS protection:
# - a counter that is initially set to MAX_REQ_PER_HOUR and decremented for each request
# - if the counter is <=0, we reject requests with a 429 Too Many Requests
# - a next_reset timestamp to allow resetting the counter at most once per hour
os.makedirs(CACHE_DIR, exist_ok=True)
cache = flask_caching.Cache(config={'CACHE_TYPE': 'FileSystemCache',
                                    'CACHE_DEFAULT_TIMEOUT': 2147483647,
                                    'CACHE_DIR': CACHE_DIR})
cache.init_app(app)
cache.set('counter', MAX_REQ_PER_HOUR)
cache.set('next_reset', time.time()+3600)
mail = flask_mail.Mail(app)
app.wsgi_app = whitenoise.WhiteNoise(app.wsgi_app, root=root_dir,
                                     index_file=True, autorefresh=do_debug)



@app.post('/action/submit')
def action_submit():
    if cache.get('counter') <= 0:
        if time.time() >= cache.get('next_reset'):
            cache.set('counter', MAX_REQ_PER_HOUR)
            cache.set('next_reset', time.time()+3600)
        else:
            return 'Too Many Requests', 429
    cache.set('counter', cache.get('counter') - 1)
    counter = cache.get('counter')
    referrer = flask.request.referrer
    form_data = flask.request.form
    mail_error = None
    try:
        msg = flask_mail.Message(subject='REIZ.NL New contact form submission',
                                 recipients=[MAIL_EMAIL],
                                 body=f'New contact form submission:\n\n{form_data}\n\n{counter=}\n')
        mail.send(msg)
    except Exception as e:
        mail_error = e
    print(f'DEBUG {form_data=}, {counter=}, {referrer=}, {mail_error=}')
    lang = form_data.get('lang', 'en')
    next_page = f'/{lang}/contact-sent' if mail_error is None else f'/{lang}/contact-not-sent'
    return flask.redirect(next_page)


def app_main():
    '''main entry point, start flask'''
    port = int(os.environ.get('PORT', 5000))
    print(f'starting main flask app on {hostname}, {port=}, {do_debug=}, {root_dir=}')
    app.run(debug=do_debug, host='127.0.0.1', port=port)


if __name__ == "__main__":
    app_main()
