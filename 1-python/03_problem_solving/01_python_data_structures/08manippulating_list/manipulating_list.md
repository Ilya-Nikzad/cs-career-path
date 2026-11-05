# 📘 PDS: Manipulating Lists

A **list in Python** is like a container that holds multiple values in order.

---

## 1. Combining Lists (Concatenation)

You can combine two lists using `+`.

---

## 2. Slicing Lists

Slicing means taking a part of a list.
**Format:** list[start:end]

**Rules:**

* Start is **included**
* End is **NOT included**

---

## 3. List Methods (Built-in Actions)

### Common Methods:

* append() → add item at end
* count() → count occurrences
* len() → total number of items
* extend() → add multiple items
* index() → find position
* insert() → add at specific position
* pop() → remove last/specific item
* remove() → remove by value

---

## ⚠️ Important Nuance

* append() adds an **entire list as ONE element** → creates a nested list
* extend() adds **each element individually**
* append() → adds ONE item (even if it’s a list)
* extend() → adds multiple items from another list

---

## 🧠 Key Concepts

* Lists are **mutable** → they can be changed directly
* sort() modifies the original list
* in checks existence
* Slicing → start included, end excluded
