## **Step 1: Python Data Types & Basic Operations**

We'll cover:
- `int`, `float`, `str`, `bool`
- `list`, `tuple`, `dict`, `set`
- Type casting
- Basic operations with these types

---

### **A. Numbers & Strings**
```python
x = 10            # int
y = 3.5           # float
name = "Edwin"    # str
is_valid = True   # bool

# String operations
print(name.upper())        # "EDWIN"
print(name[1:4])           # "dwi"
print("win" in name)       # True
```

---

### **B. Lists**
```python
fruits = ["apple", "banana", "cherry"]

fruits.append("orange")        # Add
fruits[1] = "grape"            # Update
print(fruits[0])               # Access
fruits.remove("apple")         # Remove
print(len(fruits))             # Length
fruits.remove("banana")  # Removes "banana" #❗ If the value is not found → ValueError
last = fruits.pop()
print(last)     # 'cherry'
item = fruits.pop(1)
print(item)     # 'banana' #Index out of range → IndexError

```

---

### **C. Tuples**
```python
point = (3, 4)
x, y = point       # Tuple unpacking
print(x + y)       # 7
```
> Tuples are immutable, so they’re safer for constant data.

---

### **D. Dictionaries**
```python
student = {"name": "Edwin", "age": 25}

print(student["name"])          # Access
student["age"] = 26             # Update
student["city"] = "Canberra"    # Add
print(student.get("grade", "N/A"))  # Safe get

del student["age"]             # Deletes key 'age'
student.pop("city")            # Removes and returns value
student.clear()                # Removes all items (dict becomes empty)

student.keys()     # dict_keys(['name'])
student.values()   # dict_values(['Edwin'])
student.items()    # dict_items([('name', 'Edwin')])

for key, value in student.items():
    print(key, value)

```

---

### **E. Sets**
```python
unique_vals = {1, 2, 3, 3, 2}
print(unique_vals)         # {1, 2, 3}

unique_vals.add(5)
s.update(["orange", "grape"])  # Add multiple

s.pop()               # Removes random item
s.clear()             # Empties the set

unique_vals.discard(2)
print(3 in unique_vals)    # True

a = {1, 2, 3}
b = {3, 4, 5}

a.union(b)            # {1, 2, 3, 4, 5}
a.intersection(b)     # {3}
a.difference(b)       # {1, 2}
a.symmetric_difference(b)  # {1, 2, 4, 5}

```

---

### **F. Type Casting**
```python
s = "123"
num = int(s)         # 123
f = float("3.14")    # 3.14
s2 = str(456)        # "456"
```

---

**Mini Task for You:**  
Write a Python script that:
1. Takes a string from the user.
2. Converts it to uppercase.
3. Adds it to a list.
4. Checks if "HELLO" is in the list.
