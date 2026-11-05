# Q1 (Simple): String Concatenation  
What is string concatenation in Python, and which operator is used for it?  
String concatenation means joining two or more strings together using the `+` operator.

# Q2 (Conceptual – simple): `in` as logical operator  
How is the `in` keyword used as a logical operator in conditions? What does it return?  
`in` checks whether a value exists inside a string. It returns `True` or `False`, so it works as a logical condition.

# Q3 (Conceptual – medium): String comparison  
How does Python compare two strings? What does it actually compare internally?  
Compares strings left to right, character by character, using Unicode values, until the first difference is found. That decides True or False. Like `A < Z < a < z`.

# Q4 (Conceptual – String library)  
What is the purpose of the string library (string module) in Python? Give a simple explanation.  
The string module provides a set of built-in tools/constants that help you work with text more easily (like predefined character sets such as letters, digits, punctuation).

# Q5 (Conceptual – class and dir)  
What is the purpose of the `dir()` function when used with a string in Python?  
The `dir()` function is used to list all methods and capabilities of a string object, so you can see what you can do with it.

# Q6 (Practical – searching string)  
Write a program that checks if the word "python" exists inside this text: The code is in python file  
text = "The code is in python file"  
if "python" in text.lower():  
    print("Found")  
else:  
    print("Not found")

# Q7 (Conceptual – upper/lower cases)  
What do `.upper()` and `.lower()` do in Python strings?  
.upper() → converts all characters to uppercase (BIG letters)  
.lower() → converts all characters to lowercase (small letters)

# Q10 (Conceptual – stripping whitespace)  
What does the `.strip()` method do in Python strings?  
.strip() removes whitespace from both the left and right sides of a string. It does not change spaces inside the string, only the edges.

# Q11 (Conceptual – prefixes)  
What is `startswith()`?  
It checks the beginning (prefix) of a string and returns True or False.

# Q12 (Conceptual – parsing and extracting)  
What does parsing and extracting strings mean in simple terms?  
Parsing is understanding a string’s structure, and extracting is pulling out useful parts from it.

# Q13 (Practical – mixed methods)  
What will be the output of this code, and why?  
text = "  Python Programming  "  
result = text.strip().lower().replace("python", "java")  
print(result)  
Output: java programming

# Q14 (Conceptual – class and dir revisited)  
What is the difference between: a method and a function in Python strings?  
A function works on data you pass in, while a method belongs to an object and is called using dot notation.

# Q15 (Final – Lesson Check)  
What will this code output?  
text = "Data Science"  
print(text.find("Sci"))  
Output: 5 (because "Sci" starts at index 5)