# List 
---

### Step 1: Foundation

Definition: A list is a way to keep multiple values together in one ordered collection.

What problem does it solve?
Instead of storing related data separately we can store together in specific order 

When would you recognize the need for a list?
I have multiple things of the same general kind, and I need to keep track of them.
A list can also change while your program is running: items can be added, removed, or replaced.

# Important Rule — `list`

- **Type:** built-in collection/data type
- **Purpose:** stores multiple items in one ordered collection
- **Syntax:** `my_list = [item1, item2, item3]`
- **Can contain:** numbers, strings, booleans, other lists, and mixed types
- **Order:** preserved
- **Indexing:** starts at `0`
- **Duplicates:** allowed
- **Mutable:** can be changed after creation
- **Access:** `my_list[index]`
- **Slicing:** `my_list[start:stop]`
- **Common methods:** `append()`, `insert()`, `extend()`, `reverse()`
- **Common mistake:** confusing a list with a single item
- **Mental model:** **“A list is an ordered, changeable container that holds multiple items.”**

---
# Important Rule — Indexing

- **Type:** sequence operation
- **Purpose:** accesses one specific item
- **Syntax:** `sequence[index]`
- **Works with:** subscriptable objects such as lists, strings, and tuples
- **First index:** `0`
- **Last index:** `-1`
- **Changes original:** no
- **Returns:** one item
- **Common mistake:** accessing an index that doesn't exist
- **Mental model:** **“Index = the item's position.”**

---

# Important Rule — Slicing

- **Type:** sequence operation
- **Purpose:** gets a range of items
- **Syntax:** `sequence[start:stop:step]`
- **Works with:** subscriptable sequences such as lists, strings, and tuples
- **Start:** included
- **Stop:** excluded
- **Step:** controls how items are selected
- **Changes original:** usually no
- **Returns:** a new sliced sequence
- **Common mistake:** forgetting that `stop` is excluded
- **Mental model:** **“Start here, stop before there.”**