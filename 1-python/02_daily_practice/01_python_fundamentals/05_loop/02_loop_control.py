# Project: Warehouse Stock Inspection Report

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