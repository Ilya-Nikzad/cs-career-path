#BEGIN PROGRAM
#Task: Read file,extract value and compute the average spam confidence.

# Step 1: Prompt user input for file name
f_name = input("Please, enter file name: ")

# Step 2: Handle file not found error
try:
    # Step 3: Open file and store file handle
    f_hand = open(f_name)

    # Step 4: Initialize counters
    match_count = 0
    decimal_count = 0

    # Step 5: Loop through all the lines in the file
    for line in f_hand:

        # Step 6: Check if lines contains spam confidence data
        if line.startswith("X-DSPAM-Confidence:"):

           # Step 7: Split line into label and value
           split_line = line.split(":")

           # Step 8: Convert extract value to float
           num = float(split_line[1])

           # step 9: Count matching lines and sum value
           match_count += 1
           decimal_count += num
    # Step 10: Calculate and print average result
    print(f"Average spam confidence: {decimal_count/match_count}")

# Step 11: Handling missing file error
except FileNotFoundError:
    print("File not found")