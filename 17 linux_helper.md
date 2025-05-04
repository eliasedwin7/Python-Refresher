# 🐧 Linux Essentials for Interviews

This guide focuses on **real-world, practical Linux commands** and concepts interviewers typically care about — especially for developers, testers, SREs, or automation roles.

---

## 🔧 Basic Navigation

```bash
pwd             # Print current directory
ls -l           # List with details
ls -a           # Include hidden files
cd /path        # Change directory
cd ..           # Go one level up
mkdir mydir     # Create directory
touch file.txt  # Create empty file
rm file.txt     # Delete file
rm -r folder/   # Delete directory recursively
```

---

## 📄 File Viewing & Editing

```bash
cat file.txt           # Print file contents
less file.txt          # View file page by page
head -n 10 file.txt    # First 10 lines
tail -n 10 file.txt    # Last 10 lines
tail -f logfile.log    # Live log tailing
nano file.txt          # Edit file (simple editor)
vim file.txt           # Vim editor (pro-level)
```

---

## 🔍 Searching & Filtering

```bash
grep "error" file.log          # Search for "error"
grep -r "TODO" .               # Recursive search
find . -name "*.py"            # Find files by pattern
find /etc -type f -mtime -1    # Files modified in last 1 day
```

---

## 📦 File Permissions & Ownership

```bash
ls -l                        # Show file permissions
chmod +x script.sh           # Make file executable
chmod 755 file.sh            # rwxr-xr-x
chown user:group file.txt    # Change owner
```

---

## 🧰 Process & System Info

```bash
ps aux                       # List running processes
top                          # Live CPU/memory info
htop                         # Better top (if installed)
kill -9 <pid>                # Force kill process
df -h                        # Disk usage
du -sh folder/               # Folder size
free -h                      # RAM usage
uptime                       # How long the system's been up
```

---

## 🔄 Networking & Ports

```bash
ifconfig or ip a             # Show IP addresses
ping google.com              # Test connectivity
netstat -tuln                # Open ports
ss -tuln                     # Newer alternative to netstat
curl http://localhost:8000  # HTTP request
wget https://site.com/file  # Download file
```

---

## 📁 File Compression & Archiving

```bash
tar -cvf archive.tar folder/        # Create tar
tar -xvf archive.tar                # Extract tar
gzip file.txt                       # Compress
gunzip file.txt.gz                  # Decompress
zip -r archive.zip folder/         # Zip
unzip archive.zip                   # Unzip
```

---

## ⛓️ Permissions & Users

```bash
whoami                      # Current user
id                          # User + group IDs
sudo command                # Run as root
su -                        # Switch to root
adduser newuser             # Add user
usermod -aG sudo newuser    # Add user to sudo group
```

---

## 💡 Interview-Focused Topics

| Topic                  | Questions They Might Ask                       |
| ---------------------- | ---------------------------------------------- |
| File Permissions       | `chmod`, `chown`, `ls -l`                      |
| Process Management     | `ps`, `kill`, `top`, `&`, `nohup`              |
| Logs & Monitoring      | `tail -f`, `/var/log`, `grep`, `journalctl`    |
| Networking             | `netstat`, `ss`, `curl`, `ping`, `iptables`    |
| Shell Scripting Basics | `#!/bin/bash`, loops, conditions, `$1`, `echo` |
| Scheduling Jobs        | `crontab -e`, `* * * * *`                      |
| Disk Usage             | `df -h`, `du -sh`, `mount`, `lsblk`            |
| Package Managers       | `apt`, `yum`, `dnf`, `pip`                     |

---

## 📌 Bonus: Scripting Snippet

```bash
#!/bin/bash
for file in *.txt; do
  echo "Processing $file"
  wc -l "$file"
done
```

---
