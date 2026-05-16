# Tuples in Python

## 1. What is a Tuple?
A tuple is very similar to a list.

**Main difference:**
- List → mutable (can change)  
- Tuple → immutable (cannot change)

Tuples are basically: **“read-only lists”**

**Notice:**
- Lists use `[]`  
- Tuples use `()`

**Tuples still support:**
- indexing  
- loops  
- `max()`  
- sequences  

**Key Idea:**  
Tuple = ordered sequence like a list, but cannot be modified after creation  

---

## 2. Immutable
This is the most important tuple concept.

**Immutable means:**  
Cannot be changed after creation  

---

## 3. Tuple Assignment (Unpacking)
Tuples can assign multiple variables at once.

This is called:
- tuple assignment  
- unpacking  

Tuple unpacking assigns multiple variables in one step  

---

## 4. `.items()` + Tuple Unpacking in Loops
Dictionaries store data as key → value pairs.

`.items()`:
- returns each item as a tuple (key, value)

Then we loop through and unpack them into key and value.

---

## Q1: What is a tuple in Python?
A tuple is an ordered, immutable collection of values.

---

## Q2: What is the difference between a list and a tuple?
- A list is mutable (can be changed)  
- A tuple is immutable (cannot be changed)  

---

## What does `.items()` do?
It returns each dictionary entry as a tuple (key, value), which can be unpacked into separate variables.

---

## Summary
- Tuples = immutable ordered collections  
- Lists = mutable, tuples = not changeable  
- `.items()` gives (key, value) tuples  
- Tuple unpacking splits them automatically  
- Useful for looping through dictionaries  
- Helpful for tracking values like maximums  