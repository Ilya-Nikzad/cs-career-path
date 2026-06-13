# What is a Regular Expression (Regex)?
📌 Explanation

A regular expression (regex) is a special pattern used to:
👉 search for text  
👉 match text  
👉 extract parts of text  

Instead of searching for exact words, regex lets you define rules for patterns.

---

# 2 — Core Regex Symbols (Basic Building Blocks)
📌 Explanation

Regular expressions use special symbols to define patterns instead of exact words.

These symbols act like “rules” for matching text.

## 1. ^ (caret)
📌 Meaning:  
Matches the start of a line  

---

# 3 — Using re.search() for Pattern Matching
📌 Explanation

In Python, regular expressions are stored in the re module.

Before using regex, we must import it:  
import re  

## re.search()
One of the most common functions is:  
re.search(pattern, text)  

It checks whether a pattern exists inside some text.

re.search() returns:
- Match found → True-like result  
- No match → None (False-like result)  

So it can be used inside an if statement.

---

# 4 — The ^ (Caret) Symbol: Match the Start of a Line
📌 Explanation

In regular expressions:

^

does not mean a normal caret character.

It is a special regex symbol that means:

👉 the beginning of a line  

---

# The . (Dot) Symbol: Match Any Character
📌 Explanation

In regular expressions:

.

is a special symbol that means:

👉 any single character  

It can match:
- a letter  
- a number  
- a symbol  
- a space  

(Almost any character.)

---

# 6 — The * (Star) Symbol: Match Zero or More Times
📌 Explanation

In regular expressions:

*

means:

👉 repeat the character or pattern before it zero or more times  

The star does not work by itself.

It always applies to the item immediately before it.

---

# 7 — The \S Symbol: Match a Non-Whitespace Character
📌 Explanation

In regular expressions:

\S  

means:

👉 any character that is NOT whitespace  

Whitespace includes:
- space " "  
- tab \t  
- newline \n  

---

# 8 — The + Symbol: Match One or More Times
📌 Explanation

In regular expressions:

+

means:

👉 one or more occurrences of the pattern before it  

Like *, the + applies to the item immediately before it.

NOTE  
Difference Between * and +  
*  →  zero or more (maybe)  
+  →  one or more (must!)  

---

# Q1 What is a regular expression (regex)?
A regular expression (regex) is a pattern language used to search,  
match, and extract text based on patterns instead of exact words.

# Q2 What does the symbol ^ mean in a regex pattern?
^ means the beginning of a line.

# Q3 What does the symbol . mean in a regex pattern?
. means any single character

# Q4 What is the difference between * and +?
* = zero or more occurrences  
+ = at least one or more occurrences  

# Q5 What does \S match?
\S matches any non-whitespace character.

# Q6 What does this pattern mean? ^X-\S+:
It matches a line that:  
starts with X-  
followed by one or more non-whitespace characters  
and ends with a :

---

# Summary
Regex basics:
^ → start of line  
. → any single character  
* → zero or more  
+ → one or more  
\S → non-whitespace character