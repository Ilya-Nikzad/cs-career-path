#BEGIN PROGRAM
# Step 1: Prompt user to enter text
text = input("Enter a string: ")
# Step 2: Create empty variables
uppercase = ""
lowercase = ""
length = 0
# Step 3: Look at each character in the sentence once
for char in text:
    # Step 4: For each character: add lower,upper and increase length by 1
    uppercase += char.upper()
    lowercase += char.lower()
    length += 1
# Step 5: Output result
print(f"Uppercase characters: {uppercase}")
print(f"Lowercase characters: {lowercase}")
print(f"Length: {length}")
#END PROGRAM



#BEGIN PROGRAM
# Step 1: Take input sentence
sentence = input("Enter a sentence: ")

# Step 2: Convert to uppercase
upper_sentence = sentence.upper()

# Step 3: Convert to lowercase
lower_sentence = sentence.lower()

# Step 4: Find length
length = len(sentence)

# Step 6: Display results
print("Uppercase:", upper_sentence)
print("Lowercase:", lower_sentence)
print("Length:", length)
#END PROGRAM

