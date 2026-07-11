# Lesson: Calculator Algorithm and Pseudocode

---

## 1. Algorithm

Begin

Step 1: Read the first number and the second number from the user.

Step 2: Read the operation selected by the user (+, -, *, /, %).

Step 3: Check the selected operation and perform the corresponding calculation.

Step 4: Before division, check if the second number is zero; if it is zero, display an error message.

Step 5: Display the calculation result to the user.

Step 6: If the selected operation is invalid, display an error message.

Step 7: Organize the calculator logic inside a function.

Step 8: Call the calculator function with user inputs and display the returned result.

End

---

## 2. Pseudocode

Begin

Function calculator(first_number, second_number, operation)

IF operation is "+"

    result ← first_number + second_number

ELSE IF operation is "-"

    result ← first_number - second_number

ELSE IF operation is "*"

    result ← first_number * second_number

ELSE IF operation is "/"

    IF second_number is not 0

        result ← first_number / second_number

    ELSE

        display "Error: Cannot divide by zero"

ELSE IF operation is "%"

    result ← (first_number * second_number) / 100

ELSE

    display "Invalid operation"

RETURN result

Read first_number

Read second_number

Read operation

result ← calculator(first_number, second_number, operation)

Display result

End