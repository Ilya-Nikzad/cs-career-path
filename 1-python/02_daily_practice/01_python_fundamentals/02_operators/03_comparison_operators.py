# Project: Iris Petal Length Checker

# Level 1: Find flowers with petal lengths greater than 5.0 cm.
# Read each flower's petal length.
# Compare it with 5.0 cm.
# Print the petal length when it is greater than 5.0 cm.

# Level 2: Identify flowers with petal lengths less than 5.0 cm.
# Display a different message for those flowers.

# Level 3: Identify flowers with petal lengths exactly 5.0 cm.
# Display a specific message for exactly 5.0 cm.
# Make sure the greater than 5.0 and less than 5.0 cases still work correctly.


file_name = "iris.csv"
with open(file_name, "r") as f:

    for row in f:
        row = row.strip()

        if not row:
            continue

        row = row.split(',')
        petal_length = float(row[0])

        if petal_length > 5.0:
            print(f"Petal length is greater than 5.0 cm: {petal_length} cm")
        elif petal_length < 5.0:
            print(f"Petal length is less than 5.0 cm: {petal_length} cm")
        else:
            print(f"Petal length is exactly 5.0 cm: {petal_length} cm")