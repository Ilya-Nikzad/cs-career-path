# 1: Dictionaries + Files = Powerful Counting  
A dictionary becomes extremely powerful when combined with files.  
The process is always the same:  

- Read text  
- Split text into words  
- Loop through words  
- Count using a dictionary  

### Key Idea  
- Files give us lots of data  
- Dictionaries help us count efficiently  

---

# 2: How `split()` turns text into words  
When we read a line from a file, it is just one long string.  
To count words, we must break it into parts.  

`split()` does this by separating text wherever there is whitespace (spaces, tabs, new lines).  

### Key Idea  
- `split()` converts text → list of words  
- This is the first step before counting with a dictionary  

---

# 3: Looping through files and building a histogram  
When we read a file in Python, we don’t get everything at once.  

### Key Idea  
- File loop → line loop → word loop → dictionary update  
- This is the full histogram pipeline  

---

# Q1: What does `split()` do when applied to a line of text?  
`split()` converts a string into a list of words separated by whitespace.  

---

# Q2: Why do we use `.get(word, 0)` instead of just `counts[word]`?  
Give me the value, but if it doesn’t exist, start from 0  

---

# What you learned:  
- `split()` → turns text into words  
- File loop → reads line by line  
- Dictionary → stores counts (histogram)  
- `.get(word, 0)` → avoids errors + initializes safely  

---

# Pattern:  
read → split → loop → count  

---

# ⚡ Core idea to remember:  
“Text → words → dictionary → frequency counts”