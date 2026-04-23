📘 Python Dictionary Notes
🔹 What is a Dictionary?

A dictionary is a collection of named values that store data in key–value pairs.

Example:
"name" → key
"Ali" → value

🔹 Basic Operations
📌 Access Values

Used to get a value using its key.

person["name"]

📌 Add New Value

Used to insert a new key–value pair.

person["job"] = "Student"

📌 Remove Value

Used to delete a key–value pair.

del person["city"]

📌 Loop Through Dictionary
Loop through values:
person.values()
Loop through key–value pairs:
person.items()
📘 Most Important Dictionary Methods (Python)
🔹 Get value safely

Used to get a value from a key without causing an error if the key doesn’t exist.
If the key is missing, it returns None or a default value.

person.get("name")
person.get("name", "Not Found")

🔹 Get all keys

Returns all the keys in the dictionary.

person.keys()

🔹 Get all values

Returns all the values in the dictionary.

person.values()

🔹 Get key–value pairs

Returns all items as (key, value) pairs.

person.items()