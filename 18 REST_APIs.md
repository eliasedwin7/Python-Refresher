# 🌐 REST API Cheatsheet for Interviews


## 📘 REST vs RESTful

| Term      | Meaning |
|-----------|---------|
| **REST**  | An **architectural style** with a set of constraints for designing networked applications. |
| **RESTful** | A **service that follows REST principles** (stateless, client-server, cacheable, etc.). |

🧠 **Think of REST as the rules. RESTful is the player following them.**

---

## 🔧 Core HTTP Methods

| Method  | Purpose                  | Example                        |
|---------|--------------------------|--------------------------------|
| GET     | Retrieve data            | `GET /users/1`                 |
| POST    | Create a new resource    | `POST /users`                  |
| PUT     | Update full resource     | `PUT /users/1`                 |
| PATCH   | Update part of resource  | `PATCH /users/1`               |
| DELETE  | Delete resource          | `DELETE /users/1`              |

---

## 🔑 Key REST Constraints (Theory)

1. **Client-Server**: UI and backend are separate.
2. **Stateless**: No session on the server. Each request is self-contained.
3. **Cacheable**: Responses must indicate cacheability.
4. **Uniform Interface**: Standard way to interact (HTTP, URLs, status codes).
5. **Layered System**: You don’t know what layers are in between.
6. **Code on Demand (Optional)**: Server can send code to client (e.g., JS).

---

## 📊 Common HTTP Status Codes

| Code | Meaning                  | When to Use                   |
|------|--------------------------|-------------------------------|
| 200  | OK                       | Successful GET/PUT/DELETE     |
| 201  | Created                  | After successful POST         |
| 204  | No Content               | Success, nothing to return    |
| 400  | Bad Request              | Client input is invalid       |
| 401  | Unauthorized             | Invalid or missing token      |
| 403  | Forbidden                | Valid token, but no access    |
| 404  | Not Found                | Resource does not exist       |
| 409  | Conflict                 | Resource already exists       |
| 500  | Internal Server Error    | Unexpected server failure     |

---

## ⚙️ REST vs SOAP vs GraphQL

| Feature     | REST           | SOAP              | GraphQL           |
|-------------|----------------|-------------------|--------------------|
| Protocol    | HTTP           | HTTP, SMTP        | HTTP              |
| Format      | JSON, XML      | XML only          | JSON              |
| Flexibility | Medium         | Low               | High              |
| Best For    | Web APIs       | Enterprise apps   | Frontend devs     |

---

## 🧠 Interview Concepts to Prepare

### 1. **PUT vs PATCH**

| PUT | PATCH |
|-----|-------|
| Full replacement | Partial update |
| Idempotent | Idempotent (usually) |

---

### 2. **Idempotency**

> An operation is idempotent if repeating it gives the same result.

- ✅ `GET`, `PUT`, `DELETE`
- ❌ `POST` (usually creates new)

---

### 3. **URI Design Best Practices**

✅ Good:
```

GET /users/1

```

❌ Bad:
```

GET /getUser?id=1

````

- Use **nouns**, not verbs
- Use **lowercase** and **hyphens**
- Keep URIs versioned (`/api/v1/`)

---

### 4. **HATEOAS (Advanced)**

> Hypermedia As The Engine Of Application State  
Response includes links to possible next actions.

Example:
```json
{
  "id": 1,
  "name": "Edwin",
  "links": [
    { "rel": "self", "href": "/users/1" },
    { "rel": "delete", "href": "/users/1" }
  ]
}
````

---

## 🧪 API Testing Tools

| Tool       | Purpose               |
| ---------- | --------------------- |
| Postman    | Manual API testing    |
| Curl       | CLI-based HTTP calls  |
| HTTPie     | Clean CLI API testing |
| Swagger UI | Visual API docs & try |
| Pytest     | Automated API testing |

---

## 🧰 Curl Examples

```bash
# GET
curl https://api.example.com/users

# POST
curl -X POST -H "Content-Type: application/json" \
  -d '{"name": "Edwin"}' https://api.example.com/users

# PUT
curl -X PUT -d '{"email": "new@example.com"}' https://api.example.com/users/1

# DELETE
curl -X DELETE https://api.example.com/users/1
```

---

## 🔐 Authentication Tips

* Use **Authorization** header:

```http
Authorization: Bearer <token>
```

* Support `401 Unauthorized` for invalid/missing token.
* Use refresh tokens, rate-limiting, and HTTPS in production.

---

## 🎓 Interview Pro Tips

* ✅ Explain **statelessness** and **idempotency** clearly.
* ✅ Know when to use **PUT** vs **PATCH**.
* ✅ Mention **Swagger/OpenAPI** for API docs.
* ✅ Be ready to test with `curl`, `Postman`, or `pytest + requests`.

---

## ✅ URI = **Uniform Resource Identifier**

In REST APIs, a **URI identifies a resource** — like a specific user, product, or file. It's the “address” you send your HTTP request to.

---

## 🧱 URI Structure

```
https://api.example.com/users/123
└───┬────────────┘ └──────┬──────┘
   Domain               Path → resource (`user` with ID `123`)
```

---

## 🧠 In REST, URI should be:

| Principle                | Example                         | ✅ or ❌ |
| ------------------------ | ------------------------------- | ------ |
| Use **nouns**, not verbs | `/users` instead of `/getUsers` | ✅      |
| Be **hierarchical**      | `/users/123/orders/456`         | ✅      |
| Avoid action words       | `/createUser` or `/deleteUser`  | ❌      |
| Use plural nouns         | `/products`, `/orders`          | ✅      |

---

## 🔹 Examples of REST URIs

| Action              | Method | URI Example |
| ------------------- | ------ | ----------- |
| Get all users       | GET    | `/users`    |
| Get user with ID 10 | GET    | `/users/10` |
| Create new user     | POST   | `/users`    |
| Update user         | PUT    | `/users/10` |
| Delete user         | DELETE | `/users/10` |

---

## 🧾 Difference: URI vs URL vs URN

| Term | Stands for                  | Meaning                                                         |
| ---- | --------------------------- | --------------------------------------------------------------- |
| URI  | Uniform Resource Identifier | General term for identifying a resource                         |
| URL  | Uniform Resource Locator    | A URI that tells where to find the resource (includes protocol) |
| URN  | Uniform Resource Name       | A URI that names a resource without location                    |

📝 In REST, **URL = URI** for all practical purposes.

---


Here’s a clear and interview-ready breakdown of **REST API**, **SOAP**, and the key comparison points you need to remember:

---

# 🌐 What is a REST API?

**REST (Representational State Transfer)** is a web service architecture that uses **HTTP methods** to access and manipulate resources (like users, products, files) via **URLs**.

### ✅ Key Concepts:

* **Stateless**: Each request is independent
* **Uses HTTP**: GET, POST, PUT, DELETE
* **Resource-based**: Everything is treated as a resource with a URI
* **Data format**: Usually JSON (also XML, plain text)
* **Lightweight & Fast**: Preferred for modern web/mobile apps

---

### 🧠 Points to Remember for REST API

| Topic         | Explanation                                                                     |
| ------------- | ------------------------------------------------------------------------------- |
| HTTP methods  | `GET`, `POST`, `PUT`, `DELETE`, `PATCH`                                         |
| Status codes  | `200 OK`, `201 Created`, `400 Bad Request`, `404 Not Found`, `500 Server Error` |
| URI naming    | Use **nouns**: `/users`, `/orders/1`                                            |
| Format        | JSON is most common (`application/json`)                                        |
| Idempotency   | `GET`, `PUT`, `DELETE` are idempotent (safe to repeat)                          |
| Testing tools | Postman, Curl, REST Assured, Python `requests`                                  |
| Security      | API keys, OAuth, JWT, HTTPS                                                     |

---

### 🔧 Sample REST API Call (GET)

```http
GET /users/101 HTTP/1.1
Host: api.example.com
```

Response (JSON):

```json
{
  "id": 101,
  "name": "Edwin"
}
```

---

# 🧽 What is SOAP?

**SOAP (Simple Object Access Protocol)** is a protocol for exchanging **structured information** via **XML** over HTTP, SMTP, etc.

### ❗Key Features:

* **Strict and heavy** (uses XML schemas)
* **Protocol-based**, not just an architecture
* **WSDL** (Web Services Description Language) used for contracts
* Better for **enterprise-level applications** requiring **ACID-compliant transactions**, **security**, and **formal standards**

---

## 🔁 REST vs SOAP: Quick Comparison

| Feature         | REST                | SOAP             |
| --------------- | ------------------- | ---------------- |
| Protocol        | Architectural style | Protocol         |
| Data Format     | JSON, XML           | Only XML         |
| Speed           | Faster, lightweight | Slower, verbose  |
| Flexibility     | More flexible       | Strictly defined |
| Security        | OAuth, HTTPS        | WS-Security      |
| Contract (WSDL) | Optional            | Required         |

---

## 📌 Interview Tip:

**“When would you choose SOAP over REST?”**

> *If the system demands formal contracts (WSDL), strong security, or ACID-compliant transactions — like in banking or legacy enterprise systems.*

---

