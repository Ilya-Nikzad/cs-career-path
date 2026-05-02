#BEGIN PROGRAM
# Check user is teenager or not

# Step 1: Prompt user to enter their age
age = int(input('Enter your age: ')) # Convert str to number

# Step 2: Condition to check teenager or not
if age >= 13 and age <= 19:
    print(f'You are {age} and a teenager.')
else:
    print(f'You are {age} and not a teenager.')

# Step 3: Display appreciate message
print("Thank you for checking your age!")
#END PROGRAM


#BEGIN PROGRAM
# Step 1: Prompt user to enter a number
num = int(input('Enter a number: ')) # Convert str to int

# Step 2: Checking condition and display result
if num > 0:
    print(f'The number {num} is positive.')
elif num < 0:
    print(f'The number {num} is negative.')
else:
    print(f'The number {num} is zero.')
#END PROGRAM


#BEGIN PROGRAM
# Step 1: Prompt user to enter score number
score = int(input('Enter your score: '))

# Step 2: Checking conditions and display the result
if score >= 90 and score <= 100:
    print(f'You are {score} and you are Grade A.')
elif score >= 80 and score <= 89:
    print(f'You are {score} and you are Grade B.')
elif score >= 70 and score <= 79:
    print(f'You are {score} and you are Grade C.')
else:
    print(f'You are {score} and you are Failed.')
#END PROGRAM


#BEGIN PROGRAM
# Step 1: Prompt user to enter temperature
temperature = int(input('Enter the temperature in Celsius: '))

# Step 2: Check the conditions and display result
if temperature >= 30 and temperature <= 100:
    print(f'The temperature is {temperature} and weather is hot.')
elif temperature >= 20 and temperature <= 29:
    print(f'The temperature is {temperature} and weather is warm.')
else:
    print(f'The temperature is {temperature} and weather is cold.')
#END PROGRAM