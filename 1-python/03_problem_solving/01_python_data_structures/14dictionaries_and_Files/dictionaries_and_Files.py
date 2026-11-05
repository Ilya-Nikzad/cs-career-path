# Task 1: Counting file with dictionary
text = "hello Hanna , bye Hanna"
words = text.split()
count = {}
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
print(count)

# Task 2: Looping through files and building a histogram
file_name = input("Please enter file name: ? ")
file_handle = open(file_name)
count = {}

for line in file_handle:
    if line.startswith("From "):
        print(line)
    words = line.split()
    for word in words:
       count[word] = count.get(word, 0) + 1

print(count)


# Task 3:
# Read the file mbox-short.txt, extract email addresses from lines starting with
# "From ", count how many times each sender appears using a dictionary,
# and determine the email address with the highest frequency.

#BEGIN
# file_name ← input("Enter file name")
file_name = input("Please enter file name: ? ")
# file_handle ← open(file_name)
file_handle = open(file_name)

# histogram ← {}
histogram = {}

#for each line in file_handle
for line in file_handle:
    #if line starts with "From "
    if line.startswith("From "):
        # words ← line.split()
        words = line.split()
        # email ← words[1]
        email = words[1]
        # if email in histogram then
        if email in histogram:
            # histogram[email] ← histogram[email] + 1
            histogram[email] += 1
        # else
        else:
            # histogram[email] ← 1
            histogram[email] = 1
# max_count ← 0
max_count = 0
# max_email ← None
max_email = ""

#for each email in histogram
for email in histogram:
    # if histogram[email] > max_count
    if histogram[email] > max_count:
        # max_count ← histogram[email]
        max_count = histogram[email]
        # max_email ← email
        max_email = email
# print max_email, max_count
print(max_email, max_count)
# END