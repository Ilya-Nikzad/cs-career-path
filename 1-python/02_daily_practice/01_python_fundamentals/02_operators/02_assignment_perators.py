# Project: Iris Measurement Tracker
# Dataset: Iris
# Source: UCI Machine Learning Repository — Iris Dataset
# What it represents: 150 real measurements of iris plants,
# with sepal length/width, petal length/width, and species.
import csv


# Level 1: building a small utility for analyzing plant measurements.
# Maintain a running total of sepal lengths.
# Update the total for each plant.
# After processing all 150 plants, display the total sepal length.

# Level 2: The plant researcher now wants to track two measurements while processing the same dataset.
# A running total for sepal width.
# Update that total for every record.
# Display the final sepal-width total alongside your existing sepal-length total.

# Level 3: The researcher now wants to track all four measurements in the Iris dataset.
# A running total for petal length.
# A running total for petal width.
# Update both totals while processing each record.
# Display the totals for all four measurements at the end.


file_name = 'iris.csv'

total_sepal_length = 0
total_sepal_width = 0
total_petal_length = 0
total_petal_width = 0

with open(file_name) as file:
    for line in file:
        line = line.strip()

        if not line:
            continue

        line = line.split(',')

        sepal_length = float(line[0])
        sepal_width = float(line[1])
        petal_length = float(line[2])
        petal_width = float(line[3])

        total_sepal_length += sepal_length
        total_sepal_width += sepal_width
        total_petal_length += petal_length
        total_petal_width += petal_width

print(f'Sepal length total: {total_sepal_length}')
print(f'Sepal width total: {total_sepal_width}')
print(f'Petal length total: {total_petal_length}')
print(f'Petal width total: {total_petal_width}')