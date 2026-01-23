import subprocess, json, pathlib

pathlib.Path("artifacts").mkdir(exist_ok=True)

def run(cmd):
    return subprocess.check_output(cmd, shell=True).decode()

context = {
    "diff": run("git diff origin/main...HEAD"),
}

with open("artifacts/context.json", "w") as f:
    json.dump(context, f)
