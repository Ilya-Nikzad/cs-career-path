#BEGIN PROGRAM
# Step 1: Define function and take parameters a,b
def add(a, b):
    # Step 2: arithmetic operation: add parameters
    # Step 3: Return value
    return a + b
# Step 3: Call function with arguments
result = add(19,89)
# Step 4: Output result
print(result)
#END PROGRAM


#BEGIN PROGRAM
# Step 1: Define function, Take a parameter
def even_odd(num):
    # Step 2: Check condition: if true return "even", if false return "odd"
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
# Step 3: prompt user input
number = int(input("Please enter a number: "))
# Step 4: Call the function with input value
result = even_odd(result)
# Step 5: Output result
print(f"The number {number} is {result}")
#END PROGRAM


#BEGIN PROGRAM
# Step 1: Define function, Take a parameter
def greeting(name):
    # Step 2: return value
    return f"Hello: {name}!"
# Step 3: Prompt user take name
greet_user = input("Please enter your name: ")
# Step 4: Call function with argument
result = greeting(greet_user)
# Step 5: Output result
print(result)
#END PROGRAM



