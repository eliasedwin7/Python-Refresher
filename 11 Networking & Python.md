# ✅ **Step 12: Networking & Python**

We’ll go over:

1. **HTTP requests** with `requests`  
2. **Socket programming** (TCP/UDP)  
3. **Working with APIs**  
4. **JSON, headers, timeouts, status codes**  
5. **Common networking tools for test automation**

---

### 🔹 1. HTTP Requests with `requests` Library

#### ✅ Basic GET request
```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.json())
```

---

#### ✅ POST request with payload
```python
data = {"username": "edwin", "password": "test123"}
response = requests.post("https://example.com/api/login", json=data)

print(response.status_code)
print(response.json())
```

---

#### ✅ Headers and Timeout
```python
headers = {"Authorization": "Bearer TOKEN123"}
response = requests.get("https://api.site.com/data", headers=headers, timeout=5)
```

> Always set a timeout! Otherwise the script can hang forever on network errors.

---

### 🔹 2. Consuming and Testing APIs

```python
def get_user_data(user_id):
    url = f"https://reqres.in/api/users/{user_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None
```

✅ Great for:
- Health checks
- Mock test APIs
- Writing automation tools

---

### 🔹 3. Socket Programming (Low-Level TCP/UDP)

#### ✅ TCP Server (basic)
```python
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen(1)

conn, addr = server.accept()
print("Connected by", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    print("Received:", data.decode())
    conn.sendall(b"ACK")
conn.close()
```

#### ✅ TCP Client
```python
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))
client.sendall(b"Hello")
data = client.recv(1024)
print("Received:", data.decode())
client.close()
```

🔸 Used when testing communication protocols, microservices, or internal message passing.

---

### 🔹 4. Ping a Server / Host

```python
import subprocess

def ping(host):
    return subprocess.run(["ping", "-c", "1", host], capture_output=True).returncode == 0

print(ping("google.com"))  # True if host is reachable
```

> Useful in automated health checks or device readiness tests.

---

### 🔹 5. WebSocket Clients

For real-time data feeds (common in finance/trading):
```python
# pip install websocket-client
import websocket

def on_message(ws, message):
    print("Message:", message)

ws = websocket.WebSocketApp("wss://echo.websocket.org", on_message=on_message)
ws.run_forever()
```

---

### ✅ Summary

| Tool              | Use Case                             |
|-------------------|----------------------------------------|
| `requests`        | HTTP requests to REST APIs             |
| `socket`          | Custom TCP/UDP communication           |
| `subprocess`      | Call networking tools (`ping`, `curl`) |
| `websocket-client`| Real-time data feeds                   |

---