# Task 1: Find all numbers: using findall
#BEGIN
import re
text = "I have 3 dogs, 12 cats and 100 birds"
# find all numbers in the text
numbers = re.findall(r"[0-9]+", text)
print(numbers)
#END


# Task 2: Greedy Matching
#BEGIN
import re
x = "From: stephen.marquard@uct.ac.za, from: test@mail.com"
result = re.findall(r"^F.+:", x)
print(result)
#END


# Task 3: Non-Greedy Matching — How to stop the greediness
import re
x = "From: stephen.marquard@uct.ac.za, from: test@mail.com"
result = re.findall(r"^F.+?:", x)
print(result)
#END



# Task 4: Using Parentheses to Extract Only What You Want
import re
x = "From: stephen.marquard@uct.ac.za, from: test@mail.com"
result = re.findall(r"\S+@(\S+)", x)
print(result)
#END


# Task 5: Using Backslash to Match Special Characters
#BEGIN
import re
x = "We charge $19.99 for the item"
result = re.findall(r"\$[0-9.]+", x)
print(result)
#END


# Task 6: This code is supposed to extract all uppercase vowels from a string
#BEGIN
import re
text = "Hello AEIOU World"
result = re.findall('[AEIOU]+', text)
print(result)
#END


#Task 7: Write a program that:
# Opens a file called mbox.txt
# Reads through each line
# Extracts the confidence number from lines that start with X-DSPAM-Confidence:
# Prints each number found
#BEGIN
import re
file_name = "mbox.txt"
f_handle = open(file_name)
for line in f_handle:
    result = re.findall(r'X-DSPAM-Confidence: ([0-9].+)', line)
    if len(result) == 1:
        print(result[0])
#END


# Task 8: Write a program that:
# Loops through each line
# Extracts only the price number — without the $ sign
# Skips lines that don't have a price
# Prints each price found
#Begin
import re

data = [
    "Price: $29.99 for headphones",
    "Price: $149.50 for keyboard",
    "Discount: 10% off today",
    "Price: $9.99 for cable"
]

for line in data:
    result = re.findall(r'^Price: \$([0-9.]+)', line)
    if len(result) == 1:
        print(result[0])
#END
