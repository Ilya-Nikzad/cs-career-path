# 📘 String Operations – Single Loop Optimization

## 🔹 Problem
Given a sentence:
- Convert it to uppercase
- Convert it to lowercase
- Find its length

---

## 🔹 Idea (Optimization)
Instead of looping over the string multiple times, we can process everything in **one single loop**.

This improves efficiency because we avoid revisiting the same string repeatedly.

---

## 🔹 Algorithm

1. Start  
2. Take input sentence  
3. Initialize:
   - `uppercase = ""`
   - `lowercase = ""`
   - `length = 0`
4. Loop through each character in the sentence:
   - Convert character to uppercase and add to `uppercase`
   - Convert character to lowercase and add to `lowercase`
   - Increase `length` by 1  
5. Print results  
6. End  

---

## 🔹 Python Code (Single Loop)

```python
sentence = input("Enter a sentence: ")

uppercase = ""
lowercase = ""
length = 0

for char in sentence:
    uppercase += char.upper()
    lowercase += char.lower()
    length += 1

print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Length:", length)


## 🔷 Pro level 

1. Start  
2. Take input sentence from the user  
3. Convert the sentence to **uppercase**  
4. Convert the sentence to **lowercase**  
5. Find the **length** of the sentence  
6. Display uppercase, lowercase, and length  
7. End  

---

## 🔑 Key Idea

👉 Use built-in functions to process the whole string directly:
- `upper()` → uppercase  
- `lower()` → lowercase  
- `len()` → length  

---

## 🚀 Result

This approach is:
- Simple  
- Clean  
- Efficient  
- Easy to understand  