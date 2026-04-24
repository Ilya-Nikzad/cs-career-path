# Python File Handling – Questions & Answers

---

## Q1 (Conceptual – simple)
**What does it mean when we say a file handle is a sequence in Python?**

A file handle is treated as a sequence of lines.  
When you loop over it, Python gives you one line at a time.

---

## Q2 (Practical – Counting Lines)
**Write a Python program to open a text file and count the number of lines in the file.**

### Algorithm:
- Start  
- Open the file in read mode  
- Initialize a counter variable (`count = 0`)  
- Read the file line by line  
- For each line, increment `count` by 1  
- After reaching the end of the file, close the file  
- Display the value of `count` (total number of lines)  
- End  

---

## Q3 (Conceptual – reading the whole file)
**What does `.read()` do when used on a file handle?**

`.read()` returns the entire file content as a single string,  
not line by line.

---

## Q4 (Conceptual – searching through a file)
**How can we search for a word inside a file using a loop?**

### Idea:
- Start  
- Open the file in read mode  
- Set the target word to search  
- Read the file line by line using a loop  
- For each line, check if the target word is present  
- If found, display “Word found” and stop the loop  
- If the loop ends without finding the word, display “Word not found”  
- Close the file  
- End  

---

## Q5 (Conceptual – “blank lines” problem)
**Why do we sometimes see blank lines when printing file content?**

Because:
- Each line already ends with `\n` (newline character)  
- `print()` also adds its own `\n`  
- This causes double spacing → extra blank lines  

---

## Q6 (Conceptual – rstrip)
**What does `.rstrip()` do when used on a string from a file line?**

- `.strip()` → removes both left and right spaces/characters  
- `.lstrip()` → removes only left (start) spaces/characters  
- `.rstrip()` → removes only right (end) spaces/characters  

---

## Q7 (Practical – skipping with continue)
**What will this code do?**

The program:
- Reads the file line by line  
- Skips any line that starts with `"From:"`  
- Prints all other lines  
- Removes trailing spaces and newline characters  

---

## Q8 (Conceptual – using `in` to select lines)
**What does this condition do?**

`"python" in line` checks whether the word `"python"` exists inside the line.  
It returns:
- `True` if found  
- `False` if not found  

---

## Q9 (Practical – prompt for file name)
**What will this code do?**

- `input()` asks the user to enter a file name  
- The entered name is stored in `fname`  
- `open(fname)` opens that file  
- `fhand` becomes the file handle (connection to the file)  

---

## Q10 (Conceptual – try/except for bad file name)
**What happens if the user enters a file name that does NOT exist?**

A **FileNotFoundError** occurs.  
The program will stop unless the error is handled.

---

## Q11 (Conceptual – try/except fix)
**How does try/except help when opening files?**

It prevents the program from crashing when an error happens.

- `try` → attempt to run the code  
- `except` → run this code if an error occurs instead  

It makes the program more stable and user-friendly.

---