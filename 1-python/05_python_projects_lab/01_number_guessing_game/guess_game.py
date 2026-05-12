import random # Import random module to generate secret number

print("Welcome to Number Guessing Game!")  # game intro message
print("-" * 40)

while True: # MAIN GAME LOOP (controls replay system)

    while True: # LEVEL SELECTION LOOP (forces valid input)
        # ask user for difficulty level
        levels = input("Choose a level (Easy/Medium/Hard): ").strip().lower()
        # check if input is valid
        if levels in ("easy", "medium", "hard"):
            break  # exit loop if valid
        else:
            print("Invalid choice. Try again.")  # error message

    # SET DIFFICULTY RANGE BASED ON LEVEL
    if levels == "easy":
        max_number = 10  # easy mode range
    elif levels == "medium":
        max_number = 30  # medium mode range
    else:
        max_number = 50  # hard mode range

    # show user the range they will play in
    print(f" Guess a number between 1 and {max_number}")

    # GENERATE SECRET NUMBER FOR THIS GAME
    secret_num = random.randint(1, max_number)

    attempts = 0  # counter for number of guesses

    # GUESSING LOOP (main gameplay)
    while True:
        try:
            # take user input and convert to integer
            guess = int(input(f"Your guess (1-{max_number}): "))
        except ValueError:
            # handles non-numeric input
            print(" Please enter a valid number.")
            continue  # restart loop

        # check if guess is within valid range
        if guess < 1 or guess > max_number:
            print(f" Out of range! (1-{max_number})")
            continue  # skip invalid input

        attempts += 1  # increase attempt count for valid guess

        # HINT SYSTEM (helps player)
        if guess < secret_num:
            print("Try higher ")  # guess is too low
        elif guess > secret_num:
            print("Try lower ")  # guess is too high
        else:
            # correct answer
            print(f"Correct! You got it in {attempts} attempts!")
            break  # exit guessing loop

    # 🔹 REPLAY SYSTEM
    play_again = input("Play again? (yes/no): ").strip().lower()

    # check if user wants to continue
    if play_again not in ("yes", "y"):
        print("Thanks for playing!")  # exit message
        break  # exit main loop

    print("-" * 40)  # separator between games



