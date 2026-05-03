#BEGIN PROGRAM
frequency_list = ["d","d","e","c","c","c","d","a"]
frequency = {}
for item in frequency_list:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1
print(frequency)
frequency_list = ["d","d","e","c","c","c","d","a"]
for item in frequency_list:
    count = 0
    for x in frequency_list:
        if x == item:
            count += 1
    print(item, count)


factories = ["FreshMilk Plant", "DairyMax Plant"]

departments = ["Collection", "Processing", "Packaging"]

machines = ["Pasteurizer", "Filling Machine"]

actions = ["Start", "Heat Treatment", "Sterilize", "Pack Milk", "Shutdown"]


for factory in factories:   # Loop 1
    print(f"\n🏭 Factory: {factory}")

    for department in departments:   # Loop 2
        print(f"  🏢 Department: {department}")

        for machine in machines:   # Loop 3
            print(f"    ⚙️ Machine: {machine}")

            for action in actions:   # Loop 4 (actual work cycle)
                print(f"      🥛 Action: {action} on {machine}")




#BEGIN PROGRAM
# Step 1: Prompt user input
f_name = input("Please enter file name: ")
# Step 2: Using to handle file not found error
try:
    # Step 3: Create variable store open file
    f_hand = open(f_name)
    # Step 4: Loop through all the lines in the file
    for line in f_hand:
        # Step 6: show output result
        print(line.upper().rstrip()) # Using upper and rstrip to make the word upper and remove right side whitespace
except FileNotFoundError:
    print("File not found")
#END PROGRAM



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
