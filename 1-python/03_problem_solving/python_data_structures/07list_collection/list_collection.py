#BEGIN PROGRAM
# MINI PROJECT IDEA: Program counts even and odd numbers

# Step 1: Initialize list of numbers
list_num = [12,34,656,78,23,3,4,5,6,66]

# Step 2: Set counters for even and odd
even_numbers = 0
odd_numbers = 0

# Step 3: Loop through all numbers in list
for num in list_num:
    # Step 4: Check if num % 2 is equal to 0
    if num % 2 == 0:
        # Step 5: Increase count even by 1
        even_numbers += 1
    # Step 6: If it isn't num % 2 is equal to 0
    else:
        # Step 7: Increase count odd by 1
        odd_numbers += 1
# Step 8: Output result for both counters
print(f"Even numbers are: {even_numbers}, Odd numbers are: {odd_numbers}")