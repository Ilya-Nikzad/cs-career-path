# `Looping Through Lists + in`
---

These two concepts work naturally together
when you need to inspect every item in a list and check whether a particular value exists.

Looping Through Lists: Repeating an action for each item in a list.
It lets you process every element one by one.

in: Checks whether a value exists inside a list (or other collection).
It returns True if the value is found and False if it isn’t.

---

# Important Rule — Looping Through Lists + in

Looping: for item in my_list: processes items one at a time
in: membership operator
in purpose: checks whether a value exists in a collection
in returns: True or False
Syntax: value in my_list
Loop order: follows the list's existing order
Changes: neither a normal loop nor in changes the list by itself
Duplicates: a loop processes duplicate items; in only answers whether a match exists
count() difference: count() asks “HOW MANY?”; in asks “IS IT THERE?”
Important warning: in checks membership, not position
Best use: when a requirement says to check whether something exists or compare items against another collection
Mental model: Loop = “check each item.” in = “is this value there?”

