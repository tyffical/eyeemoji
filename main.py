import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = os.environ['OPENAI_API_KEY']

print("Type whatever you want, then press Enter! :)")
prompt = input()

test_prompt = "This is a test"

response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=5, echo=True)

print(response["choices"][0]["text"])