# Q7: Print each character in the string "Python" one by one

text_1 = "python"

for char in text_1:
    print(char)



# Q9: Count how many times the letter "a" appears in the string

text = "banana"
count = 0

for char in text:
    if char == "a":
        count += 1

print("Count of 'a':", count)




# Q11: Check if the letter "p" exists in the string

text = "python"

if "p" in text:
    print("Found")
else:
    print("Not found")