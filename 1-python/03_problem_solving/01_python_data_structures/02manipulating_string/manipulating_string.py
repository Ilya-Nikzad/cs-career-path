#BEGIN PROGRAM
#Task 1: Checks if the word "python" exists inside this text handling the case-sensitive

# Step 1: Declare variable
first_text = "I love learning Python programming"
# Step 2: Condition check
if "python" in first_text.lower():
    print("Found python in the text")
else:
    print("Python not found in the text")

#END PROGRAM


#BEGIN PROGRAM
# Task 2: Replace "Python" with "Java" in a given string

# Step 1: Define the original text
sec_text = "I love Python programming"

# Step 2: Use .replace() to create a new string with "Python" replaced by "Java"
jav_changed = sec_text.replace("Python", "java")

# Step 3: Print the updated text
print(jav_changed)

#END PROGRAM


#BEGIN PROGRAM
#Task 3: Output check
text = "  Python Programming  "
result = text.strip().lower().replace("python", "java")
print(result)
#END PROGRAM


#BEFIN PROGRAM
text = "Data Science"
print(text.find("Sci"))
#END PROGRAM

