# use smolagents to generate an image for a prompt

import sys
import json
import os
#from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel
from smolagents import CodeAgent, OpenAIServerModel, Tool

# Load API keys from secret-keys.json
secrets_path = os.path.join(os.path.dirname(__file__), 'secret-keys.json')
with open(secrets_path, 'r') as f:
    secrets = json.load(f)
HF_API_KEY = secrets.get('HF_API_KEY')
GEMINI_API_KEY = secrets.get('GEMINI_API_KEY')
if not HF_API_KEY or not GEMINI_API_KEY:
    raise Exception("Missing HF_API_KEY or GEMINI_API_KEY in secret-keys.json.")

# model=HfApiModel(token=HF_API_KEY)

model = OpenAIServerModel(
    model_id="gemini-2.0-flash",
    api_key=GEMINI_API_KEY,
    api_base="https://generativelanguage.googleapis.com/v1beta/openai/",
    temperature=0.7
)
image_generation_tool = Tool.from_space(
    "black-forest-labs/FLUX.1-schnell",
    name="image_generator",
    description="Generate an image from a prompt",
    token=HF_API_KEY
)

# agent.run("How many seconds would it take for a leopard at full speed to run through Pont des Arts?")
# agent.run("How many Rs are there in 'carry strawberries in the rain'?")
len(sys.argv) >= 3 or sys.exit("Usage: python generate-image-for-prompt.py <prompt-file> <output_file>")
prompt_file = sys.argv[1]
with open(prompt_file, 'r') as f:
    prompt = f.read().strip()
output_file = sys.argv[2]

image_generation_tool(prompt)
agent = CodeAgent(tools=[image_generation_tool], model=model)
agent.run("Generate an image and save it to " + output_file)
