#BEGIN ALGORITHM

# Step 1: Initialize a list
num_list = [12, 346, 23, 54, 34]

# Step 2: Display heading
print("Number of list: ", end="")

# Step 3: Loop through list using index
for i in range(len(num_list)):
    # Step 4: Print elements with comma formatting, Ternary operator
    print(num_list[i], end=", " if i < len(num_list) - 1 else "")

# Step 5: Move to next line
print()

# Step 6: Initialize total variable
total = 0

# Step 7: Loop through each element
for num in num_list:
    # Step 8: Add each element to total
    total += num

# Step 9: Display sum of list
print(f"Sum of the list: {total}")

#END ALGORITHM


#BEGIN PROGRAM
# Step 1: Initialize a list
num_list = [12, 346, 23, 54, 34]

# Step 2: Add a new number to the list
num_list.append(100)

# Step 3: Remove one number from the list
num_list.remove(23)

# Step 4: Change one element in the list
num_list[1] = 999

# Step 5: Display updated list
print("Updated list:", num_list)
#END PROGRAM