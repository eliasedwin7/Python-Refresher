# Repo for selenium code

## 📘 Selenium WebDriver Commands Cheat Sheet
| **Operation**                        | **Command**                           | **Method/Property** | **Description**                                                                 |
|-------------------------------------|----------------------------------------|----------------------|---------------------------------------------------------------------------------|
| Navigate to URL                     | driver.get("https://example.com")      | Method               | Opens the URL in the browser session                                           |
| Get Current URL                     | driver.current_url                     | Property             | Returns the current URL from the browser's address bar                         |
| Back                                | driver.back()                          | Method               | Simulates the browser's back button                                            |
| Forward                             | driver.forward()                       | Method               | Simulates the browser's forward button                                         |
| Refresh Page                        | driver.refresh()                       | Method               | Reloads the current page                                                       |
| Get Page Title                      | driver.title                           | Property             | Returns the title of the current page                                          |
| Maximize Window                     | driver.maximize_window()               | Method               | Enlarges window to fill the screen (not full screen)                           |
| Minimize Window                     | driver.minimize_window()               | Method               | Minimizes the current window                                                   |
| Full Screen Window                  | driver.fullscreen_window()             | Method               | Fills screen like F11 key                                                      |
| Close Current Window                | driver.close()                         | Method               | Closes the current tab/window                                                  |
| Quit Browser                        | driver.quit()                          | Method               | Closes all tabs and ends the WebDriver session                                 |
| Get Page Source                     | driver.page_source                     | Property             | Returns HTML source of the page                                                |
| Find Element by ID                  | driver.find_element(By.ID, "id")       | Method               | Locates a single element by ID                                                 |
| Find Elements by Class Name         | driver.find_elements(By.CLASS_NAME, "class") | Method         | Locates all matching elements by class name                                    |
| Send Text to Input Field            | element.send_keys("text")              | Method               | Sends keystrokes to input field                                                |
| Click on Element                    | element.click()                        | Method               | Clicks the specified element                                                   |
| Clear Input Field                   | element.clear()                        | Method               | Clears any existing text in the field                                          |
| Get Element Text                    | element.text                           | Property             | Gets the visible text of an element                                            |
| Get Element Attribute               | element.get_attribute("attribute")     | Method               | Returns the value of a specified attribute                                     |
| Take Screenshot                     | driver.save_screenshot("screenshot.png") | Method             | Captures screenshot of current browser window                                  |

In Selenium, when you interact with a WebElement, you can access various **properties** and **methods** to extract or manipulate information.


### 🔍 **Common Properties & Methods of a WebElement**

| **Property/Method**                  | **Type**     | **Description**                                                                 |
|-------------------------------------|--------------|---------------------------------------------------------------------------------|
| `element.text`                      | Property     | Gets the visible text inside the element                                        |
| `element.tag_name`                  | Property     | Returns the tag name (like `div`, `input`, `a`)                                |
| `element.size`                      | Property     | Returns the size of the element as a dict: `{'height':..., 'width':...}`       |
| `element.location`                  | Property     | Returns the X, Y coordinates of the element                                     |
| `element.is_displayed()`            | Method       | Returns `True` if the element is visible                                        |
| `element.is_enabled()`              | Method       | Returns `True` if the element is enabled (usable)                              |
| `element.is_selected()`             | Method       | Returns `True` if the element (checkbox/radio) is selected                      |
| `element.get_attribute("name")`     | Method       | Gets the value of the specified attribute (like `href`, `value`, etc.)         |
| `element.get_dom_attribute("name")` | Method       | Gets the raw DOM attribute (even if not reflected in HTML attribute)           |
| `element.get_property("name")`      | Method       | Gets the JavaScript DOM property (not always the same as HTML attribute)       |
| `element.screenshot("el.png")`      | Method       | Takes a screenshot of the specific element                                     |
| `element.rect`                      | Property     | Returns `{'height', 'width', 'x', 'y'}` of the element                         |
| `element.value_of_css_property("property")` | Method | Gets the value of a CSS property like `color`, `font-size`, `background-color` |



### 🎯 What is `Select`?

- It's a **special Selenium class** that helps you easily **interact with `<select>` dropdown menus**.
- You use `Select` **only** when you are dealing with `<select>` HTML tags (the classic dropdowns).
- It gives you clean methods like **select by visible text**, **select by index**, **select by value**.

---

### 🧪 Simple Example

Imagine this HTML:

```html
<select id="cars">
  <option value="volvo">Volvo</option>
  <option value="saab">Saab</option>
  <option value="mercedes">Mercedes</option>
</select>
```

You can control it using:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.example.com")  # page with select box

dropdown = Select(driver.find_element(By.ID, "cars"))

dropdown.select_by_visible_text("Saab")
# or
dropdown.select_by_value("mercedes")
# or
dropdown.select_by_index(0)  # 0 = Volvo
```

---

### 📋 Quick Cheat Sheet: `Select` Class Methods

| **Method**                       | **Description**                      |
|-----------------------------------|--------------------------------------|
| `select_by_visible_text("text")`  | Select option matching the visible text |
| `select_by_value("value")`        | Select option by the `value` attribute |
| `select_by_index(index)`          | Select option by its position (0-based) |
| `deselect_all()`                  | Deselect all options (only for multi-select) |
| `deselect_by_value("value")`      | Deselect option by value |
| `deselect_by_visible_text("text")`| Deselect option by visible text |
| `deselect_by_index(index)`        | Deselect option by index |
| `options`                         | Returns all options (WebElements) |
| `first_selected_option`           | Returns the first selected option |

---

### ⚡ In short:
- **`Select`** = Super handy helper when dealing with dropdowns
- **Without it**, you would need to manually click and select options using complex code.

---

Of course, Edwin! Here’s a neat, clear section you can add to your README about **ActionChains**:

---

# 📜 ActionChains in Selenium

`ActionChains` is a Selenium class that lets you **simulate advanced user interactions** with the browser, like:
- Mouse hover
- Click and hold
- Drag and drop
- Right-click (context click)
- Double-click
- Move to element
- Keyboard actions

It builds a **chain of actions** that are performed **in sequence**, just like a real user would do.

---

## 🛠 Basic Example:

```python
from selenium.webdriver import ActionChains

# Setup driver
driver = webdriver.Chrome()

# Example element
element = driver.find_element(By.ID, "my_element")

# Create action chain object
actions = ActionChains(driver)

# Move to the element and click
actions.move_to_element(element).click().perform()
```

✅ `.perform()` executes the complete action chain.

---

## 🎯 Common Actions:

| **Action** | **Code** |
|------------|----------|
| Move to an element | `actions.move_to_element(element).perform()` |
| Click on an element | `actions.click(element).perform()` |
| Click and hold | `actions.click_and_hold(element).perform()` |
| Release mouse button | `actions.release(element).perform()` |
| Context-click (right-click) | `actions.context_click(element).perform()` |
| Double-click | `actions.double_click(element).perform()` |
| Drag and drop | `actions.drag_and_drop(source, target).perform()` |

---

## 📌 Why use ActionChains?

- To interact with **hover menus** or **hidden elements**.
- To simulate **drag-and-drop**, which normal `.click()` cannot handle.
- To simulate **complex workflows** that require sequences (e.g., hover ➔ click ➔ input text).

---

✅ **Tip:** Always `.perform()` after building your action chain!

---


# 📚 Waits in Selenium

👉 In Selenium, **waits** are used to **pause your script** until a certain condition is met,  
like:  
- Page fully loaded
- Element appears
- Element becomes clickable
- Text appears on page

---

# 🎯 Three Types of Waits

| Type | Use Case | My Opinion |
|:-----|:---------|:-----------|
| **Implicit Wait** | Waits for *any element* to appear | ❗ Lazy way, not recommended for serious scripts |
| **Explicit Wait** | Waits for *specific condition* | ✅ Best way for professional, robust automation |
| **Fluent Wait** | Waits *polling repeatedly* at intervals | 🚀 Great for advanced control, but rarely needed unless website is weird |

---

# 🛠 Quick Example for Each:

## 1. Implicit Wait
> Set once. Selenium waits globally for any find_element calls.

```python
driver.implicitly_wait(10)  # seconds
driver.find_element(By.ID, "some_id")  # waits up to 10 sec
```

✅ Easy, but ❌ not flexible for individual elements.  
(Everything gets the same timeout even if not needed.)

---

## 2. Explicit Wait (⭐ Preferred ⭐)

> Wait until a **specific element** or **specific condition** is true.

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "some_id")))
```

✅ Very clean.  
✅ Only waits where needed.  
✅ Fine-tuned control.

---

## 3. Fluent Wait (Advanced version of Explicit Wait)

> Like Explicit Wait but with **custom polling interval** and **custom exceptions** handling.

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10, poll_frequency=1)  # poll every 1 sec
element = wait.until(EC.element_to_be_clickable((By.ID, "some_id")))
```

✅ Only needed when website is very slow, animated, or has random popups.

---

# ⚡ My Practical Recommendations:

| Task | Which Wait to Use |
|:-----|:------------------|
| Page loading generally | `time.sleep()` (only if rough script) or **wait for specific element** |
| Waiting for buttons, popups, fields | Always **Explicit Wait** |
| Weird dynamic AJAX pages | Fluent Wait if needed |

---

# 📌 Summary

| Type | When to Use |
|-----|-------------|
| `implicitly_wait()` | Only for small projects or demos |
| `WebDriverWait + EC` | Always for production quality |
| `Fluent Wait` | Only for rare "keep checking every few seconds" needs |

---

✅ **Golden Rule:**  
**Use explicit waits unless you have a very strong reason not to.**

---

