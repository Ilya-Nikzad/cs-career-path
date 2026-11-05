# Task 1: Change string into list
str = "I love Python"
list_str = str.split()
print(list_str)

# Task 2: Access the elements by index
print(list_str[0], list_str[1], list_str[2])


# Task 3: Using loop with split
for item in list_str:
    print(item)

# Task 4: Default split() automatically handles messy spacing.
messy_str = "I          love                  Python"
words = messy_str.split()
print(words)


# Task 5:split(character) lets you control where the string is cut.
data = "apple!banana!orange"
items = data.split("!")
print(items)


# Task 6: If the separator is missing, split() returns the whole string as one list item.
text = "apple-banana-orange"
result = text.split()
print(result)


# Task 7: split() makes extracting structured text much easier.
f_name = open("mbox-short.txt")
for line in f_name:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    word = line.split()
    print(word[1])


# Task 8: The “double split” concept (nested splitting)
data = "stephen@example.com"
parts = data.split("@")
subparts = parts[1].split(".")


# Task 8: The “double split” concept (nested splitting)
data = "stephen@example.com"
parts = data.split("@")
subparts = parts[1].split(".")
print(parts)
print(subparts)


# Task 9:
line = "From stephen@example.com Sat Jan 5"

# Step 1: Split the line
words = line.split()
print("All words:", words)

# Step 2: Extract email
email = words[1]
print("Email:", email)

# Step 3: Split email using "@"
pieces = email.split("@")
print("Email parts:", pieces)

# Step 4: Extract domain part
domain = pieces[1]
print("Domain:", domain)

# Task 1: Write code to extract only the domain part
line = "From stephen@example.com Sat Jan 5"
email = line.split()[1]
domain = email.split("@")[1]
print(domain)


# Task 2: From this line, extract the username only (before @):
line = "From stephen@example.com Sat Jan 5"
email = line.split()[1]
username = email.split("@")[0]
print(username)


# Task 3: From this line, extract only the domain name without .com
line = "From stephen@example.com Sat Jan 5"
email = line.split()[1]
domain = email.split("@")[1]
domain_name = domain.split(".")[0]
print(domain_name)


# Task 4: You are given multiple email log lines print ONLY the usernames:
# alice
# bob
# carol
lines = [
    "From alice@example.com Sat Jan 5",
    "From bob@gmail.com Sun Jan 6",
    "From carol@yahoo.com Mon Jan 7"
]
for line in lines:
    email = line.split()[1]
    username = email.split("@")[0]
    print(username)




