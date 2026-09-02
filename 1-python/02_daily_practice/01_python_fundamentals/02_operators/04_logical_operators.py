# Project: Iris Measurement Classifier
# Data Source
# Website: UCI Machine Learning Repository
# Dataset: Iris Dataset
# What it contains: 150 iris flower measurements

# Level 1: Find flowers that have both a petal length greater than 5.0 cm and a petal width greater than 1.5 cm.
# Read each flower's petal length and petal width.
# Use and to check both conditions.
# Print the measurements when both conditions are satisfied.

# Level 2: Task: Expand your classifier so a flower is selected if it either meets the existing measurement requirements,
# or has an especially large petal length.
# Keep your existing and condition.
# Add an or condition for petal length greater than 6.0 cm.
# Print the flower when either condition is satisfied.

# Level 3: Task: Make the classifier more precise by excluding flowers with a petal width of exactly 1.5 cm from the first condition.
# Keep your existing and + or logic.
# Change the first petal-width comparison so it requires the width to be strictly greater than 1.5 cm.
# Add a not condition so flowers with petal length not greater than 6.0 cm are handled separately.
# Print a different message for those flowers.


file_name = "iris.csv"

with open(file_name) as file:
    for row in file:
        row = row.strip()

        if not row:
            continue

        row = row.split(',')
        petal_length = float(row[0])
        petal_width = float(row[1])

        if (petal_length > 5.0 and petal_width > 1.5) or (petal_length > 6.0):
            print(
                f"Petal length: {petal_length} cm, "
                f"Petal width: {petal_width} cm, "
                f"Longer length: {petal_length} cm"
            )

        elif not (petal_length > 6.0):
            print(
                f"Petal length is not greater than 6.0 cm: "
                f"{petal_length}"
            )