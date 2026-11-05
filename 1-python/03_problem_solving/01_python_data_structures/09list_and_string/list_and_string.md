
# 🔹 Python split() — Clean Study Notes

---

# 1. Core Idea of split()

A string in Python can be broken into smaller parts using the built-in method called `split()`.

👉 Key idea:  
- `split()` = turn a sentence into a list of words  
- It splits using spaces  
- It removes the spaces  
- It returns a list  

---

# 2. Working with split results

👉 Key idea:  
After splitting, each piece can be accessed using indexes.

---

👉 Key idea:  
`split()` + `for loop` is a core Python pattern for processing text.

---

👉 Key idea:  
Default `split()` automatically handles messy spacing.

---

# 3. Custom separators

`split()` does NOT have to split using spaces.  
You can tell it to split using another character.

👉 Key idea:  
`split(character)` lets you control where the string is cut.

---

# 4. When separator is not found

What happens if the separator is not found:

If `split()` cannot find the separator,  
it returns a list containing the original string as one item.

👉 Key idea:  
If the separator is missing, `split()` returns the whole string as one list item.

---

# 5. Real-world usage

Using `split()` while reading file data:

👉 Key idea:  
`split()` makes extracting structured text much easier.

---

# 6. Double split concept

The “double split” concept (nested splitting):  
Sometimes we split a string twice to extract deeper information.

👉 Key idea:  
You can chain `split()` operations to break data into deeper layers.

---

👉 Key idea:  
Double split = step-by-step extraction from structured text

---

# 7. Common coding pattern

Clean pattern — skip lines + split + extract  
A very common real-world coding pattern (especially in file reading) is:

👉 Key idea:  
This pattern = filter → split → extract  
It is one of the most important text-processing patterns in Python.

---

# 8. Practice Questions

### Question 1: What does split() do to a string?
split() changes/breaks a string into smaller pieces (usually words) and returns them as a list.

---

### Question 2: What is the default separator used by split()?
The default separator for `split()` is whitespace.

---

### Question 3: What happens if the separator is NOT found in the string?
`split()` returns the whole original string as a single item inside a list.

---