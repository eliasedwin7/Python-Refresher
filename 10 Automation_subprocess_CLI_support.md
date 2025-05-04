# **Step 10: Automation, Subprocess & CLI in Python**

---

### 🔹 **1. Why Automation?**

As a Test Engineer, you often:
- Run tests from CLI
- Execute batch jobs/scripts
- Collect logs or reports
- Control tools (test benches, firmware, pipelines)

Python makes this smooth with `subprocess`, `os`, and `argparse`.

---

### 🔹 **2. `subprocess`: Running Terminal Commands**

#### ✅ Basic Shell Command
```python
import subprocess

subprocess.run(["ls", "-l"])
```

#### ✅ Capturing Output
```python
result = subprocess.run(["echo", "Hello"], capture_output=True, text=True)
print(result.stdout.strip())  # Hello
```

#### ✅ Error Handling
```python
try:
    subprocess.run(["cat", "nofile.txt"], check=True)
except subprocess.CalledProcessError as e:
    print("Command failed:", e)
```

---

### 🔹 **3. `os` Module: File System Automation**

```python
import os

os.mkdir("reports")                   # Create folder
print(os.getcwd())                   # Get current directory
os.listdir(".")                      # List files
os.rename("old.txt", "new.txt")      # Rename files
```

---

### 🔹 **4. `argparse`: Command-Line Interfaces**

Used to make your script behave like a tool with flags and inputs.

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", help="Your name")
args = parser.parse_args()

print(f"Hello, {args.name}")
```

Run with:
```bash
python script.py --name Edwin
```

---

### 🔹 **5. Automate a Simple Test Case**

```python
import subprocess

def run_pytest():
    result = subprocess.run(["pytest", "--maxfail=1", "--disable-warnings"], capture_output=True, text=True)
    print(result.stdout)

run_pytest()
```

This can be run on CI or part of a larger test automation pipeline.

---

### ✅ Summary

| Tool        | Use Case                                 |
|-------------|-------------------------------------------|
| `subprocess`| Run shell commands, control processes     |
| `os`        | Navigate filesystem, manage paths         |
| `argparse`  | Create command-line tools with options    |
