#BEGIN PROGRAM
# Step 1: Open the markdown file
file_handle = open("processing_file.md", encoding="utf-8")  # If the file can't be found, use the full file path
# Step 2: Loop through each line in the file
for line in file_handle:
    # Step 3: Output result
    print(line)
#END PROGRAM


#BEGIN PROGRAM
# Step 1: Open the markdown file
file_handle = open("processing_file.md", encoding="utf-8")

# Step 2: Initialize a counter to count number of lines
count = 0

# Step 3: Loop through each line in the file
for line in file_handle:
    # Step 4: Increment counter for each line
    count += 1

# Step 5: Print total number of lines in the file
print(count)
#END PROGRAM


#BEGIN PROGRAM
# Step 1: Open the file in read mode
file_handle = open("processing_file.md", encoding="utf-8")

# Step 2: Use read() to read and print the entire file content
print(file_handle.read())

# Step 3: Use close() to close the file
file_handle.close()
# END PROGRAM


#BEGIN PROGRAM
# Step 1: Open the file in read mode
file_handle = open("processing_file.md", encoding="utf-8")
# Step 2: Set the target word to search
target_word = "Q1"
# Step 3: Read the file line by line using a loop
for line in file_handle:
    # Step 4: For each line, check if the target word is present
    if target_word in line:
        # Step 5: If found, display “Word found” and stop the loop
        print("Word found")
        break
# Step 6: If the loop ends without finding the word, display “Word not found”
else:
    print("Word not found")
# Step 7: Close the file
file_handle.close()
# END PROGRAM


# BEGIN PROGRAM
# Step 1: Open the file in read mode with UTF-8 encoding
file_handle = open("processing_file.md", encoding="utf-8")
# Step 2: Read the file line by line using a loop
for line in file_handle:
    # Step 3: Check if the line starts with "#"
    if line.startswith("#"):
        # Step 4: If it is a comment line, skip it completely
        continue
    # Step 5: Otherwise, print the line without extra spaces/newline
    print(line.strip())
# Step 6: Close the file after processing
file_handle.close()
# END PROGRAM


# BEGIN PROGRAM
# Step 1: Ask the user to enter a file name
file_name = "processing_file.md"
# Step 2: Try to open the file
try:
    file_handle = open(file_name, encoding="utf-8")
    # Step 3: If successful, confirm the file is opened
    print("File opened successfully")
# Step 4: If an error occurs
except:
    print("File not found")
# END PROGRAM