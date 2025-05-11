# generate an image for a prompt
# this version uses smolagents, an openai (gemini) model and a hf text to image tool

import sys
import json
import os
#from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel
from smolagents import CodeAgent, OpenAIServerModel, load_tool, AgentImage

# Load API keys from secret-keys.json
secrets_path = os.path.join(os.path.dirname(__file__), 'secret-keys.json')
with open(secrets_path, 'r') as f:
    secrets = json.load(f)
GEMINI_API_KEY = secrets.get('GEMINI_API_KEY')
if not GEMINI_API_KEY:
    raise Exception("Missing GEMINI_API_KEY in secret-keys.json.")

model = OpenAIServerModel(
    model_id="gemini-2.0-flash",
    api_key=GEMINI_API_KEY,
    api_base="https://generativelanguage.googleapis.com/v1beta/openai/",
    temperature=0.7
)
image_generation_tool = load_tool("m-ric/text-to-image", trust_remote_code=True)

len(sys.argv) >= 3 or sys.exit("Usage: python generate-image-for-prompt.py <prompt-file> <output_file>")
prompt_file = sys.argv[1]
with open(prompt_file, 'r') as f:
    prompt = f.read().strip()
output_file = sys.argv[2]

agent = CodeAgent(tools=[image_generation_tool], model=model)
#GradioUI(agent).launch() # works but have to specify the prompt in the UI and save the image manually

result=agent.run("Generate an image that looks as follows: " + prompt)
assert isinstance(result, AgentImage), "Expected result to be an AgentImage, got: " + str(result)
tmp_path=result.to_string()
file_extension = tmp_path.split('.')[-1]
assert '.' not in output_file, "Output file name should not contain a dot (.)"
output_file += '.' + file_extension
os.rename(tmp_path, output_file)
print(f"Image saved to {output_file}")
