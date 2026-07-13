# Project: Develop a Python calculator application that performs the following operations:
# Addition (+)
# Subtraction (-)
# Multiplication (*)
# Division (/)
# Percentage (%)

# Function
def calculator(first_num, second_num, op):
    if op == "+":
        output = first_num + second_num
    elif op == "-":
        output = first_num - second_num
    elif op == "*":
        output = first_num * second_num
    elif op == "/":
        if second_num != 0:
            output = first_num / second_num
        else:
            return "Error: Cannot divide by zero"
    elif op == "%":
        output = (first_num * second_num) / 100
    else:
        return "Invalid operation"
    return output


# Call function
first_number = float(input("First number: "))
second_number = float(input("Second number: "))
operation = input("Operation (+, -, *, /, %): ")
result = calculator(first_number, second_number, operation)
print("Result:", result)
