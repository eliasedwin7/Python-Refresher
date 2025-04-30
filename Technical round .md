**second-round technical interview** at **QuintessenceLabs**:
---

### 🔍 **1. Deep Dive into Your Experience**
Expect questions like:
- “Walk us through how you tested an API or full system.”
- “How do you approach debugging when something fails in CI/CD?”
- “Have you written your own automation scripts? Show us how.”

📌 **Tip:** Use STAR (Situation, Task, Action, Result) to structure your answers clearly.

---

### 🧪 **2. Practical Testing Scenarios**
They may give you a scenario like:
> “You’re testing a key management system. What would you check?”

Focus on:
- Input validation  
- API behavior  
- Security (key leakage, access control)  
- Integration with other systems

---

### 🧑‍💻 **3. Automation & Scripting Task**
You might be asked to:
- Write a **PyTest test case**
- Automate an API test using Python `requests`
- Interpret a failed Jenkins pipeline log
- Explain test output or trace a bug

📌 **Prepare a few quick scripts** you’ve written recently — they may ask for code sharing or whiteboarding.

---

### 🔐 **4. Security Awareness**
They may quiz you on:
- What makes a random number *secure*?
- How would you test a **secure key store**?
- Difference between **encryption** and **hashing**

---

### 🧠 **5. Problem Solving & Communication**
Expect:
- Logic puzzles or test strategy problems  
- Questions on **how you’d test without full requirements**
- How you collaborate with devs during a release crunch

---

### ✅ What to prep:
- REST API testing (Postman + Python scripts)
- PyTest basics and `assert` usage
- Jenkins + Git workflow (pipelines, PRs, merge conflicts)
- System testing scenarios
- Basic networking + encryption terms (TLS, RSA, AES)

---

---

### ✅ **1. REST API Testing (Postman + Python)**

**What to know:**
- How to send GET, POST, PUT, DELETE requests
- How to validate status codes, headers, and JSON bodies

**In Postman:**  
- Auth tab for Bearer/Basic tokens  
- Tests tab: `pm.response.code === 200`  
- Save environment variables (like `{{token}}`)

**In Python (requests + pytest):**
```python
import requests

def test_get_user():
    response = requests.get("https://api.example.com/user/1")
    assert response.status_code == 200
    assert "username" in response.json()
```

🎤 *In interview:*  
**“I use Postman to validate API responses and check status codes, headers, and JSON fields. For automation, I write PyTest-based scripts using the `requests` library to test all positive and negative paths.”**

---

### ✅ **2. PyTest + assert Usage**

**Key things:**
- Use `assert` for expected values
- Parametrize tests to reduce code duplication
- Use fixtures for setup/teardown

```python
import pytest

@pytest.mark.parametrize("x, y, result", [(1, 2, 3), (2, 2, 4)])
def test_add(x, y, result):
    assert x + y == result
```

🎤 *In interview:*  
**“I write modular tests with PyTest, using parametrize to cover multiple inputs and fixtures to manage setup and teardown. Assertions help validate behavior in each scenario.”**

---

### ✅ **3. Jenkins + Git Workflow**

**Jenkins Pipeline Stages:**
1. Checkout from Git
2. Build
3. Test (run PyTest or similar)
4. Deploy (if applicable)

**Git Concepts:**
- Create branches for features
- Use PRs to merge code into `main`
- Resolve merge conflicts manually (`git mergetool`)

🎤 *In interview:*  
**“I integrate test scripts into Jenkins pipelines that trigger on every PR. I’ve configured jobs to run unit tests and API tests automatically. For Git, I follow a branch–PR–review workflow and am comfortable resolving conflicts.”**

---

### ✅ **4. System Testing Scenarios**

Be ready for questions like:
- “How would you test a key management system?”
- “How would you test a secure login flow?”

Think of:
- **Data flow testing**
- **Auth & permissions**
- **Boundary testing**
- **Integration between services (e.g., key gen + storage)**

🎤 *In interview:*  
**“In system testing, I focus on end-to-end flows, validating interactions across components. For example, when testing a key manager, I’d test generation, storage, retrieval, access control, and error handling.”**

---

### ✅ **5. Networking + Encryption Basics**

**TLS:** Creates an encrypted tunnel between browser/server  
**AES:** Fast symmetric encryption (same key for encrypt/decrypt)  
**RSA:** Asymmetric (public/private key) — slow but secure  
**Ports:** E.g., HTTPS uses 443  
**IP Protocols:** TCP for reliable delivery, UDP for speed

🎤 *In interview:*  
**“I understand that TLS encrypts data in transit, RSA is used for key exchange, and AES handles actual data encryption. I’m also familiar with concepts like IP addressing, ports, and firewalls in secure communication.”**


### 🔄 **REST vs RESTful API**

#### ✅ **REST (Representational State Transfer)**
- It’s an **architectural style** — a **set of rules or principles** for designing networked APIs.
- Think of it like the **blueprint** for how APIs should behave.

To be RESTful, an API must:
- Use **HTTP methods** (GET, POST, PUT, DELETE)
- Be **stateless** (no session stored on server)
- Use **URI** to identify resources (like `/users/1`)
- Return **JSON or XML** (commonly JSON now)

---

#### ✅ **RESTful API**
- It’s an **actual implementation** of those REST principles.
- If your API follows REST rules, it’s a **RESTful API**.

---

### 🧠 Simple analogy:
- **REST** is the *rulebook*.
- A **RESTful API** is a *game that follows the rulebook*.

---

🎤 **In interview, say:**
> “REST is a design philosophy for building APIs, and a RESTful API is one that follows those REST principles — using HTTP methods, being stateless, and exposing resources through URIs.”

Want a one-liner summary too?