What is an algorithm?
A step-by-step method to solve a problem
It must:
Have clear steps
Take input
Produce output
End eventually


What is pseudocode?
A way to write algorithms using simple English + programming-like structure
It is NOT real Python.
It is:
easier than code
more structured than normal English
used for planning

Before coding in Python:
we first design the solution using pseudocode
IF a is greater than b THEN
    do something

The GCD of two numbers is:
The largest number that divides both numbers exactly (no remainder)

Idea behind Euclid’s Algorithm (core logic)
Now we move from what GCD is → to how we compute it efficiently.
Instead of checking all divisors, Euclid’s algorithm uses a key observation:
The GCD doesn't change if we replace the larger number with the difference of the two numbers.

What we do repeatedly
We keep doing:
If numbers are not equal:
subtract smaller from larger
replace the larger number with that result
Repeat until:
both numbers become equal


Flowchart logic (decision structure)
Now we convert the idea into decision steps, like a flowchart.
Step 1: Input
We start with two numbers:
a
b
Step 2: Check equality
We ask:
Is a equal to b?
If YES → stop and output a (this is the GCD)
If NO → continue
Step 3: Decide which is larger
We ask:
Is a greater than b?

If YES → replace a with (a − b)
If NO → replace b with (b − a)
Key idea
Each loop:
reduces one of the numbers
brings them closer together
Step 4: Repeat
After updating values:
go back and check again
This creates a loop:
compare
subtract
repeat
Final stopping condition
When:
a == b
we stop and output the result


We are not just subtracting numbers randomly.
We are using a mathematical property:
The GCD of two numbers does NOT change when we replace the larger number with their difference.


🔹 What problem we solved

We learned how to find the:

👉 Greatest Common Divisor (GCD)

🔹 Core method used

We used Euclid’s Algorithm, which works by:

Repeatedly subtracting the smaller number from the larger one
Keeping doing this until both numbers become equal
🔹 Final rule

When:

a == b

👉 That value is the GCD

🔹 Algorithm structure (pseudocode idea)
Input two numbers (a, b)
While they are not equal:
subtract smaller from larger
Output final value
Key thinking model

Instead of brute force:
We shrink the problem step-by-step while preserving the answer

Big takeaway
Looping = repetition until condition is met
IF/ELSE = decision making
Subtraction = problem reduction