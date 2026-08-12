# Task:  Student Gradebook Viewer
# level 1: Basic
# Store the grades in a list.
# Display the entire list of grades.
# Display the total number of grades recorded.
# Identify and display key positions in the sequence:
# The first grade
# The last grade
# The highest grade
# The lowest grade

grades = [78, 92, 85, 64, 90, 73, 88]
print(f"Grade List: {grades}")
print(f"Total Grade: {len(grades)}")
print(f"First Grade: {grades[0]}")
print(f"Last Grade: {grades[-1]}")
print(f"Highest Grade: {max(grades)}")
print(f"Lowest Grade: {min(grades)}")



# Level 2: Intermediate Version
# Store both classes' grades separately.
# Create one combined grade list.
# Display the combined grades.
# Display the total number of grades.
# Display the first and last grades.
# Create a view showing only the middle portion of the combined grades.
# Keep the original class lists unchanged.

class_a = [78, 92, 85, 64]
class_b = [90, 73, 88, 81]
combined_class = class_a + class_b
print(f"Combined Class: {combined_class}")
print(f"Total Combined Class: {len(combined_class)}")
print(f"First grade: {combined_class[0]} Last grade: {combined_class[-1]}")
number = len(combined_class)
mid = number // 2
if number % 2 == 0:
    middle = combined_class[mid -1: mid +1]
else:
    middle = combined_class[mid]
print("Middle portion:", middle)
print(f"Class A: {class_a}\nClass B: {class_b}")



# Level 3: Complete Version
# Combine the two class grade lists.
# Display the complete combined gradebook.
# Display the total number of grades.
# Display the first and last grades.
# Display the middle portion of the gradebook.
# Create a separate copy of the combined grades for analysis.
# Use the separate copy to show the grades in highest-to-lowest order.
# Make sure the original combined gradebook remains in its original order.
# Display the original and analyzed versions clearly.

class_a = [78, 92, 85, 64]
class_b = [90, 73, 88, 81]

combine = class_a + class_b
print(combine)
print(f"First grade {combine[0]} Last grade {combine[-1]}")
number = len(combine)
mid = number//2
if number % 2 == 0:
    middle = combine[mid-1:mid+1]
else:
    middle = combine[mid]
print(f"Middle portion: {middle}")
combine_copy = combine.copy()
combine_copy.sort(reverse=True)
print(f"Original gradebook (unchanged): {combine}")
print(f"Analyzed gradebook (highest to lowest): {combine_copy}")
