#BEGIN PROGRAM
# Task 1: Prints numbers from 1 to 5 using a loop

# Step 1: Loop through range 1 to 5
for i in range(1,6):
    # Step 2: Output result
    print(i)
#END PROGRAM


#BEGIN PROGRAM
# Task 2: Uses a loop to print numbers from 1 to 10

# Step 1: Loop through range
for i in range(1,11):
    # Step 2: Output result
    print(i)
#END PROGRAM


# BEGIN PROGRAM
# Task 3: Print numbers from 1 to 20 and calculate their sum, then print the final result

# Step 1: Initialize variable to store sum
count = 0

# Step 2: Loop through numbers from 1 to 20
for num in range(1, 21):
    # Step 3: Print each number from 1 to 20
    print(num)

    # Step 4: Add each number to the total sum
    count += num

# Step 5: Output the final sum
print(count)
# END PROGRAM


#BEGIN PROGRAM
# Task 4: Print numbers 1–10, count even numbers, and print total even count and sum

# Step 1: Initialize variable to store count of even numbers
even_count = 0

# Step 2: Initialize variable to store sum of even numbers
sum_even = 0

# Step 3: Loop through numbers from 1 to 10
for num in range(1, 11):

    # Step 4: Check if number is even
    if num % 2 == 0:
        even_count += 1      # Count even number
        sum_even += num      # Add even number to sum

# Step 5: Output results
print("Total even numbers:", even_count)
print("Sum of even numbers:", sum_even)
#END PROGRAM


# BEGIN PROGRAM
# Task 5: Guessing Game

# Step 1: Store the correct secret number
correct_guess = 234

# Step 2: Use an infinite loop until the correct guess is entered
while True:

    # Step 3: Handle invalid (non-number) input
    try:

        # Step 4: Ask the user to enter a guess
        guess = int(input("Guess a number: "))

        # Step 5: Check if the guess is correct
        if guess == correct_guess:
            print("Congratulations, you guessed it")

            # Step 6: Stop the loop when guessed correctly
            break

        # Step 7: Check if guess is too low
        elif guess < correct_guess:
            print("Too low")

        # Step 8: Otherwise the guess is too high
        else:
            print("Too high")

    # Step 9: Handle invalid input error
    except ValueError:
        print("Please enter a number.")
#END PROGRAM



# BEGIN PROGRAM
# Task 6: Keeps asking the user for a password until they enter the correct one.

# Step 1: Initialize a correct password value and store it
correct_pass = "python123"

# Step 2: Use an infinite loop until the right password is entered
while True:
    # Step 3: Prompt user to enter password
    password = input("Enter your password: ")
    # Step 4: Check if pass is correct
    if password == correct_pass:
        print("Access granted")
        # Step 6: Stop the loop when guessed correctly
        break
    else:
        print("Access denied")
#END PROGRAM


# BEGIN PROGRAM
# Task 6: keeps asking the user for numbers and adds them together until the user enters 0.

# Step 1: Initialize variable to store total sum (Memory)
count = 0

# Step 2:Use an infinite loop until user enter 0
while True:
    # Step 2: Prompt user enter a number
    number = int(input("Enter your number: "))
    # Step 3: If number is 0 print result and exit
    if number == 0:
        print("Total: ", count)
        # Stop loop and exit
        break
        # Step 4: Compute the number and add
    if number != 0:
        count += number
#END PROGRAM

