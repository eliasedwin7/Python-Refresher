# **Python README guide** that shows you how to read data from **JSON, YAML, Excel, and CSV** files 

all in one place. Great for quick reference in data-driven testing or scripting.

---

# 📘 Python File Reading Cheatsheet

A handy guide for reading data from common file types: **JSON, YAML, Excel, and CSV**.

---

## 📂 1. Reading JSON Files

### 🔧 File: `data.json`

```json
[
    {"name": "Edwin", "age": 30},
    {"name": "Ali", "age": 28}
]
```

### 🧪 Code:

```python
import json

with open('data.json') as f:
    data = json.load(f)

print(data)  # List of dicts
```

---

## 🟨 2. Reading YAML Files

### 🔧 File: `data.yaml`

```yaml
- name: Edwin
  age: 30
- name: Ali
  age: 28
```

### 🧪 Code:

```python
import yaml

with open('data.yaml') as f:
    data = yaml.safe_load(f)

print(data)  # List of dicts
```

📦 **Install PyYAML** if needed:

```bash
pip install pyyaml
```

---

## 📊 3. Reading Excel Files

### 🔧 File: `data.xlsx`

| Name  | Age |
| ----- | --- |
| Edwin | 30  |
| Ali   | 28  |

### 🧪 Code:

```python
import pandas as pd

df = pd.read_excel('data.xlsx')
print(df)
```

📦 **Install Excel support**:

```bash
pip install pandas openpyxl
```

---

## 📋 4. Reading CSV Files

### 🔧 File: `data.csv`

```
name,age
Edwin,30
Ali,28
```

### 🧪 Code:

```python
import csv

with open('data.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
```

Or use pandas:

```python
import pandas as pd

df = pd.read_csv('data.csv')
print(df)
```

---

## ✅ Summary Table

| File Type | Library               | Function                             |
| --------- | --------------------- | ------------------------------------ |
| JSON      | `json`                | `json.load()`                        |
| YAML      | `pyyaml`              | `yaml.safe_load()`                   |
| Excel     | `pandas` + `openpyxl` | `pd.read_excel()`                    |
| CSV       | `csv` / `pandas`      | `csv.DictReader()` / `pd.read_csv()` |

---
