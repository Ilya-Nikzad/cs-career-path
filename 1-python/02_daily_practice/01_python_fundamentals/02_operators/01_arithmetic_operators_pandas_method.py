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


# Pandas is a tool for organizing, manipulating, and analyzing data in Python.
import pandas as pd

# .xlsx = a file format used to store Excel spreadsheets and tabular data
data_frame = pd.read_excel("online retail.xlsx")

quantity = data_frame["Quantity"]
unit_price = data_frame["UnitPrice"]

# Calculate revenue for each transaction
data_frame["Revenue"] = quantity * unit_price

# Calculate total and average revenue
total_revenue = data_frame["Revenue"].sum()
average_revenue = data_frame["Revenue"].mean()

# Determine which transactions are above average
data_frame["AboveAverage"] = data_frame["Revenue"] > average_revenue

# Count transactions above average
count_above_average = data_frame["AboveAverage"].sum()

# Display results
print(data_frame[["InvoiceNo", "Revenue", "AboveAverage"]].head())
print(f"Transactions Above Average: {count_above_average}")
print(f"Average Revenue: {average_revenue}")
print(f"Combined Revenue: {total_revenue}")