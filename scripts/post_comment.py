import sys, subprocess, os

mode = sys.argv[1]
body = open(f"artifacts/test_{mode}.json").read()

subprocess.run([
  "gh", "pr", "comment", os.environ["PR_NUMBER"],
  "--body", f"### 🤖 AI {mode.replace('_',' ').title()}\n```json\n{body}\n```"
])
