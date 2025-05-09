# use smolagents to generate an image for a prompt
# includes (disbaled) telemetry code to allow inspecting the steps

# in a separate terminal, run the following command to start the telemetry server
# python -m phoenix.server.main serve
# then after running can inspect at http://localhost:6006/projects/

import sys
import json
import os
#from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel
from smolagents import CodeAgent, DuckDuckGoSearchTool, OpenAIServerModel
# from opentelemetry import trace
# from opentelemetry.sdk.trace import TracerProvider
# from opentelemetry.sdk.trace.export import BatchSpanProcessor
# from openinference.instrumentation.smolagents import SmolagentsInstrumentor
# from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
# from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

# endpoint = "http://localhost:6006/v1/traces"
# trace_provider = TracerProvider()
# trace_provider.add_span_processor(SimpleSpanProcessor(OTLPSpanExporter(endpoint)))
# SmolagentsInstrumentor().instrument(tracer_provider=trace_provider)

# Load API keys from secret-keys.json
secrets_path = os.path.join(os.path.dirname(__file__), 'secret-keys.json')
with open(secrets_path, 'r') as f:
    secrets = json.load(f)

HF_API_KEY = secrets.get('HF_API_KEY')
GEMINI_API_KEY = secrets.get('GEMINI_API_KEY')

if not HF_API_KEY or not GEMINI_API_KEY:
    raise Exception("Missing HF_API_KEY or GEMINI_API_KEY in secret-keys.json. Example structure:\n{\n  \"HF_API_KEY\": \"your-hf-key\",\n  \"GEMINI_API_KEY\": \"your-gemini-key\"\n}")

# model=HfApiModel(token=HF_API_KEY)

model = OpenAIServerModel(
    model_id="gemini-2.0-flash",
    api_key=GEMINI_API_KEY,
    # Google Gemini OpenAI-compatible API base URL
    api_base="https://generativelanguage.googleapis.com/v1beta/openai/",
)
agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)

# agent.run("How many seconds would it take for a leopard at full speed to run through Pont des Arts?")
# agent.run("How many Rs are there in 'carry strawberries in the rain'?")
len(sys.argv) >= 3 or sys.exit("Usage: python generate-image-for-prompt.py <prompt-file> <output_file>")
prompt_file = sys.argv[1]
output_file = sys.argv[2]
agent.run("Generate an image for the prompt in " + prompt_file + " and save it to " + output_file)
