# Task : Finding Numbers in a Haystack using regex
# In this assignment you will read through and parse a file with text and numbers.
# You will extract all the numbers in the file and compute the sum of the numbers.
#BEGIN
import re
file_name = "regex_sum_2362198.txt "
file_handle = open(file_name)
total = 0
for line in file_handle:
    digit = re.findall("[0-9]+", line)
    for number in digit:
        number = int(number)
        total += number
print(total)
#END

#Here is the list comprehension version of your code:
import re

file_name = "regex_sum_2362198.txt"
file_handle = open(file_name)

total = sum([int(x) for x in re.findall("[0-9]+", file_handle.read())])

print(total)