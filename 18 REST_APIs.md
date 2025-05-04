# 🌐 REST API Cheatsheet for Interviews

A practical reference covering REST, RESTful, key HTTP concepts, status codes, and tooling — with theory and comparisons tailored for interview prep.


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

