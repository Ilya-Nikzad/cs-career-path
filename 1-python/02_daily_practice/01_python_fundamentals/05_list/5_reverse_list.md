### reverse()
---

What it is
reverse() changes the order of a list so the elements appear in the opposite order.

What problem it solves
It solves situations where you need to reverse the existing order of a list.

When would I recognize the need for it?
Think of reverse() when a requirement says things like:
“Show the most recent item first.”


Important rule
reverse() is specifically a method for Python lists.
reverse() changes the original list.

---

# Important Rule — `reverse()`

- **Type:** list method
- **Call on:** list only
- **Input:** none
- **Syntax:** `my_list.reverse()`
- **Purpose:** reverses the order of the list
- **Changes:** original list
- **Returns:** `None`
- **Important:** it does not sort the list
- **Example idea:** `[1, 2, 3]` → `[3, 2, 1]`
- **Common mistake:** expecting it to return the reversed list
- **Mental model:** **“Flip the current order.”**