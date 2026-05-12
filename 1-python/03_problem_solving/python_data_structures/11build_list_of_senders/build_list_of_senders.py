#Read the file line by line, If a line starts with "From " (not "From:"),
# split it into words, print the second word (email),
# and count how many matching lines there are. Print the total count at the end.

#BEGIN PROGRAM
# Step 1: Ask the user for the file name
file_name = input("Enter file name: ")

# Step 2: Open the file
file_handle = open(file_name)

# Step 3: Create a counter variable
counter = 0

# Step 4: Read the file line by line
for line in file_handle:

    # Step 5: Check if the line starts with "From "
    if line.startswith("From "):

        # Step 6: Split the line into words
        words = line.split()

        # Step 7: Get the second word (email)
        sender = words[1]

        # Step 8: Print the email
        print(sender)

        # Step 9: Increase the counter
        counter += 1

# Step 10: Print the total count
print(f"There were {counter} lines in the file with From as the first word")
#END PROGRAM
