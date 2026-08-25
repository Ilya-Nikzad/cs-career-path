# Insert()

---

What it is?

insert() adds one item at a specific position in a list.  
Like: insert(1, "review notes")

What problem it solves?

Adding an item while controlling where it appears in the list.

When would I recognize the need for it?

When a requirement says something like:  
A new item belongs before another item.  
A new item needs a specific position.  
The order of the list matters, and the new item shouldn't simply go at the end.

Important rules

If you insert at an existing index, the existing items don't get replaced—they move to make room.

---

# Important Rule — `insert()`

- **Type:** list method
- **Call on:** list only
- **Input:** index + one item
- **Syntax:** `my_list.insert(index, item)`
- **Purpose:** adds one item at a specific position
- **Changes:** original list
- **Returns:** `None`
- **Order:** existing items shift to the right
- **Duplicates:** allowed
- **Important:** if the index is beyond the list, Python places the item at the end
- **Mental model:** **“Put this one item at this position.”**
- list[0:0] = iterable inserts all iterable items at the front, without removing existing items.