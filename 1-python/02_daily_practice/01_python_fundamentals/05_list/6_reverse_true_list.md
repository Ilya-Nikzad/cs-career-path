### reverse=True
___

What it is
reverse=True tells a sorting operation to arrange items in descending order.

What problem it solves
It is useful when you need data sorted from largest/highest → smallest/lowest or Z → A.

When I would recognize the need for it
When a requirement says:
Highest first
Newest first, when sorting by a sortable value
Largest to smallest
Descending order
Z to A

Think:
sort() = organize
reverse=True = organize in the opposite direction

Important rule
reverse=True is an argument to sorting. It is different from reverse()

---

# Important Rule — `reverse=True`

- **Type:** keyword argument
- **Purpose:** tells certain functions/methods to use reverse order
- **Common use:** `sorted(..., reverse=True)`
- **Syntax:** `function(..., reverse=True)`
- **Important:** `reverse=True` is not a method
- **Important:** it does not mean “sort”; it only controls the direction/order
- **`True`:** reverse order
- **`False`:** normal/default order
- **Changes original:** depends on the function being used
- **Mental model:** **“Do it in reverse order.”**