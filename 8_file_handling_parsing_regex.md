Perfect. Let's move to **Step 8: File Handling, Parsing, and Regex**—crucial for a Test Engineer, especially when dealing with logs, configs, test data, and automation.

---

## **Step 8: File Handling, Parsing & Regex in Python**

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

### 🔹 Real-World Example: Log Parser

```python
def extract_errors(filename):
    with open(filename) as f:
        for line in f:
            if re.search(r"ERROR", line):
                print(line.strip())
```

---

**Mini Challenge:**  
Write a script that reads a `.txt` file and extracts all dates in the format `YYYY-MM-DD`.

---

Ready for **Step 9: Unit Testing & Pytest** next? That’s directly tied to your role as a test engineer.