# Task 1: Return square of number
def square_number(number):
    return number * number
print(square_number(2))

# Task 2: Return "Positive" or "Negative".
def even_odd(num):
    if num % 2 == 0:
        return f"{num} : It's even."
    else:
        return f"{num} : It's odd."
print(even_odd(2))

# Task 3: Return full name.
def full_name(first_name, last_name):
    if first_name and last_name:
        return f"Full Name: {first_name} {last_name}."
    else:
        return f"Please, enter a first name and last name."
print (full_name(input("Please enter your first name: "), input("Please enter your last name: ")))


# Task 4: Return 20% discount if price > 100, otherwise return original price
def discount_checker(price):
    if price > 100:
        price = price - (price * 0.20)
        return f"20% off for prices above $100, Final Price: {price}"
    else:
        return f"Total Price: {price}"

print(discount_checker(int(input("Please enter a price: "))))

# Task 5:  Login Function:
def check_login():
    correct_username = "Hanna"
    correct_password = "122334"
    attempts = 0
    while attempts < 3:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username == correct_username and password == correct_password:
            return ("Access granted")
        attempts += 1
        if username != correct_username and password != correct_password:
            print("Username and password both incorrect")
        elif username != correct_username:
            print("Username is incorrect")
        else:
            print("Password is correct")
    return ("Too many attempts")
print(check_login())
