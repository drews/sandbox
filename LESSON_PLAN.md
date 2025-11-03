# 🕒 One-Hour Python: Control, Flow, and Scope

> Theme: **“Thinking in Motion — How Code Decides, Repeats, and Remembers”**  
> Audience: Complete beginners  
> Time: ~60 minutes total

---

## 🧩 0–15 min — Variables and Scope

**Goal:** Understand how Python stores and shares information.

**Key Concepts:**
- Variables: names that store values  
- Functions: blocks that do something  
- Scope: where variables “live” and who can see them  

**Mini Challenge:**  
Write a function that changes a player’s health.  
```python
health = 100

def take_damage(amount):
    global health
    health -= amount
    print("Health now:", health)

take_damage(10)
