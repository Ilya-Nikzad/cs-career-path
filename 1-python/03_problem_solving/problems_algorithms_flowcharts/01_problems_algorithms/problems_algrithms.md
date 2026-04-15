# 📘 Algorithms & Problems – Lecture Notes

## 🧠 Why Do We Need Algorithms?
We use algorithms to solve problems.

Before defining algorithms, we must understand what a **problem** is in computer science.

---

## 💡 What is a Problem?

In everyday life, problems can be vague or complex (e.g., deciding to take a holiday).

In computer science, a problem must be:
- Clearly defined
- Solvable using data
- Expressed in a mathematical or logical form

Computers cannot handle vague questions without structure or context.

---

## 🔢 Input and Output

A computer science problem always has:

- **Input** → data given to the computer
- **Output** → the expected result or answer

### Example 1: Holiday Days
Let:
- x = total holiday days allowed
- y = holiday days already used

Two possible questions:

1. Can I take more holidays?
   - Condition: `x > y`
   - Output: True / False

2. How many holiday days are left?
   - Calculation: `x - y`
   - Output: a number

👉 Key idea: The type of output matters in defining the problem.

---

## 📌 Formal Definition of a Problem
A problem in computer science consists of:
- Well-defined input
- A question about that input
- A well-defined output

---

## 🔍 Example Problem

### Question:
Does the equation `x² = 2` have an integer solution?

- Input: 2
- Output: True / False

---

## 🧪 Different Solution Methods

### Method 1: Square Root Approach
- Compute √2
- Check if it is an integer

❌ Issue: Square root calculation is not a basic operation in simple algorithms.

---

### Method 2: Enumeration Approach
- Compute squares of integers: 1², 2², 3², ...
- Check if any equals 2
- Stop when value exceeds 2

✔ This method can be written as a proper algorithm.

---

## ⚠️ Key Insight
A problem can often have **multiple solution methods**.

Question:
Which method is better if both give the correct answer?

---

## 🤖 What is an Algorithm?

An algorithm is:
> A step-by-step set of simple instructions that solves a problem.

---

## 📌 Properties of Algorithms:
- Produces the correct output
- Uses basic operations (addition, comparison, logic, etc.)
- Can be executed by a computer
- Written as clear step-by-step instructions

---

## 🔁 Generalization of the Problem

For a more general problem like:
`x² = y`

We can adapt both methods:
- Square root method (requires a general square root algorithm)
- Enumeration method (checking increasing squares)

---

## ⭐ Key Takeaways
- A problem = input + question + output
- An algorithm = step-by-step method to solve a problem
- There can be multiple algorithms for the same problem
- General algorithms are more powerful and reusable

---