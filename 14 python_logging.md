#  Python Logging Cheatsheet

Python's `logging` module helps you track what's happening in your code — useful for debugging, monitoring, and production diagnostics.

---

## 🔹 Logging Levels

| Level      | Purpose                            |
| ---------- | ---------------------------------- |
| `DEBUG`    | Detailed info, for diagnostics     |
| `INFO`     | General info (start, stop, config) |
| `WARNING`  | Unexpected, but non-breaking       |
| `ERROR`    | A serious issue, something broke   |
| `CRITICAL` | Very serious, may stop the program |

---

## 🔹 Basic Usage

```python
import logging

logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")
```

---

## 🔹 Logging to a File

```python
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename='example.log',
    level=logging.DEBUG,
    filemode='w'  # overwrite on each run
)
```

---

## 🔹 Custom Format

```python
import logging

logging.basicConfig(
    format='%(levelname)s:%(message)s',
    level=logging.DEBUG
)

logging.debug('This is a debug message')
```

---

## 🔹 Date & Time in Logs

```python
import logging

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logging.info('Logged with timestamp')
```

---

## 🔹 Logging to File & Console Simultaneously

```python
import logging

logger = logging.getLogger(__name__) #dispaly the function name
logger.setLevel(logging.DEBUG)

# File Handler
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)

# Console Handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add Handlers
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.debug("This goes to file")
logger.info("This goes to both")
logger.error("This goes to both")
```

---

💡 Pro Tip: Always use `getLogger(__name__)` in modules so log messages show where they came from.
