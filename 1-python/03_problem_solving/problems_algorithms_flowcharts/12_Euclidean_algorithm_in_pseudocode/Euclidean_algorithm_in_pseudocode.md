# 1: What is the Euclidean Algorithm?
The Euclidean Algorithm is a method used to find the Greatest Common Divisor (GCD) of two numbers.  
The GCD is the largest number that divides both numbers exactly.  
The algorithm works by repeatedly subtracting the smaller number from the larger number until both numbers become equal.  
When both numbers are equal, that value is the GCD.  

Example  
Find the GCD of 12 and 8:  
12 > 8  
→ 12 − 8 = 4  
Now:  
a = 4  
b = 8  
Next:  
8 > 4  
→ 8 − 4 = 4  
Now:  
a = 4  
b = 4  

---

# 2: Euclidean Algorithm Using a WHILE Loop (Pseudocode Idea)
A while loop repeats instructions as long as a condition is true.  
For the Euclidean Algorithm, the condition is:  
“keep looping while a ≠ b”  
Inside the loop, we reduce the larger number by subtracting the smaller number.  

Explanation  
We define a function:  
Name: Greatest Common Divisor  
Inputs: a, b (integers)  
Then:  
While a is not equal to b  
If a > b, replace a with a - b  
Else, replace b with a - b  
Repeat until both are equal  
Return a  

---

# 3: Euclidean Algorithm Using a FOR Loop (Pseudocode Idea)
A for loop repeats a fixed number of times.  
In this version of the Euclidean Algorithm, we force a  
maximum number of iterations instead of stopping based on a condition.  
We use:  
for i from 0 to (a + b)  
This is just a “safe upper limit” so the loop runs enough times to reach the answer.  

Explanation  
We define a function:  
Name: Greatest Common Divisor  
Inputs: a, b  
Then:  
Loop from i = 0 to i = a + b  
If a == b, stop the loop early (break)  
If a > b, set a = a - b  
If b > a, set b = a - b  
After loop ends, return a  

---

# Q1: What does the Euclidean Algorithm aim to find?
The Euclidean Algorithm finds the Greatest Common Divisor (GCD) of two numbers.  

# Q2: In the subtraction method, what do we do when a > b?
When a > b, we replace a with a - b  

# Q3: What is the stopping condition in the WHILE loop version?
when both numbers are equal a == b  

# Q4: In the FOR loop version, why do we use a + b as the loop limit?  
Use a + b as the loop limit to ensure the loop runs enough times to guarantee the algorithm finishes  

# Q5: What happens when both numbers become equal?
we stop the loop, and that value is returned as the GCD.  

# Key Thinking Pattern: “Reduce Until Equal”

# 4: The Euclidean Algorithm follows this thinking model:
Pattern:  
👉 Start with two numbers  
👉 Reduce the larger one  
👉 Keep shrinking the difference  
👉 Stop when both are equal  

Core idea in real life:  
“Find the biggest shared factor to simplify or optimize systems”  

# What to remember (Exam focus)
GCD = largest common divisor  
Use subtraction repeatedly  
WHILE loop = condition-based repetition  
FOR loop = fixed repetition + break  
Stop when a == b