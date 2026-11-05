# Task 1 : Histogram
names = ["Csev", "Cwen", "Csev", "Zhen", "Cwen"]

histogram = {}

for name in names:
    if name in histogram:
        histogram[name] += 1
    else:
        histogram[name] = 1

print(histogram)

# Task 2: Counts how many times each name appears.
names = ["a", "b", "c", "d", "d"]
count = {}

for name in names:
    if name not in count:
        count[name] = 1
    else:
        count[name] += 1   # IMPORTANT FIX

print(count)


# Task 3: Histogram using .get()
names = ["Csev", "Cwen", "Csev", "Zhen", "Cwen"]
count = {}
for name in names:
    count[name] = count.get(name, 0) + 1
print(count)

# Task 4: Build a histogram (dictionary) that counts each word.
words = ["apple", "banana", "apple", "orange", "banana", "apple"]

histogram = {}

for name in words:
    histogram[name] = histogram.get(name, 0) + 1
print(histogram)