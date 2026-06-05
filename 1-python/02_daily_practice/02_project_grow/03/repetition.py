# Task 1: Print numbers 1 → 10 using a for loop.
for i in range(1,11):
    print(i)

# Task 2: Print numbers 10 → 1 using a while loop.
count = 10
while count > 0:
    print(count)
    count -= 1
# Task 3: Ask user for a number.Print multiplication table.
multiple_num = int(input("Please enter a number: "))
for i in range(1,11):
    print (multiple_num,"x",i,"=", multiple_num * i)

#Task 4: Ask user for password. Keep asking until correct password entered.
correct_password = "121212"
while True:
    password = input("Please enter password: ")
    if password == correct_password:
        break
    else:
        print("Please enter a valid password")

#Task 5 — ATM PIN Validation correct pin = "1234" user has 3 tries
# if correct "Access granted" else after 3 fails "Card locked"
correct_pin = "123456"
attempts = 0
while attempts < 3:
    pin = input("Enter your pin: ")
    if pin == correct_pin:
        print("Correct pin")
        break
    else:
        attempts += 1
        print("Wrong pin")
if attempts == 3:
    print("Card Locked")