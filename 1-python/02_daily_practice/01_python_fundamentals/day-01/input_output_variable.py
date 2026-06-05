#BEGIN PROGRAM
# Tax 1: Ask user name → print greeting

# Step 1: Prompt user to enter name
name = input("What is your name? ").strip() # .strip():removes spaces at start and end of a str

# Step 2: Output the result
print(F"Hello, {name}!") # Fstring: keep it clean
#END PROGRAM


#BEGIN PROGRAM
# Tax 2: Ask user age → print age + 5
# Step 1: Prompt user to enter age
age = int(input("What is your age? ")) # covert str to int

# Step 2: Perform arithmatic operation
sum_age = age + 5

# Step 3: Output the result
print(f"Your age is {age}, in 5 years you will be {sum_age}!")
#END PROGRAM

#BEGIN PROGRAM
# Tax 3: Ask user 2 numbers → print sum
# Step 1: Prompt user to enter two numbers
first_num = int(input("Please: Enter first number:")) # covert str to int
second_num = int(input("Please: Enter second number:"))

# Step 2: Perform arithmatic operation
total = first_num + second_num

# Step 3: Output the result
print(f"First: {first_num}, Second: {second_num}, Sum: {total}")
#END PROGRAM


# BEGIN PROGRAM
# Task 4: Create variables and print them in sentences

# Step 1: Declare variables
name = "Hanna"
age = 21
number_1 = 10
number_2 = 15.0

# Step 2: Output results and their data types
print(f"Name: {name}, Type: {type(name)}")            # type() shows the data type of a variable
print(f"Age: {age}, Type: {type(age)}")
print(f"First number: {number_1}, Type: {type(number_1)}")
print(f"Second number: {number_2}, Type: {type(number_2)}")

# END PROGRAM