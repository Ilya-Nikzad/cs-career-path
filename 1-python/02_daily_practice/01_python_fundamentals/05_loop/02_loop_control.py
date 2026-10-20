# Project: Warehouse Stock Inspection Report
from functools import partial
from itertools import product
from statistics import quantiles

# Client Request
# A small electronics distributor wants a daily utility to inspect its warehouse stock records.
# The warehouse manager receives a list of products that were checked during the day.
# Some records are incomplete because the product scanner occasionally fails to capture a quantity.
# The manager wants a report that identifies products requiring attention,
# while ignoring records that cannot currently be evaluated.

# Data Source
# The records represent a simplified warehouse stock-check export supplied by the client.

# Business Rules
# The warehouse manager has established these operational rules:
# - A product with 0 units is considered out of stock and requires immediate attention.
# - A product with 1–5 units is considered critically low.
# - A product with more than 5 units does not require stock-level attention today.
# - A record with missing quantity cannot be evaluated and should be excluded from stock-level calculations.
# - Once the report has identified all out-of-stock products, it does not need to search for additional out-of-stock information for that particular inspection.
# - Products with valid quantities must still be considered for the other stock categories.
# - The report must distinguish between an unavailable quantity and a genuine quantity of 0.

# Deliverable
# Produce a Warehouse Stock Inspection Report containing:
# - total number of valid stock records
# - number of records excluded because their quantity is missing
# - list of out-of-stock products
# - list of critically low products
# - number of products with more than 5 units
# - total units represented by valid stock records

# Testing expectations
# Test the program against the supplied records and pay particular attention to:
# - the difference between missing quantity and 0
# - the boundary between 5 and 6
# - whether out-of-stock products are identified correctly
# - whether excluded records affect the valid-stock totals
# - whether the final counts reconcile with the supplied records

#BEGIN

file_name = "02_warehouse_stock"

valid_products = {}
none_valid_products = {}
out_stock = {}
critical_stock = {}
products_over_five = {}

with open(file_name, encoding="utf-8") as file_handle:
    for line in file_handle:
        line = line.strip()
        parts = line.split("—")

        product = parts[0].strip()
        quantity = parts[1].strip()

        if quantity.isdigit():
            quantity = int(quantity)
            valid_products[product] = quantity

            if quantity == 0:
                out_stock[product] = quantity
            elif quantity <= 5:
                critical_stock[product] = quantity
            else:
                products_over_five[product] = quantity
        else:
            none_valid_products[product] = quantity

total_units = 0

for product in valid_products:
    total_units += valid_products[product]

print("Valid stock records:", len(valid_products))
print("Missing quantity records:", len(none_valid_products))
print("Out of stock products:", list(out_stock))
print("Critically low products:", list(critical_stock))
print("Products with more than 5 units:", len(products_over_five))
print("Total valid units:", total_units)
print("Records not evaluated:", list(none_valid_products))
