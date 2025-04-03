Awesome. Now we move into **Step 9: Unit Testing & Pytest**—absolutely core for a **Test Engineer** role, especially at a place like SIG.

---

## **Step 9: Unit Testing & Pytest**

---

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

```python
import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3]

def test_sum(sample_data):
    assert sum(sample_data) == 6
```

---

### 🔹 **5. Parametrize (Test Multiple Inputs)**
```python
@pytest.mark.parametrize("a,b,result", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0)
])
def test_add(a, b, result):
    assert add(a, b) == result
```

---

### 🔹 **6. Mocking (for APIs, Files, etc.)**

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

### 🔹 **7. Structuring Test Folders**

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

**Mini Task:**  
Write a function that multiplies two numbers and create a `pytest` test file to test it with 3 values.

---

Ready to hit **Step 10: Automation, Subprocess & CLI tools** next?