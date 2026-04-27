#BEGIN PROGRAM
# Find maximum in a list
# Step 1: Initialize a list of numbers
max_list = [12, 34, 766, 32, 2]
# Step 2: Assume the first element is the maximum
maximum = max_list[0]
# Print list for readability
print("Numbers in the list:", end=' ')
print(*max_list, sep=', ')
# Step 3: Loop through each number in the list
for num in max_list:
    # Step 4: Check if current number is greater than current maximum
    if num > maximum:
        # Update maximum value
        maximum = num
# Step 5: Print the maximum value
print("Maximum value:", maximum)
#END PROGRAM


#BEGIN PROGRAM
# Task 2: count item in list (code version)
# Step 1: Initialize a list of numbers
count_list = [12, 34, 766, 32, 2]

# Step 2: Stor value for count
count = 0
# Step 3: Loop through each number in the list
for num in count_list:
    # Step 4: Increment count by 1 for each item
    count += 1
# Step 5: Output the result
print("Count:", count)
#END PROGRAM


#BEGIN PROGRAM
# Task 3: Simple function + loop combo
# Step 1: Initialize multiplication_table function
def multiplication_table():
    num = int(input("Enter a number: "))
    for i in range(1, 11):
      x = num * i
      print (f"{num} x {i} = {x}")
    return "Multiplication table"
print(multiplication_table())
#END PROGRAM

