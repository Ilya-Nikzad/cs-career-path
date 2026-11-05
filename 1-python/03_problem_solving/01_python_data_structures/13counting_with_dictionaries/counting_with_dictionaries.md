# Counting with Dictionaries

## What is a Histogram?

A histogram in programming is a way to count how many times each item appears in a dataset.

Instead of drawing bars like in math class, we store counts using a dictionary.

- Each key = an item (like a name or word)
- Each value = how many times it appears

A histogram = automatic counting system using dictionaries

Histogram building = repeat: check → add or initialize → update count

---

## Q1: What is a histogram in Python (in simple term)

Histogram is a dictionary that stores counts of items automatically.

---

## Q2: What does each key and each value represent in a histogram dictionary?

- Key is the item
- Value is the count of how many times it appears

---

## Q3: In a histogram, what happens when you see an item for the first time?

Create it in the dictionary and set its count to 1.

---

## Q4: What happens when we see an item that is already in the histogram?

We increase its current count by 1.

---

# How to Think About Histograms

When solving histogram problems, always follow this mental flow:

```text
Look at item
Ask: have I seen it before?

If NO  → start count at 1
If YES → add 1 to existing value

Store updated value back in dictionary
```

---

# SUMMARY

## 🧠 What you learned

- Histogram = dictionary of counts
- Key = item (word, name, etc.)
- Value = number of occurrences
- First time → initialize to 1
- Repeated → increment by 1
- `.get(key, 0)` simplifies counting logic

---

## ⚡ What to remember

- “First time = 0 + 1”
- “Next times = +1 again”
- `