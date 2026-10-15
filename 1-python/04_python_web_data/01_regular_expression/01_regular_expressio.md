# Regular Expression "Regex"

## Core Idea

Regular expressions (Regex) let you search for patterns in text instead of searching for exact words.

Regex allows you to describe what the text should look like.

Python's re library can then search for matching text and extract the results.

The key idea is: you describe the pattern, and Python finds the matching text.

---

## 1. What is a regular expression?

A regular expression is a string that describes a text pattern. Like: 

pattern = "cat"

text = "The cat is sleeping."

But regex becomes more powerful when you use special symbols to describe patterns that can match many different pieces of text.

Consider these examples:

Pattern and What it describes

cat:  The exact text cat

c.t:  c, followed by any character, followed by t

cat:  ca followed by one or more t characters

\s:   A whitespace character

[0-9]:	One digit from 0 to 9

In Python, Regex is used to find patterns in text.

- . means any character.
- \. means a real period (.).
- \ changes how a symbol is interpreted.
- This is called escaping.

---

2. `The re library`

re is a built-in Python library used to search, match, and replace text patterns using Regex.

```       

import re

text = "Your order number is 5821."
result = re.search("order", text)

print(result)

```
