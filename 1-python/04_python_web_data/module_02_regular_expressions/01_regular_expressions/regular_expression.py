# Task 1: Find if cat exists in the text.
#BEGIN
# Step 1: Store text in variable
text = "I have a cat and a dog."
# Step 2: Check the conditions
if "cat" in text:
    print("Found")
else:
    print("Not Found")
#END

# Using Regular expression
#BEGIN
# Step 1: Import Library re
import re

# Step 2: Store text in variable
text = "I have a cat and a dog."

# Step 3: Using search function in condition
if re.search(r"c.t", text):
    print("Found")
else:
    print("Not found")
#END




# Task 2: Find and extract all numbers from a string

# Step 1: Initialize the text string
text = "I have 2 apples and 15 oranges."

# Step 2: Create an empty list to store extracted numbers
# and a temporary string to build multi-digit numbers
numbers = []
current = ""

# Step 3: Loop through each character in the text
for cha in text:
    if cha.isdigit():
        # If the character is a digit, add it to the current number
        current += cha
    else:
        # If a non-digit is found, save the completed number (if any)
        if current != "":
            numbers.append(current)
        current = ""  # reset for the next number

# Step 4: Append the last number if the string ends with a digit
if current != "":
    numbers.append(current)

print(numbers)
# END of manual method

# Using regular expressions method now
#BEGIN
import re

text = "I have 2 apples and 15 oranges."

# Extract all sequences of digits using regex
numbers = re.findall("\d+", text)
print(numbers)
#END



# Task 3: Find emails.

# Step 1: The input work on it
text = "Contact me at ali@gmail.com and test@yahoo.com"
parts = text.split()
for word in parts:
    if "@" in word:
        print(word)

# Using regular expressions method now
import re

text = "Contact me at ali@gmail.com and test@yahoo.com"
emails = re.findall(r"\S+@\S+", text)
for email in emails:
    print(email)


# Task 4: Read mbox-short.txt and print only the lines that start with From using the regex

# BEGIN
file = "mbox-short.txt"
f_handle = open(file)

# FOR EACH line IN file
for line in f_handle:

    # IF line STARTS WITH "From "
    if line.startswith("From "):
        print(line.rstrip())
# END FOR
# END


#Using the regular expressions method with the caret (^)
import re

file = "mbox-short.txt"
f_handle = open(file)

# LOOP through each line in the file
for line in f_handle:

    # CHECK: does the line start with "From "?
    if re.search("^From ", line):

        # OUTPUT cleaned line
        print(line.rstrip())

# FINISH: close file
f_handle.close()
#END


# Task 5: Grab everything and print it
#BEGIN
import re
line = "Xray is cool 123 !@#"
result = re.search("^X.*", line)
print(result.group())
#END

