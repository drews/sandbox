# 🧭 Python Control Flow + Keywords in Context

> Theme: "Code that Decides, Repeats, and Responds"
> Audience: New Python learners (1-hour focused session)

---

## 🎯 Overview

Python’s **control flow** is how your program decides *what to do next*. In this guide, you’ll:

* Explore **decision-making**, **loops**, and **error handling**
* See **keywords** in context — the real building blocks of Python logic
* Learn through small examples and linked references

All documentation links point to **Python 3.12**, ensuring accuracy.

---

## 🔡 The Core Control Keywords

### 1. `if`, `elif`, `else`

**Purpose:** Make decisions based on conditions.

```python
x = 7

if x > 10:
    print("Big number!")
elif x > 5:
    print("Medium number!")
else:
    print("Small number!")
```

📘 Docs: [If Statements](https://docs.python.org/3.12/tutorial/controlflow.html#if-statements)

---

### 2. `for`, `while`, `break`, `continue`, `pass`

**Purpose:** Repeat actions until a condition changes.

```python
for i in range(5):
    if i == 2:
        continue  # skip this round
    if i == 4:
        break      # stop loop early
    print(i)

while True:
    cmd = input("Type 'exit' to stop: ")
    if cmd == 'exit':
        break
    pass  # placeholder for future logic
```

📘 Docs: [For Statements](https://docs.python.org/3.12/tutorial/controlflow.html#for-statements)

---

### 3. `def`, `return`

**Purpose:** Group logic into reusable functions.

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Ada"))
```

📘 Docs: [Defining Functions](https://docs.python.org/3.12/tutorial/controlflow.html#defining-functions)

---

### 4. `try`, `except`, `raise`, `finally`

**Purpose:** Handle (or raise) errors gracefully.

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Can't divide by zero!")
    finally:
        print("Division attempt complete.")

result = divide(10, 0)
```

📘 Docs: [Errors and Exceptions](https://docs.python.org/3.12/tutorial/errors.html)

---

### 5. `import`, `from`, `as`

**Purpose:** Bring in external code or modules.

```python
import math
from random import choice as pick

print(math.sqrt(16))
print(pick(['apple', 'banana', 'cherry']))
```

📘 Docs: [Modules](https://docs.python.org/3.12/tutorial/modules.html)

---

### 6. `with`

**Purpose:** Simplify resource management (like opening files).

```python
with open('notes.txt', 'w') as f:
    f.write('Python keywords rock!')
```

📘 Docs: [The with Statement](https://docs.python.org/3.12/reference/compound_stmts.html#the-with-statement)

---

### 7. `global`, `nonlocal`

**Purpose:** Control variable *scope*.

```python
count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # 1
```

📘 Docs: [Scopes and Namespaces](https://docs.python.org/3.12/tutorial/classes.html#python-scopes-and-namespaces)

---

### 8. `class`, `yield`, `lambda`

**Purpose:** Advanced control of data and flow.

```python
class Counter:
    def __init__(self):
        self.value = 0
    def tick(self):
        self.value += 1

# Generators
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Lambda
square = lambda x: x * x
```

📘 Docs:

* [Classes](https://docs.python.org/3.12/tutorial/classes.html)
* [Generators](https://docs.python.org/3.12/tutorial/classes.html#iterators)
* [Lambda Expressions](https://docs.python.org/3.12/tutorial/controlflow.html#lambda-expressions)

---

## 🧠 Practice Challenge

Write a short program that:

1. Imports `random`
2. Loops 5 times, generating a number each time
3. Uses `if/elif/else` to print a reaction based on the number
4. Wraps this in a `try/except` block to handle user interrupts

---

## 🪄 Reflection

* Which keywords shape *decision-making*? (hint: `if`, `elif`, `else`)
* Which shape *repetition*? (hint: `for`, `while`)
* Which shape *structure*? (hint: `def`, `class`, `import`)

Once you can *read* and *apply* these, you’ve unlocked Python’s inner rhythm — control, flow, and scope working in harmony.

---

**Next Iteration Ideas:**

* Add visual flow diagrams
* Include interactive examples (Jupyter or REPL style)
* Provide keyword grouping by behavior (decision / iteration / error / structure)
