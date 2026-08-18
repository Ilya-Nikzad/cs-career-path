### extend 
---

What it is
extend() adds multiple items from another iterable to the end of a list.

What problem it solves
It is useful when you already have a list and need to add several items from another collection.

When I would recognize the need for it

When a requirement says:
Add all the new items to the existing list.

Important rule
extend() changes the original list.

---

# Important Rule — `extend()`

- **Type:** list method
- **Call on:** list only
- **Input:** any iterable (list, tuple, string, set, etc.)
- **Syntax:** `my_list.extend(iterable)`
- **Purpose:** adds items individually to the list
- **Changes:** original list
- **Returns:** `None`
- **Order:** preserves item order
- **Duplicates:** does not remove duplicates
- **String warning:** `"cat"` → `"c"`, `"a"`, `"t"`
- **`append()` difference:** `append()` adds the whole object as one item
- **`+` difference:** `+` creates a new list; `extend()` changes the existing list
- **Best use:** when you need to add all items from another iterable
- **Mental model:** **“Take these items and add them individually.”**