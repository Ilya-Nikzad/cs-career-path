#BEGIN PROGRAM

# Step 1: Repeat until the user enters valid numbers
while True:
    try:
        # Step 2: Prompt the user to enter two numbers
        num_1 = int(input("Please enter the first number: "))  # Convert to int
        num_2 = int(input("Please enter the second number: ")) # Convert to int
        # Step 3: Exit the loop if inputs are valid
        break
    except ValueError:
        # Step 4: Handle invalid input
        print("Oops! That was not a valid integer. Please try again.")

# Step 5: Calculate the sum of the two numbers
total = num_1 + num_2

# Step 6: Display the result
print(f'The sum of {num_1} and {num_2} is {total}')

#END PROGRAM

#BEGIN PROGRAM

# Step 1: Get user input
name = input("What is your name? ")
age = int(input("How old are you? ")) # Convert str to int

# Step 2: Output result
print(f"Hello {name}! You will be {age + 1} years old next year.")

#END PROGRAM

#BEGIN PROGRAM

# Step 1: Prompt the user to enter two numbers
num_1 = int(input("Please enter the first number: ")) # Convert type str to int
num_2 = int(input("Please enter the second number: ")) # Convert type str to int

# Step 2: Calculate the multiple of two numbers
total = num_1 * num_2

# Step 3: Display the result
print(f"The result is {total}")

#END PROGRAM

#BEGIN PROGRAM

# Step 1: Prompt user to enter a number
num = input("Please enter a number: ")

# Step 2: Convert string to float
num = float(num)

# Step 3: Multiply number by 2 and display result
print(f'The multiple of {num} is {num * 2}')

#END PROGRAM