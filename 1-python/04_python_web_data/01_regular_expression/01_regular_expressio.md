# Regular Expression "Regex"

## Core Idea

Regular expressions (Regex) let you search for patterns in text instead of searching for exact words.

Regex allows you to describe what the text should look like.

Python's re library can then search for matching text and extract the results.

The key idea is: you describe the pattern, and Python finds the matching text.

---

## 1. What is a regular expression?

A regular expression is a string that describes a text pattern.

```
pattern = "cat"

text = "The cat is sleeping."
```

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

## 2. The re library

re is a built-in Python library used to search, match, and replace text patterns using Regex.

```       
import re

text = "Your order number is 5821."
result = re.search("order", text)

print(result)

```
re.search() looks for the first occurrence of a matching pattern anywhere in the text.

It returns a match object when a match is found, or None when no match is found.

Regex matching is case-sensitive by default, so "order" does not match "Order"


Understanding the match object

- re.search() finds a matching pattern.
- .group() returns the matched text.
- if result checks whether a match exists, preventing errors if no match is found.

```
import re

text = "Your order number is 5821."
result = re.search("order", text)

if result:
    print(result.group())
```
The output is exact text: order 

---

## 3. re.search() versus re.findall()

These functions both look for patterns, but they return different kinds of results.

re.search()

Finds the first match anywhere in the string and returns a match object, or None.

```
import re

text = "Room 12, Floor 4, Room 27"
result = re.search(r"\d+", text)

print(result.group())
```

output:

`12`

re.findall()

Finds all non-overlapping matches and returns them in a list of strings for the patterns covered in this lesson.

```
import re

text = "Room 12, Floor 4, Room 27"
result = re.findall(r"\d+", text)

print(result)
```

Output:

`['12', '4', '27']`

Use re.search() when you only need to know whether a pattern appears or want the first occurrence.

Use re.findall() when you need to collect every occurrence.

Notice the r before the pattern string: r"\d+" is called a raw string.

It is a convenient way to write regex patterns containing backslashes without Python interpreting those backslashes as string escapes first.

---

## 4. Regex symbols: the important building blocks

A. ^ — Beginning of the string

The caret ^ matches the beginning of the string.

Use it when: checking whether a line or text field begins with a particular prefix.

B. $ — End of the string

The dollar sign $ matches the end of the string.

Together, ^ and $ can require a pattern to match the entire string.

C. . — Any character

A period . matches almost any single character, usually excluding newline characters.

D. * — Zero or more repetitions

The asterisk * means the preceding pattern can appear zero or more times.

E. + — One or more repetitions

The plus sign + also repeats the preceding pattern, but requires at least one occurrence.

Remember: * allows zero repetitions; + requires at least one.

F. \s — Whitespace

The pattern \s matches a whitespace character, such as a space, tab, or newline.
```
import re

text = "Order 25\nOrder 36"
print(re.findall(r"\s", text))
```

It finds the space between Order and 25, the newline, and the space between Order and 36.

To find a sequence of one or more whitespace characters, use \s+.

This is useful when text contains inconsistent spacing.

G. \S — Non-whitespace

The uppercase \S is the opposite of \s: it matches a character that is not whitespace.

Because + matches one or more repetitions, the pattern extracts each continuous group of non-whitespace characters.

Compare:
- \s+ finds groups of spaces, tabs, or newlines.
- \S+ finds groups of non-whitespace characters.

H. [] — Character sets

Square brackets define a set of allowed characters for a single position in the match.

```
import re

print(re.findall(r"[aeiou]", "education"))
```

Output: 

```
['e', 'u', 'a', 'i', 'o']
```
The pattern matches any one of the listed vowels.

Also: can use range with it

```
import re

print(re.findall(r"[0-9]", "Room 204, Floor 3"))
```

Output:
```
['2', '0', '4', '3']
```

() — Grouping

Parentheses group parts of a regex pattern together.

This is especially useful when applying repetition to a sequence of characters.

```
import re

text = "abc ababc ababab"
print(re.findall(r"(ab)+", text))
```

Output:
```
['ab', 'abab', 'ababab']
```

Here, (ab)+ matches one or more repetitions of the whole group ab.

Remember: () groups characters together, and + repeats the entire group.

- (ab)+ → repeats the whole ab.
- Matches: ab, abab, ababab
- ab+ → repeats only the letter b.
- Matches: ab, abb, abbb

---

## 5. Combining symbols into useful patterns

The real value of regex comes from combining simple symbols to describe a more useful pattern.

```
import re

text = "Products: AB123, XY456, A9123"

print(re.findall(r"[A-Z]+[0-9]+", text))
```

Output:

```
['AB123', 'XY456', 'A9123']
```

The pattern matches a sequence of uppercase letters followed by a sequence of digits.

---

## Important Rules
1. Import the library with import re.

2. re.search() returns the first match object or None.

3. re.findall() returns all non-overlapping matches as a list.

4. ^ matches the beginning; $ matches the end.

5. . matches almost any single character; \. matches a literal period.

6. * means zero or more repetitions; + means one or more.

7. \s matches whitespace; \S matches non-whitespace.

8. [ ] defines a set or range of allowed characters.

9. () groups patterns and can create capturing groups.

10. Regex finds patterns, but a match alone does not guarantee that the underlying data is valid.



