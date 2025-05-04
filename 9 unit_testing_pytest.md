# **Step 9: Unit Testing & Pytest**

### 🔹 **1. What is Unit Testing?**

It’s testing **individual pieces of your code** (like functions or classes) in isolation.

> You check: "Does this part behave as expected?"

---

### 🔹 **2. The `unittest` Module (built-in)**

```python
import unittest

def add(a, b):
    return a + b

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertNotEqual(add(1, 1), 3)

if __name__ == '__main__':
    unittest.main()
```

✅ You get:
- `assertEqual`, `assertTrue`, `assertIn`, `assertRaises`, etc.

---

### 🔹 **3. Pytest (the go-to tool)**

Much simpler, more powerful.

#### ✅ Installation
```bash
pip install pytest
pytest --help #for all the commands
```

#### ✅ Example
```python
# test_math.py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```

Then run:
```bash
pytest test_math.py
```

---

### 🔹 **4. Pytest Fixtures**

Used to set up pre-conditions or shared test data.
Inroder to access the *teardown* you can use the `yeild` keyword in the *fixture*.
`request` fixture help in providing information of the requesting test function

```python
import pytest

@pytest.fixture
def sample_data():
    print('Started setup')
    yeild
    print('End of test')
    return [1, 2, 3]

def test_sum(sample_data):
    assert sum(sample_data) == 6
```
### 🔹 **5. Conftest.py**
If you want to share the the common modules,fixtures for all the test in a folder put that in `conftest.py`.
If you don't want to provide setup_test as pararmeter in every test you provide `autouse` .
`scope` defines the session of the program run
```python
import pytest
@pytest.fixture(scope="session",autouse=True)
def setup_test():
    print('Started setup')
    yeild
    print('End of test')

```


---

### 🔹 **6. Parametrize (Test Multiple Inputs)**

1st option is to parametrize with fixture 
```python
@pytest.fixture(params=["a","b"])
def demo_fixture(request):
    print(request.param)

def testlogin(demo_fixture):
    print("Login sucessful")
```

2nd option is to parametrize with mark 

```python
@pytest.mark.parametrize("a,b,result", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0)
])
def test_add(a, b, result):
    assert add(a, b) == result
```
3rd option : [pytest_generte_tests](https://docs.pytest.org/en/stable/how-to/parametrize.html#pytest-generate-tests) allows one to define custom parametrization schemes

```python
# content of conftest.py


def pytest_addoption(parser):
    parser.addoption(
        "--stringinput",
        action="append",
        default=[],
        help="list of stringinputs to pass to test functions",
    )


def pytest_generate_tests(metafunc):
    if "stringinput" in metafunc.fixturenames:
        metafunc.parametrize("stringinput", metafunc.config.getoption("stringinput"))

```
---

### 🔹 **7. Mocking (for APIs, Files, etc.)**

```python
from unittest.mock import patch

@patch("module.api_call")
def test_api(mock_api):
    mock_api.return_value = {"status": 200}
    result = module.api_call()
    assert result["status"] == 200
```

> You "pretend" something works, without actually calling it.

---

### 🔹 **8. Structuring Test Folders**

```
project/
│
├── app/
│   └── core.py
├── tests/
│   └── test_core.py
```

Run all tests with:
```bash
pytest
```
Perfect!  
Here’s a **clean professional-style Pytest Advanced Features Cheatsheet** you can use like a README or print for quick reference.

---

# 📄 pytest Advanced Features Cheatsheet

---

## ✅ pytest.mark (Markers)

| Purpose | Example | Usage |
|:---|:---|:---|
| Label tests with categories (like `slow`, `db`, `auth`,`sanity`) | `@pytest.mark.slow` | Run specific tests: `pytest -m slow` |
| Custom groupings for organization or CI pipelines | `@pytest.mark.api` | Run: `pytest -m api` |

---

## ✅ pytest.skip and pytest.xfail

| Purpose | Example | When To Use |
|:---|:---|:---|
| **Skip** a test temporarily | `@pytest.mark.skip(reason="Feature under development")` | Known unready tests |
| **Skipif** a test temporarily | `@pytest.mark.skipif(condition,reason="skipped condition")` | Known unready tests |
| **Expected failure** (known bug, won't block pipeline) | `@pytest.mark.xfail(reason="Bug ID 1234")` | Acknowledge known issues without failing suite |

---

## ✅ pytest.raises

| Purpose | Example | Usage |
|:---|:---|:---|
| Assert that a block of code raises an exception |  |
```python
with pytest.raises(ZeroDivisionError):
    divide(5, 0)
``` 
| Confirm correct error handling |
| Match exception message |  |
```python
with pytest.raises(ValueError, match="invalid literal"):
    int("abc")
``` 
| Check message for detailed validation |

---

## ✅ caplog (Capture Logs)

| Purpose | Example | Usage |
|:---|:---|:---|
| Capture log output during a test |  |
```python
def test_log_message(caplog):
    logger.info("Important log")
    assert "Important log" in caplog.text
``` 
| Validate that expected logging happens |

---

## ✅ monkeypatch (Temporary Replacements)

| Purpose | Example | Usage |
|:---|:---|:---|
| Mock or replace parts of system temporarily |  |
```python
def test_os_name(monkeypatch):
    monkeypatch.setattr('os.name', 'my_fake_os')
    assert get_os_name() == 'my_fake_os'
``` 
| Use for environment variables, functions, classes |

---

# ✨ Bonus Common pytest CLI Commands

| Command | What It Does |
|:---|:---|
| `pytest -v` | Verbose output (show each test) |
| `pytest -k "testname"` | Run tests matching substring |
| `pytest -m "marker"` | Run tests with specific marker |
| `pytest --maxfail=2` | Stop after 2 failures |
| `pytest --tb=short` | Shorter tracebacks on failure |
| `pytest -s filename.py` | to run specfic file |

---

# 🧠 Smart Rules of Thumb:

| Situation | Tool |
|:---|:---|
| Testing exception behavior? | Use `pytest.raises` |
| Organizing slow/fast/db tests? | Use `@pytest.mark` |
| Skipping temporary tests? | Use `@pytest.mark.skip` |
| Faking/mocking behavior? | Use `monkeypatch` |
| Validating log output? | Use `caplog` |

---

# 🚀 Example Combined Usage:

```python
import pytest

@pytest.mark.slow
def test_big_calculation():
    assert big_calc(1000000) > 0

@pytest.mark.skip(reason="Waiting for API access")
def test_api_call():
    assert call_api() == 200

def test_divide_zero():
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        divide(1, 0)

def test_log_output(caplog):
    logger.error("Something bad happened")
    assert "bad happened" in caplog.text

def test_fake_os(monkeypatch):
    monkeypatch.setattr('os.name', 'super_os')
    assert get_os_name() == 'super_os'
```

---

# 📋 Final Important Reminder:

✅ **pytest** is extremely powerful because of:
- **Clean syntax** (`assert` without extra libraries)
- **Flexible decorators** (`mark`, `fixture`, `parametrize`)
- **Built-in mocking** (`monkeypatch`, `caplog`)
- **Great error reporting** by default

---

---

### ✅ Summary

| Concept         | Purpose                           |
|------------------|-----------------------------------|
| `unittest`       | Basic test framework (built-in)   |
| `pytest`         | Clean, powerful, widely used      |
| `fixture`        | Set up test context               |
| `parametrize`    | Run one test with many inputs     |
| `mock`           | Isolate external systems          |

---

# 📘 Data-Driven Testing (DDT) with Pytest

Data-Driven Testing allows you to run the same test logic against multiple data inputs — clean, powerful, and highly maintainable.


---

## 📂 External File Data Example (JSON)

### 👉 `test_data.json`

```json
[
    {"a": 1, "b": 2, "expected": 3},
    {"a": 3, "b": 4, "expected": 7}
]
```

### 👉 test code

```python
import json
import pytest

# Load test data from JSON
with open("test_data.json") as f:
    data = json.load(f)

@pytest.mark.parametrize("entry", data)
def test_add_from_file(entry):
    assert entry["a"] + entry["b"] == entry["expected"]
```

---

## 📂 External File Data Example (CSV)

### 👉 `test_data.csv`

```
a,b,expected
1,2,3
4,5,9
```

### 👉 test code

```python
import csv
import pytest

def read_csv_data():
    with open('test_data.csv', newline='') as f:
        reader = csv.DictReader(f)
        return [(int(r['a']), int(r['b']), int(r['expected'])) for r in reader]

@pytest.mark.parametrize("a, b, expected", read_csv_data())
def test_add_from_csv(a, b, expected):
    assert a + b == expected
```

---

## 💡 Summary

| Tool                       | Use                           |
| -------------------------- | ----------------------------- |
| `@pytest.mark.parametrize` | Built-in Pytest way to do DDT |
| `json.load()`              | Read test cases from JSON     |
| `csv.DictReader()`         | Read test cases from CSV      |

---

📌 **Best Practice:** Keep your test logic clean, move test data to external files when the data grows large.




