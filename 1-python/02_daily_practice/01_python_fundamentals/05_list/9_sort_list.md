# sort()
---

sort() organizes the items inside the existing list.

What it is?
It is a list method used to sort a list in ascending order by default.

What problem it solves?
It is useful when a requirement asks you to organize data into a meaningful order, such as:
“Show the lowest price first.”
or: “Rank the results from highest to lowest.”

When I would recognize the need for it
Lowest → highest
Highest → lowest
Alphabetical order
Ranking
Ordered results
Comparing data in an organized order

---

# Important Rule — sort() + sorted()
Type: sort() is a list method; sorted() is a built-in function
Call on: sort() → list; sorted() → accepts many sortable iterables
Input: optional sorting options such as reverse and key
Syntax: my_list.sort() / sorted(iterable)
Purpose: organizes items into sorted order
Default order: ascending
Changes: sort() changes the original list; sorted() does not
Returns: sort() returns None; sorted() returns a new list
Order: changes the order according to the sorting rule
Duplicates: preserved
Important warning: don't use sort() when you need to preserve the original list
reverse=True: can make sorting descending
reverse() difference: reverse() flips the current order; it does not sort
Best use: sort() when changing the existing list is intended; sorted() when the original order must remain available
Mental model: “Sort organizes; sorted() gives me a new organized version.”