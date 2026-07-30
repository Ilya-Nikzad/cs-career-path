#BEGIN PROGRAM
#Task 1: Check user age (adult and minor)

# Step 1: prompt user for age
age = int(input("How old are you? ")) # Convert str to int

# Step 2: check the condition and output result
if age >= 18:
    print(f"Age {age} is an adult.")
else:
    print(f"Age {age} is a minor.")

#END PROGRAM



#BEGIN PROGRAM
# Task 2: Ask number is even or odd

# Step 1: prompt user enter number
number = int(input("Please, Enter a number: ? "))

# Step 2: check condition and output result
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

#END PROGRAM



# BEGIN PROGRAM
# Task: Checking password

# Step 1: Store the correct password
stored_pass = "Maryam nazanin"

# Step 2: Give the user 3 attempts
for i in range(3):

    # Step 3: Ask the user to enter the password
    # .strip() removes extra spaces from the beginning and end
    pass_value = input("Please enter a password: ").strip()

    # Step 4: Check if the entered password is correct
    if stored_pass == pass_value:
        print("Access granted.")
        break  # stop the loop if correct

# Step 5: If all 3 attempts are used and no correct password
else:
    print("Access denied. Too many attempts.")