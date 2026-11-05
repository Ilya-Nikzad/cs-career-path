# File Handling in Python – Q&A

## Q1 (Simple)
What is a file in programming?  
A file is a place in a computer that stores data permanently.

---

## Q2 (Conceptual – simple): Flat text  
What is a flat text file?  
A flat text file stores data as plain text, line by line, without complex structure (no formatting, just characters).

---

## Q3 (Conceptual – open file)  
What does the `open()` function do in Python?  
`open()` is used to open a file so the program can work with it (read from it or write to it).

---

## Q4 (Conceptual – syntax)  
What does this line mean? `fhand = open(filename, mode)`  

`open(filename, mode)` → opens the file  
`fhand` → is a file handle (reference to the file)  

Important:  
`fhand` does NOT store the file’s content.  
It stores a connection/handle to the file so you can read or write it.

---

## Q5 (Conceptual – mode)  
What does the mode in `open(filename, mode)` represent? Give one example.  
The mode tells Python how you want to use the file (read, write, etc.).

- `"r"` → read  
- `"w"` → write (overwrites file)  
- `"a"` → append (adds new content to the end without deleting existing content)

---

## Q6 (Conceptual – without mode)  
What happens if you open a file like this? `fhand = open("data.txt")`  

If no mode is given, Python uses default mode `"r"` (read mode).  
This means the file can only be read, not modified. It returns a file object that allows interaction with the file.

---

## Q7 (Conceptual – newline character)  
What is the purpose of the newline character `\n` in a text file?  
The newline character `\n` moves the cursor to a new line in a text file.

---

## Q8 (Conceptual – file lines)  
Why does a text file usually have a `\n` at the end of each line?  
A text file uses `\n` at the end of each line so that:  
- The current line ends properly  
- The next line starts on a new line  
- Data is stored in a line-by-line structure  

---

## Q9 (Practical – file reading basics)  
What will this code do?  
fhand = open("data.txt", "r")  
print(fhand.read())  

It reads all the content inside the file.

---

## Q10 (Conceptual – understanding file reading)  
What is the difference between `read()` and reading a file line by line?  

`read()` reads the entire file at once and returns everything as one big string.

---

## Q11 (Practical – line reading)  
What will this code do?  
fhand = open("data.txt", "r")  
for line in fhand:  
print(line)  

The loop reads the file line by line.  
Each iteration takes one line and prints it.

---

## Q12 (Conceptual – file handle)  
What is a file handle (`fhand`) in Python? What does it represent?  
A connection to a file object that allows Python to interact with the file.

---

## Q13 (Practical – safe closing)  
What is the purpose of closing a file using:  
fhand.close()  

It is used to finish working with a file and free up system resources.

---

## Q14 (Conceptual – safety & best practice)  
Why is it better to use a `with` statement when working with files instead of manually opening and closing them?  
- `with` automatically closes the file  
- It ensures the file is closed even if an error happens  
- It makes code safer and cleaner  

---

## Q15 (Final – parsing and extracting from file)  
What will this code do?  
with open("data.txt", "r") as fhand:  
for line in fhand:  
print(line.strip())  

It opens `data.txt`, reads it line by line, and prints each line without extra spaces or blank lines.