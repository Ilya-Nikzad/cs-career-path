# Task : Read the file line by line, split each line into words,
# and add only new (non-duplicate) words to a list.
# After collecting all unique words, sort the list alphabetically and print it.

#BEGIN PROGRAM
# Step 1: Prompt the file name
file_name = input("Enter file name: ")

# Step 2: Open file using file handle
file_handle = open(file_name)

# Step 3: Initialize a list to store unique words
words_list = []

# Step 4: Loop through each line in the file
for line in file_handle:

    # (optional cleanup) remove extra spaces/newlines
    line = line.strip()

    # Step 5: Split line into words
    for word in line.split():

        # Step 6: Check if word is NOT already in the list (no duplicates)
        if word not in words_list:
            words_list.append(word)

# Step 7: Sort the words alphabetically
sorted_words_list = sorted(words_list)

# Step 8: Output result
print(sorted_words_list)
#END PROGRAM