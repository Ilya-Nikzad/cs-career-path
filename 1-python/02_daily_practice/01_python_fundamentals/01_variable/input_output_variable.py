# 1. Integer (int)
age = 15

print(f"age: {age}")
print(f"type: {type(age)}")


# 2. Float (float)
price = 12.50

print(f"price: {price}")
print(f"type: {type(price)}")


# 3. String (str)
name = "Hanna"

print(f"name: {name}")
print(f"type: {type(name)}")


# 4. Boolean (bool)
is_student = True

print(f"is_student: {is_student}")
print(f"type: {type(is_student)}")


# 5. Complex (complex)
number = 3 + 4j

print(f"number: {number}")
print(f"type: {type(number)}")

letter = "x"

# function
print(f"type: {type(number)}")
print(f"length of name: {len(name)}")
print(f"Unicode of letter: {ord(letter)}")


# Method
print(f"uppercase name: {name.upper()}")


# indexing
print(f"first character: {name[0]}")


# String iterable
for letter in name:
    print(f"Iterable string: {letter}")