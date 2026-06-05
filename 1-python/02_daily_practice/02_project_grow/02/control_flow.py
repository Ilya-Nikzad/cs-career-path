#Task 1: Ask user for temperature above 30 hot below cold:
check_temperature = int(input("What temperature do you live in? "))
if check_temperature >= 30:
    print(f"temperature is {check_temperature}, It's hot")
else:
    print(f"temperature is {check_temperature}, It's cold")


# Task 2: sk user for a number: if number > 0 print "Positive" else print "Negative"
check_number = int(input("Please, Enter a number? "))
if check_number > 0:
    print(f"number {check_number} is positive ")
else:
    print(f"number {check_number} is negative ")


# Task 3: Ask exam score:
check_grade = int(input("Please, Enter your score? "))
if check_grade >= 90:
    print(f"{check_grade}: It's grade A")
elif check_grade >= 80:
    print(f"{check_grade}: It's grade B")
else:
    print(f"{check_grade}: It's grade C")

# Task 4: Ask username: if empty → print "Invalid input" else → print "Valid username"
check_username = (input("Please, Enter your username: "))
if check_username == "":
    print(f"username is empty, {check_username} is invalid")
else:
    print(f"username is {check_username}")

#Task 5 — Login System: check user name and password:
check_username = input("Please, Enter your username: ")
check_password = input("Please, Enter your password: ")
if check_username == "Hanna" and check_password == "124612":
    print("Access granted")
else:
    print("Access denied")

#Mini Build: Movie Age Checker: Ask user age if above 18 can watch and if senior 30% off
check_age = int(input("Please enter your age: "))
price = 100

if check_age < 18:
    print(f"Your age is {check_age}: Below 18 not allowed to watch.")
elif check_age <= 22:
    final_price = price * 0.7
    print(f"30% off for age 18 to 22. Final price: {final_price}. Enjoy the show.")
else:
    print(f"Price: {price}. Enjoy the show.")






