# `join() + split()`
---

split()

split() takes one string and breaks it into a list of pieces

.join() takes multiple strings and combines them into one string,
using the string before .join() as the separator.

split() → one string → many strings

join()  → many strings → one string

---

# `mportant Rule — join() + split()`

Type: string methods

split() call on: a string

join() call on: the separator string

split() input: optional separator

join() input: an iterable of strings

Basic syntax: text.split(separator) / separator.join(items)

split() returns: a list of strings

join() returns: one string

Original data: neither method changes the original string

Default split(): with no argument, splits on whitespace

Important join() restriction: the items being joined must be strings

Common mistake: "a,b,c".join(...) does NOT split "a,b,c"; the string before .join() is the separator

Direction: split() breaks apart; join() puts together

Mental model: “Split breaks a string apart; join connects strings together.”