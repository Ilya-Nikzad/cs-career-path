# pop()
---
pop() removes an item from a list and returns the removed item.

What it is
It is a list method used when you want to remove an item by its position.

What problem it solves
It is useful when an item needs to leave a list and you may need to use the removed item afterward.

When I would recognize the need for it
Look for requirements involving:
Removing something by position
Taking an item out of a list
Removing an item and using the removed value
Taking the last item from a list

---

# Important Rule `pop()`
Type: list method
Call on: list
Input: optional index
Syntax: my_list.pop() or my_list.pop(index)
Purpose: removes and returns one item
Default: no index → removes the last item
Changes: original list
Returns: the removed item
Index: supports positive and negative indexes
Order: remaining items keep their relative order
Duplicates: removes only the item at the selected index
Important warning: invalid indexes and popping from an empty list raise IndexError
remove() difference: remove(value) removes by value; pop(index) removes by position
Indexing difference: items[index] only accesses; pop(index) accesses and removes
Best use: when you need to remove an item by position and possibly use the removed value
Mental model: “Take this item out and give it back.”