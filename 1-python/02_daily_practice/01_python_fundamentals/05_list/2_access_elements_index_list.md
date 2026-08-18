###  Accessing Elements & Indexing 
---

A list can contain many values, but often you need to work with one particular value.
Python uses indexes to identify positions.
Simple explanation:
Positive index — counts from the start (left), beginning at 0
Negative index — counts from the end (right), beginning at -1
Why use negative? Easy way to get last items without knowing the list's length.

---

# Important Rule — Accessing Elements

- **Type:** list/string/sequence operation
- **Purpose:** gets a specific item from a collection
- **Syntax:** `collection[index]`
- **Works with:** subscriptable objects such as lists, strings, and tuples
- **Indexing starts:** `0`
- **Negative index:** `-1` means the last item
- **Changes original:** no
- **Returns:** the accessed item
- **Common mistake:** using an invalid index → `IndexError`
- **Mental model:** **“Use `[position]` to get an item.”**