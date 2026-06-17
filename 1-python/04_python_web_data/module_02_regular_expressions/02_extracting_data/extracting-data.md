# Regular Expressions — Extracting Data

## Core Concept

`findall()` lets you extract data instead of just checking True/False.

It scans through a string, finds every part that matches your pattern, and returns them all as a list.

---

# STEP 1: What is `findall()` and why do we use it?

`findall()` is a function in Python's `re` library.

It scans through a string, finds every part that matches your pattern, and returns them all as a list.

Example:

```python
import re

x = "My favorite numbers are 2, 19 and 42"

nums = re.findall("[0-9]+", x)

print(nums)
```

Output:

```python
['2', '19', '42']
```

---

# STEP 2: What does `[0-9]+` actually mean?

Before going further, let's break down the pattern.

## `[0-9]`

Square brackets describe **one single character**.

Inside the brackets, you define what that character can be.

```text
[0-9]
```

means:

- Any digit from 0 to 9
- Matches exactly one digit

Examples:

```text
5  ✓
8  ✓
12 ✗ (two digits)
```

---

## `+`

```text
+
```

means:

> One or more of the thing before it.

Therefore:

```text
[0-9]+
```

means:

> One or more digits in a row.

Examples:

```text
2
19
42
123456
```

---

## `[0-9]` vs `\d`

Both mean digit.

```text
[0-9]
```

and

```text
\d
```

are equivalent.

Examples:

```text
[0-9]+ == \d+
```

✅ Both match one or more digits.

---

# STEP 3: Greedy Matching

By default, regular expressions are **greedy**.

Greedy means:

> Match the largest possible string that still satisfies the pattern.

Example:

```python
import re

x = "From: stephen.marquard@uct.ac.za, from: test@mail.com"

result = re.findall('F.+:', x)

print(result)
```

Output:

```python
['From: stephen.marquard@uct.ac.za, from: test@mail.com']
```

---

## Why?

Pattern:

```text
F.+:
```

Breakdown:

| Part | Meaning |
|--------|--------|
| F | Start with F |
| . | Any character |
| + | One or more times |
| : | End with colon |

Greedy matching says:

> Take the largest match possible.

So it stretches all the way to the last colon.

Think of it like:

```text
Greedy = stretching a rubber band as far as possible
```

---

# STEP 4: Non-Greedy Matching

You can turn off greediness by adding:

```text
?
```

after `+` or `*`.

Example:

```python
import re

x = "From: stephen.marquard@uct.ac.za, from: test@mail.com"

result = re.findall('F.+?:', x)

print(result)
```

Output:

```python
['From:']
```

---

## Why?

Pattern:

```text
F.+?:
```

Breakdown:

| Part | Meaning |
|--------|--------|
| F | Start with F |
| . | Any character |
| +? | One or more, but non-greedy |
| : | End with colon |

Now regex says:

> Take the smallest match possible.

So it stops at the first colon.

---

## Greedy vs Non-Greedy

| Pattern | Type | Behaviour |
|----------|----------|----------|
| `.+` | Greedy | Largest possible match |
| `.+?` | Non-Greedy | Smallest possible match |
| `.*` | Greedy | Largest possible match |
| `.*?` | Non-Greedy | Smallest possible match |

Simple memory trick:

```text
Greedy = takes the biggest slice of cake
Non-Greedy = takes only the slice it needs
```

---

# STEP 5: Parentheses for Extraction

Sometimes you need to:

- Match a large pattern
- Extract only a small part

Use:

```text
()
```

for extraction.

---

## Example Without Parentheses

```python
import re

line = "From stephen.marquard@uct.ac.za Sat Jan 5"

result = re.findall('\S+@\S+', line)

print(result)
```

Output:

```python
['stephen.marquard@uct.ac.za']
```

---

## Example With Parentheses

```python
import re

line = "From stephen.marquard@uct.ac.za Sat Jan 5"

result = re.findall('\S+@(\S+)', line)

print(result)
```

Output:

```python
['uct.ac.za']
```

---

## Why?

Pattern:

```text
\S+@(\S+)
```

Matches:

```text
stephen.marquard@uct.ac.za
```

But extracts only:

```text
uct.ac.za
```

because it is inside:

```text
()
```

---

## Key Rule

```text
Match more → Extract less
```

Use the full pattern for accurate matching.

Use `()` to extract only the part you want.

---

# STEP 6: Matching Special Characters with Backslash

Many regex characters have special meanings:

```text
.
+
*
$
[
]
(
)
```

What if you want the actual character itself?

Use:

```text
\
```

before it.

---

## Example

```python
import re

x = "We charge $19.99 for the item"

result = re.findall('\$[0-9.]+', x)

print(result)
```

Output:

```python
['$19.99']
```

---

## Pattern Breakdown

```text
\$[0-9.]+
```

| Part | Meaning |
|--------|--------|
| `\$` | Literal dollar sign |
| `[0-9.]` | Digit or dot |
| `+` | One or more |

---

## Why Escape?

Without escape:

```text
$
```

means:

```text
End of line
```

With escape:

```text
\$
```

means:

```text
Actual dollar sign character
```

---

## Common Escapes

| Want to Match | Write |
|---------------|--------|
| . | `\.` |
| $ | `\$` |
| + | `\+` |
| * | `\*` |
| [ | `\[` |
| ] | `\]` |
| ( | `\(` |
| ) | `\)` |

---

# Summary

## `findall()`

Returns a list of all matching substrings.

Example:

```python
re.findall("[0-9]+", text)
```

---

## Character Patterns

| Pattern | Meaning |
|----------|----------|
| `[0-9]` | One digit |
| `[0-9]+` | One or more digits |
| `[0-9]*` | Zero or more digits |
| `[AEIOU]` | One uppercase vowel |
| `\S` | One non-whitespace character |

---

## Greedy vs Non-Greedy

| Pattern | Behaviour |
|----------|----------|
| `.+` | Longest match |
| `.+?` | Shortest match |
| `.*` | Longest match |
| `.*?` | Shortest match |

---

## Parentheses

```text
()
```

Used to extract only a specific part of a match.

Rule:

```text
Match more → Extract less
```

---

## Escape Characters

Use:

```text
\
```

before special regex characters when you want them treated literally.

Examples:

```text
\$  \.  \+  \*  \[
```