#BEGIN PROGRAM
# Task 1: Greeting Function take user's name as parameter

# Step 1: Define function with a single parameter
def greeting(name):
    # Step 2: Return value
    return f'Hello, {name}!'
# Step 3: Take argument and print result
print((greeting("Hanna")))
#END PROGRAM



#BEGIN PROGRAM
# Task 2: Function that takes 2 parameters and calculates sum

# Step 1: Define function
def sum_numbers(num1, num2):
    # Step 2: Perform arithmetic addition and return result
    return num1 + num2

# Step 3: Call function with arguments and print result
print(sum_numbers(1, 2))
#END PROGRAM


#BEGIN PROGRAM
# Task 3: Function to check odd and even

# Step 1: Define function
def check_number(num):
    # Step 2: Check whether number is odd or even
    if num % 2 == 0:
        return "It is an even number"
    else:
        return "It is an odd number"

# Step 3: Call function and print result
print(check_number(897492))
#END PROGRAM


#BEGIN PROGRAM
# Task 4: Function takes name and prints greeting

# Step 1: Define function with parameter
def greeting(name):
    # Step 2: Return greeting message
    return "Hello, " + name + "!"

# Step 3: Take user input as argument
name = input("What is your name? ")

# Step 4: Call function and print result
print(greeting(name))
#END PROGRAM