# Task 1: tuple
numbers = (10, 20, 30)
print(numbers)


# Task 2: Getting one item using its position.
numbers = (10, 20, 30)
print(numbers[0])


# Task 3: Going through each item one by one.
colors = ("red", "blue", "green")
for color in colors:
    print(color)


# Task 4: Finding the biggest value.
numbers = (10, 20, 30)
print(max(numbers))


# Task 4: Tuples can assign multiple variables at once.
(x, y) = (4, "Fred")
print(x)
print(y)


# Task 4: .items() + Tuple Unpacking in Loops
d = {"Chuck": 1, "Fred": 42}

for key, value in d.items():
    print(type(key), type(value))


# Task 5: MINI CHALLENGE
dictionary = {"a": 3, "b": 7, "c": 2}

max_key = None
max_value = 0

for key, value in dictionary.items():
    if value > max_value:
        max_value = value
        max_key = key
print(max_key, max_value)






# Task: Read a mailbox file, extract the hour from each "From " line timestamp,
# count occurrences per hour, and output the frequency distribution sorted by hour.
# Step 1: Get file name from user
# file_name ← input("Enter file name")
file_name = input("Please enter file name: ")

# Step 2: Open the file
# file_hand ← open(file_name)
file_handle = open(file_name)

# Step 3: Initialize dictionary to store counts
# counts ← empty dictionary
counts = {}

# Step 4: Read each line in the file
# for each line in file_hand:
for line in file_handle:

    # Step 5: Check only lines that start with "From "
    # if line starts with "From " then
    if line.startswith("From "):

        # Step 6: Extract time from the line
        # time ← split(line)[5]
        time = line.split()[5]

        # Step 7: Extract hour from time (HH:MM:SS)
        # hour ← split(time, ":")[0]
        hour = time.split(":")[0]

        # Step 8: Count occurrences of each hour
        # if hour exists in counts then counts[hour] ← counts[hour] + 1
        # else counts[hour] ← 1
        if hour in counts:
            counts[hour] += 1
        else:
            counts[hour] = 1

# Step 9: Print results sorted by hour
# for each hour in sorted(counts) do print hour, counts[hour]
for hour in sorted(counts):
    print(hour, counts[hour])