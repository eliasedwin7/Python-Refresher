# ☁️ Amazon S3 Interview Prep (Theory)

---

## 📌 What is Amazon S3?

* **S3 = Simple Storage Service**
* It is a **scalable, durable, object-based storage service** by AWS.
* You can store **any amount of data**, such as files, logs, media, backups, etc.

---

## 📦 Key Concepts

| Term                    | Description                                                          |
| ----------------------- | -------------------------------------------------------------------- |
| **Bucket**              | A container for storing files (objects). Unique across AWS globally. |
| **Object**              | A single file in S3. Includes data + metadata.                       |
| **Key**                 | The unique name (or full path) of an object in a bucket.             |
| **Region**              | Physical AWS data center location where your S3 bucket resides.      |
| **Storage Class**       | Controls cost/durability/access speed (e.g., Standard, Glacier, IA). |
| **ACL / Bucket Policy** | Used for access control — who can access and what operations.        |

---

## 🔐 Access Control & Security

1. **Bucket Policies** – JSON-based rules at the bucket level
2. **IAM Policies** – Set user or role-based permissions
3. **ACLs** – Legacy way to manage object-level permissions
4. **Encryption**

   * SSE-S3 (server-side, AWS-managed keys)
   * SSE-KMS (server-side, customer-managed keys)
   * Client-side encryption (done before upload)

---

## 📊 S3 Use Cases

* Static website hosting
* Backup and restore
* Software distribution
* Media storage
* Data lake for analytics
* CI/CD artifact storage

---

## 💬 Common Interview Questions & Sample Answers

---

### ❓ 1. What’s the difference between S3 and EBS?

**Answer:**

* S3 is **object storage**, used for storing files like images, logs, etc.
* EBS is **block storage**, used for EC2 volumes (like a hard drive).

---

### ❓ 2. How is data secured in S3?

**Answer:**

* By default, everything is private.
* Access can be given using **IAM policies, bucket policies, or pre-signed URLs**.
* Data can be encrypted using SSE or KMS.
* Logging and versioning help track changes and access.

---

### ❓ 3. What is S3 versioning?

**Answer:**

* It stores **every version** of every object.
* Helps in recovery after accidental deletes or overwrites.
* Cannot be disabled once enabled (only suspended).

---

### ❓ 4. What is the difference between S3 Standard and S3 Glacier?

**Answer:**

| S3 Standard     | S3 Glacier                     |
| --------------- | ------------------------------ |
| Frequent access | Long-term archival             |
| Fast access     | Slower retrieval (minutes–hrs) |
| Higher cost     | Lower storage cost             |

---

### ❓ 5. What are pre-signed URLs?

**Answer:**

* URLs that allow temporary, secure access to a private object.
* Often used to let someone download a file without making the bucket public.

---

## 🚦S3 Key Features Summary

| Feature         | Notes                               |
| --------------- | ----------------------------------- |
| Durability      | 99.999999999% (11 9's)              |
| Availability    | 99.99% uptime                       |
| Unlimited Data  | Store from bytes to petabytes       |
| Global Access   | Access via HTTP/HTTPS from anywhere |
| Event Triggers  | Can invoke Lambda on upload/delete  |
| Lifecycle Rules | Auto-archive or delete based on age |

---

## 🧠 Tips for Interviews

* Focus on **use cases, security, and lifecycle management**.
* Emphasize **real-world usage** in CI/CD pipelines or test result archiving.
* Know basic differences between **S3 vs. EBS vs. EFS**.
