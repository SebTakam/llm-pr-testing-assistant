import sys, os
from openai import OpenAI

mode = sys.argv[1]
client = OpenAI(api_key=os.environ["LLM_API_KEY"])

prompt = open(f"compiled_{mode}_prompt.txt").read()

resp = client.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.2
)

with open(f"artifacts/test_{mode}.json", "w") as f:
    f.write(resp.choices[0].message.content)

