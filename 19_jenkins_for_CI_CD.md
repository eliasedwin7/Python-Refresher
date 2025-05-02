# 🚀 CI/CD with Jenkins – Quick Guide for Testers

---

## 🧩 CI/CD Pipeline Steps

1. **Code Check-in**
   Developer pushes code to GitHub/GitLab/Bitbucket.

2. **Build**
   Jenkins pulls the latest code, compiles/builds it.

3. **Test**
   Jenkins runs unit tests, integration tests, UI tests, etc.

4. **Results**
   Test results (pass/fail, logs, reports) are stored and/or emailed.

---

## 👨‍🔧 DevOps Role

* Set up the **Jenkins master/slave (agent)** servers
* Configure **build triggers**
* Manage system-level dependencies
* Maintain **credentials, secrets**, and **network access**

---

## 👩‍💻 Tester’s Role

You as a tester may:

1. **Configure or monitor Jenkins jobs** post-deployment
2. Set the job to run:

   * **After every code change**
   * **Once a day** (scheduled build)
3. Review test results, logs, and metrics
4. Connect **test scripts** (like Selenium, Pytest) into the pipeline

---

## 🧪 Job Example: Freestyle Project

1. In Jenkins → New Item → **Freestyle project**
2. **Add build step** → “Execute Windows batch command”

   ```cmd
   pytest tests/
   ```

---

## 🔧 Jenkins Parameters

You can make your Jenkins job interactive by using:

| Parameter Type | Use Case                             |
| -------------- | ------------------------------------ |
| **String**     | Enter a test name or URL             |
| **Choice**     | Dropdown (e.g., dev, staging)        |
| **Boolean**    | True/False toggle (e.g., run smoke?) |

---

## 🔗 Integrating GitHub

* Use **Git plugin**
* Provide Git repo URL
* Set credentials if private
* Use **webhook** for auto-trigger on code push

---

## 📧 Email Notifications

1. Install **Email Extension Plugin**
2. Configure SMTP in **Manage Jenkins > System Config**
3. Use “Post-build Actions” → **Editable Email Notification**
4. Add trigger: e.g., "Send when build fails"

---

## ⚙️ Groovy Scripts in Jenkins

* Used for **Jenkins Pipeline as Code** (Jenkinsfile)
* DSL (Domain-Specific Language) for scripting builds
* More powerful than freestyle jobs

### Example Groovy (Jenkinsfile):

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest tests/'
            }
        }
    }
}
```

---

## 🛠 What are BUILD Files?

* **Not a Jenkins concept by default**
* Common in tools like:

  * `Bazel` → uses `BUILD` and `WORKSPACE` files to describe builds
  * `Gradle` → uses `build.gradle`
  * `Maven` → uses `pom.xml`

In Jenkins, you may call:

```groovy
sh './gradlew build'
```

---

## 📌 Summary

| Area            | Tool / Concept          |
| --------------- | ----------------------- |
| Job Type        | Freestyle, Pipeline     |
| Script Support  | Bash, Batch, Groovy     |
| Variables       | Choice, String, Boolean |
| Notifications   | Email, Slack, Teams     |
| SCM Integration | GitHub, GitLab          |
| Scheduling      | Cron expressions        |
| Advanced Logic  | Groovy / Jenkinsfile    |

---

