# Project: Sales Revenue Calculator
# Dataset: Online Retail
# Source: UCI Machine Learning Repository
# What it represents: real transactional records from a UK-based online retail business,
# including quantities and unit prices.
# Level 1: The business wants a small utility that calculates the revenue,
# for individual transactions.
# For each selected transaction:
# Get its Quantity.
# Get its UnitPrice.
# Calculate the transaction's revenue.
# Display the quantity, unit price, and calculated revenue.
# Calculate the combined revenue of the selected transactions.

# Level 2: The business now wants to calculate the average revenue per transaction.
# Keep your existing revenue calculation.
# Calculate the average revenue from the Revenue column.
# Display the average revenue.


# Level 3: The business now wants to identify profitable vs. unprofitable transactions.
# Create the AboveAverage column.
# Compare each Revenue value with average_revenue.
# Store True/False in AboveAverage.
# Display the transaction number, Revenue, and AboveAverage.
# Count how many transactions have AboveAverage == True.



# It reads the Excel file, converts it to CSV format,
# and saves it without the Pandas row index with one time run it
# After that we don't need this statements
#import pandas as pd
#data_frame = pd.read_excel("online retail.xlsx").to_csv("online retail.csv",index=False)


# Read the CSV file
file_name = "Online Retail.csv"

with open(file_name, "r") as f:
    next(f)

    revenue_list = []
    above_average = []

    for line in f:
        line = line.strip()
        line = line.split(",")

        quantity = int(line[-5])
        print(f"Quantity: {quantity}")

        unit_price = float(line[-3])
        print(f"Unit Price: {unit_price}")

        revenue = quantity * unit_price
        print(f"Revenue: {revenue}")

        revenue_list.append(revenue)

# Calculate combined revenue
total_revenue = 0

for revenue in revenue_list:
    total_revenue += revenue

# Calculate average revenue
average_revenue = total_revenue / len(revenue_list)

# Determine which transactions are above average
for revenue in revenue_list:
    if revenue > average_revenue:
        above_average.append(True)
        print(f"Above Average: {revenue}, True")
    else:
        above_average.append(False)

# Count transactions above average
count_above_average = 0

for result in above_average:
    if result == True:
        count_above_average += 1

# Display results
print(f"Average Revenue: {average_revenue}")
print(f"Combined Revenue: {total_revenue}")
print(f"Transactions Above Average: {count_above_average}")




