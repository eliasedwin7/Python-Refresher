# 🚀 Git Quick Reference Guide

## 📁 Git Project Structure

Git works across three areas:

* **Working Directory**: Your local codebase
* **Staging Area**: Where changes wait to be committed
* **Git Repository**: The `.git/` folder that stores commit history and metadata

---

## 🔧 Scenario 1: You Are the Architect (Create a New Project)

You're setting up a Git project from scratch:

```bash
git status                      # See current state of files
git init                        # Initialize a new Git repo
git add filename                # Stage a specific file
git add .                       # Stage all files
git commit -m "Initial commit" # Commit with message

git config --global user.name "Your Name"
git config --global user.email "you@example.com"

git branch -m main                             # Rename default branch to main
git remote add origin https://repo.url.git     # Link to remote repo
git push -u origin main                        # Push to remote
```

### 📄 `.gitignore`

Use this file to exclude files/folders from being tracked (e.g., `__pycache__/`, `.env`, `.vscode/`)

---

## 🔧 Scenario 2: You Join an Existing Project (Team Member)

You work on top of an already setup project:

```bash
git clone https://repo.url.git    # Download repo
cd repo-name
# Make changes
git add .
git commit -m "My changes"
git push
```

### 🔄 End-to-End Team Workflow

1. `git clone`
2. Start working on your feature
3. Make changes
4. Run `git pull` to get latest changes (merge if needed)
5. Stage and commit
6. Push to your branch
7. Open a pull request

---

## 🌿 Branching Strategy

* **main** is the production or baseline branch
* Developers create separate **feature branches** and work in isolation

```bash
git branch                       # List branches
git checkout -b feature_branch   # Create and switch to new branch
git add .
git commit -m "Your message"
git push origin feature_branch   # Push to remote branch
```

### 🔁 Pull Request Flow

1. Push your feature branch
2. Open a Pull Request (PR) on GitHub/GitLab
3. Review, comment, approve
4. Merge to main if no conflicts

---

## ⚔️ Merge Conflicts

Happen when two branches edit the same part of a file.

Conflict looks like this:

```diff
<<<<<<< HEAD
Your branch's changes
=======
Incoming branch's changes
>>>>>>> feature_branch
```

### To Resolve:

1. Manually fix the code
2. Run: `git add .`
3. Run: `git commit`
4. Run: `git push`

---

## 🧰 Useful Git Commands

```bash
git diff                         # See unstaged changes
git diff --cached                # See staged changes
git diff commit1 commit2         # Compare two commits
git reset filename               # Unstage a file
git tag v1.0.0                   # Create a tag
git branch -d branch_name        # Delete local branch
git remote set-url origin URL    # Change the repo URL
git log --oneline --graph        # Visual commit history
```

---

🔧 Use this guide when you’re:

* Setting up your own repo
* Contributing to a team
* Managing merge conflicts and branches


