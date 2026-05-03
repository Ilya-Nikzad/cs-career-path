#BEGIN PROGRAM
# Task 7: Finding max in the list

# Step 1: Initialize a list of number
list_num = [12,555,23,5,8,1,8]

# Step 2: Initialize max as first index
max_num = list_num[0]

# Step 3: Loop through all numbers in the list
for check_num in list_num:
    # Step 4: Check which number is bigger
    if check_num > max_num:
        # Step 5: Store bigger num in max_num
        max_num = check_num
# Output result
print(max_num)