# while loop
i = 0
while i < 5:
    i += 1
    print(i)

# count down forward
second = 0
while second <= 10:
    print(f"Time passed: {second}")
    second += 1

print("Time's up!")

# count down backward
second = 10
while second > 0:
    print (f"Time left: {second}")
    second -= 1
print(f"Times's up: {second}")

#validation loop
password = ""
while password != "121412":
    password = input("Please enter your password: ")
print("Access granted")


# Number guessing game
secret = 99
guess = 0
while guess != secret:
    guess = int(input("Guess a number (1-100: "))
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
print(f"You win {guess} correctly")
