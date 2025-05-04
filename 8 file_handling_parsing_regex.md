
# **Step 8: File Handling, Parsing & Regex in Python**

---

### 🔹 **1. File Handling**

#### ✅ Reading a File
```python
with open("log.txt", "r") as f:
    content = f.read()
```

#### ✅ Reading Line-by-Line
```python
with open("log.txt", "r") as f:
    for line in f:
        print(line.strip())
```

> `with` ensures the file is automatically closed.  
> Use `.strip()` to remove `\n`.

#### ✅ Writing to a File
```python
with open("output.txt", "w") as f:
    f.write("Hello, world!")
```

- `"w"` – overwrite
- `"a"` – append
- `"r"` – read

---

### 🔹 **2. Parsing CSV, JSON**

#### ✅ CSV File
```python
import csv

with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])
```

#### ✅ JSON File
```python
import json

with open("data.json", "r") as f:
    data = json.load(f)
    print(data["name"])
```

---

### 🔹 **3. Regular Expressions (Regex)**

**Why?**  
- Powerful tool for text searching, pattern matching, and log parsing.

```python
import re
```

---

#### ✅ Basic Pattern Matching
```python
text = "User: edwin123, Email: edwin@test.com"
match = re.search(r"edwin\d+", text)
print(match.group())  # edwin123
```

#### ✅ Extract Email
```python
emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
```

#### ✅ Replace Values
```python
replaced = re.sub(r"\d+", "***", "Phone: 1234567890")  # Phone: ***
```

---

### 🔹 Common Regex Patterns

| Pattern     | Meaning                       |
|-------------|-------------------------------|
| `\d`        | Digit                         |
| `\w`        | Word character (a-z, A-Z, 0-9, _) |
| `.`         | Any character                 |
| `+`         | One or more                   |
| `*`         | Zero or more                  |
| `^text`     | Starts with "text"            |
| `text$`     | Ends with "text"              |
| `[a-z]`     | Any lowercase letter          |
| `()`        | Grouping                      |

---
#### Regex Pattern for Gmail Validation
```python
import re

pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'

email = "edwin.alias@gmail.com"

if re.match(pattern, email):
    print("Valid Gmail address ✅")
else:
    print("Invalid Gmail address ❌")
```

### 🔹 Real-World Example: Log Parser

```python
def extract_errors(filename):
    with open(filename) as f:
        for line in f:
            if re.search(r"ERROR", line):
                print(line.strip())
```

---

# 🎛️ Section: Argument Parsing in Python

---

## 🔹 What Is Argument Parsing?

**Argument parsing** allows your Python script to accept input values from the **command line**, making it configurable and reusable without changing the code.

You use the **`argparse` module** to handle this cleanly and professionally.

---

## 🔸 Why Use `argparse`?

* Makes your script flexible
* Avoids hardcoding values
* Adds built-in help (`--help`)
* Great for automation, test tools, CLI apps

---

## 🔸 Basic Example

```python
import argparse

parser = argparse.ArgumentParser(description="Add two numbers")
parser.add_argument("a", type=int, help="First number")
parser.add_argument("b", type=int, help="Second number")

args = parser.parse_args()
print("Sum:", args.a + args.b)
```

### ✅ Usage:

```bash
python add.py 5 3
# Output: Sum: 8
```

---

## 🔸 Common Argument Types

| Flag Type        | Syntax Example                    | Description                          |
| ---------------- | --------------------------------- | ------------------------------------ |
| Positional       | `parser.add_argument("filename")` | Required argument                    |
| Optional (flag)  | `--verbose`                       | Boolean flag (`True` if present)     |
| Optional (value) | `--mode test`                     | Key-value pair                       |
| Type conversion  | `type=int`                        | Auto-convert to `int`, `float`, etc. |
| Default value    | `default=10`                      | If not passed, fallback value        |

---

## 🔸 Example with Flags and Defaults

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", default="Guest", help="Your name")
parser.add_argument("--verbose", action="store_true", help="Enable debug mode")

args = parser.parse_args()

if args.verbose:
    print("Verbose mode is on.")
print(f"Hello, {args.name}!")
```

### ✅ Usage:

```bash
python greet.py --name Edwin --verbose
# Verbose mode is on.
# Hello, Edwin!
```

---

## 🔸 Helpful Features

* `parser.add_argument('--count', type=int, choices=[1, 2, 3])`
* `parser.add_argument('--list', nargs='+')` → accepts multiple values
* `parser.add_argument('--version', action='version', version='1.0')`

---

## 📌 Interview Tips

| Question                             | Suggested Answer                                                  |
| ------------------------------------ | ----------------------------------------------------------------- |
| Why use `argparse`?                  | To make CLI scripts configurable and user-friendly                |
| How is it different from `sys.argv`? | `argparse` is structured, provides help, validation, and defaults |
| What does `action="store_true"` do?  | Sets the value to `True` if the flag is present in the command    |

---

