# app.py - main flask app
# to run: python app.py


import os
import json
import subprocess
import datetime

import flask


app = flask.Flask(__name__)


@app.post('/action/create')
def action_create_update():
    name = flask.session.get('user')
    dd_hh_mm = (flask.request.form['exp_days'], flask.request.form['exp_hours'], flask.request.form['exp_minutes'],)
    return flask.redirect('/file/'+flask.request.form['new_name'])


def app_main():
    '''main entry point, start flask'''
    hostname = subprocess.run(["hostname"], capture_output=True).stdout
    if isinstance(hostname, bytes):
        hostname = hostname.decode('utf-8')
    hostname = hostname.strip().lower()
    do_debug = (hostname in {'cooldesk'})
    port = 5000
    print(f'starting main flask app on {hostname}, {port=}, debug={do_debug}')
    app.run(debug=do_debug, host="0.0.0.0", port=port)


if __name__ == "__main__":
    app_main()
