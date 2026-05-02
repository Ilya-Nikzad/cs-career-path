Module 03: Conditional Execution – Python Notes
Section 1: Conceptual Questions (with answers)

Question 1: What is the difference between if, elif, and else in Python?
Answer:

if → checks a condition first
elif → checks another condition only if previous if/elif were False
else → runs when all previous conditions are False ✅

Question 2: What do the logical operators and, or, and not do in Python?
Answer:

and → True only if both conditions are True
or → True if at least one condition is True
not → reverses the truth value: True becomes False, False becomes True ✅

Question 3: In what order does Python check conditions in an if…elif…else statement?
Answer: Top-down: if → first elif → next elif … → else at the end ✅

Question 4: How do you combine two conditions so that both must be True?
Answer: Use the and logical operator ✅

Section 2: Exercises (without answers/code)

Exercise 1 – Pseudo-Code Practice:
Write pseudo-code for a program that asks the user for their age, prints "You are a teenager" if age is between 13 and 19, else prints "You are not a teenager," and ends with a thank-you message.

Exercise 2 – Practical Coding Exercise 1:
Write a Python program that asks the user for a number, then prints whether it is positive, negative, or zero.

Exercise 3 – Mini-Challenge 1:
Write a Python program that asks for an exam score (0–100) and prints the grade according to:

90–100 → Grade A
80–89 → Grade B
70–79 → Grade C
Below 70 → Fail

Exercise 4 – Mini-Challenge 2:
Write a program that asks for temperature in Celsius and prints:

"Hot" if > 30
"Warm" if 20–30
"Cold" if < 20
Tips / Best Practices
Write pseudo-code before coding.
Always convert user input to the correct type before comparisons.
Use meaningful variable names.
Test all branches of if…elif…else to avoid logical errors.
For multiple conditions, use and / or appropriately.