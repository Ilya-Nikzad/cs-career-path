person = {
    "name": "Hanna",
    "age": 20,
    "city": "New York",
}
#It controls what goes between values. Default: sep=" " space,sep="" nothing,sep="-" → dash
print("name:", person["name"], "\nage:", person["age"], "\ncity:", person["city"], sep="")

#Access value:
print(person["name"])
#Remove Value:
del person["city"]
# Add value:
person["city"] = "New York"

person = {
    "name": "Hanna",
    "age": 20,
    "city": "New York",
}

# 1: Loop for keys only
print("KEYS:")
for key in person:
    print(key)

print()

# 2: Loop for values only
print("VALUES:")
for value in person.values():
    print(value)

print()

# 3: Loop for both key and value
print("KEY-VALUES:")
for key, value in person.items():
    print(f"{key}:{value}")


#BEGIN PROGRAM
# Step 1: Initialize the dictionary with student information
student_info = {
    "id": "235323",  # Student ID
    "full_name": "Hanna",  # Student full name
    "age": 21,  # Student age
    "grade": "100A",  # Student grade
    "marks": {"Python": 85, "Data Structure": 90, "Algorithm": 78},  # Subject marks
    "subjects": ["Math", "Science", "English"]  # List of subjects
}

# Step 2: Loop through each key-value pair in the dictionary
for key, value in student_info.items():

    #Step 3: Check if the value is a dictionary
    if isinstance(value, dict):
        # Print the dictionary key
        print(f"{key}:", end='')

        # Step 4: Loop through nested dictionary items
        for sub_key, sub_value in value.items():
            # Print nested key-value pairs
            print(f"{sub_key}: {sub_value},", end="")
            # Move to the next line
            print()

    # Check if the value is a list
    elif isinstance(value, list):
        # Print the list key
        print(f"{key}:", end='')
        # Print list elements separated by commas
        print(*value, sep=",")

    # For normal values (string, int, etc.)
    else:
        # Print key and value directly
        print(f"{key}:{value}")
#END PROGRAM