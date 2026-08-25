# `11_enumerate_list`

---

enumerate() lets you loop through an iterable while getting both the item and,  
its position at the same time.

What problem it solves

Loop through these items and also show their position/number

When I would recognize the need for it

Display each item's position  
Number a list of results  
Show rankings  
Add a row/item number while looping  
Use both the item and its index during a loop

---

# Important Rule — enumerate()

Type: built-in function  
Call on: an iterable such as a list, tuple, or string  
Input: iterable, optional start value  
Syntax: enumerate(iterable, start=0)  
Purpose: provides each item together with its counting position  
Changes: does not change the original iterable  
Returns: an enumerate iterator  
Default position: starts at 0  
start=: changes the first position number  
Order: follows the iterable's existing iteration order  
Important warning: the position from enumerate() is not automatically the same as a custom ranking or value inside the data  
Looping difference: for item in items gives only the item; enumerate(items) gives the position and item  
Best use: when a loop needs both an item's position and its value  
Mental model: “Give me the item and its number together.”