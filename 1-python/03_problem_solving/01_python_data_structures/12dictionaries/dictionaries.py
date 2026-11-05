# Task 1: Create and Update a Dictionary
student = {
    "name":"Hanna",
    "age": 21,
    "grade":"B"
}
student["age"] = student["age"] + 1
student["grade"] = "A"
student["school"] = "Michigan"
print(student)


# Task 2: Use .get() to access dictionary values, update existing values,
# and add a new key only if it doesn’t already exist.
# Print the number of bananas using .get().
# Try to print the number of grapes using .get() (what happens if it doesn’t exist?)
# Add 3 apples to the inventory (update the value, don’t replace it).
# If "grapes" is NOT in the dictionary, add it with value 12.
# Print the final dictionary.

inventory = {
    "apples": 10,
    "bananas": 5,
    "oranges": 8
}
inventory.get("oranges")
if not "grapes" in inventory:
    inventory["grapes"] = 12
inventory["apples"] = inventory["apples"] + 3
print(inventory)
