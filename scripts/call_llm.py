import json, os, openai

openai.api_key = os.environ["LLM_API_KEY"]

prompt = open("compiled_prompt.txt").read()

response = openai.ChatCompletion.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.2
)

print(response.choices[0].message["content"])
