# Variables & Basic Data Types

---

# 1. The 5 Main Basic Data Types

1. Integer → `int`
2. Float → `float`
3. String → `str`
4. Boolean → `bool`
5. Complex → `complex`

Each type is used to store a different kind of value.

---

# Integer — int

Type: `int`  
Stores: whole numbers  
Examples: `10`, `-5`, `0`, `100`  
Decimals: not included  
Useful for: counting, quantities, ages, scores

---

# Float — float

Type: `float`  
Stores: numbers with decimal values  
Examples: `3.14`, `10.5`, `-2.5`  
Useful for: prices, measurements, averages, percentages

---

# String — str

Type: `str`  
Stores: text  
Written inside: quotes  
Examples: `"Hello"`, `"Python"`, `"123"`  
Useful for: names, messages, sentences, labels

Important warning:

`"123"` is a string.

`123` is an integer.

---

# Boolean — bool

Type: `bool`  
Stores: `True` or `False`  
Values: `True` / `False`  
Useful for: conditions, decisions, yes/no states

---

# Complex — complex

Type: `complex`  
Stores: complex numbers  
Contains: real part + imaginary part  
Uses: `j` for the imaginary part

Useful for:

Mathematics  
Engineering  
Scientific calculations

---

# The 5 Types — Quick Review

`int` → whole numbers  
`float` → decimal numbers  
`str` → text  
`bool` → True or False  
`complex` → complex numbers

---

# 2. Variables

What it is?

A variable is a name that refers to a value stored in a Python program.

What problem it solves?

It lets us store information, reuse it, change it, and work with it instead of writing the value repeatedly.

When I would recognize the need for it:

Store a person's name  
Store a number  
Store a calculation result  
Store True or False  
Store text  
Reuse data later  
Change a value during the program

Syntax:

variable_name = value

---

# 3. Variable Names

Python has rules for creating variable names.

- Must not start with a number
- Must not contain spaces
- Must not be a Python keyword
- Can contain letters, numbers, and underscores `_`
- Variable names are case-sensitive
- Should use meaningful names

---

# 4. Method vs Function

Function → A reusable block of code that performs a task. Example:

`type(x)` → Returns the data type of `x`.

`len(x)` → Returns the number of characters in `x`.

`ord(x)` → Returns the Unicode code of a character.

Method → A function that belongs to an object and is called using `.`. Example: `x.upper()`

---

# 5. String Indexing

Indexing → Accessing a specific character in a string using its position.

Python starts indexing from `0`.

Example: `x[0]` → gets the first character of `x`.

---

# 6. String Iterable

Iterable → A string can be read one character at a time.

Example: `for char in x:` → goes through each character in `x`.

---

# f-string 

f-string → A Python string prefixed with f that allows variables and expressions to be evaluated directly inside {}.

