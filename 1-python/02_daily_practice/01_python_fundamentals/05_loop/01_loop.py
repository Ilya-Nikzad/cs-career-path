# Project: Customer Order Processing Report

# Client Request
# A small online business currently reviews its customer orders manually at the end of each day.
# The owner wants a simple Python utility that processes the day's order records and produces a useful daily report.
# The business needs to know how many orders were received, the total value of the orders,
# and which orders require attention based on their value.

# Data Source:
# customer_data file
# The order records represent a realistic small-business daily order

# Business Rules
# The finished utility should:
# Process every order in the day's records.
# Determine the total number of orders.
# Determine the total sales value.
# Identify orders with a value of RM150 or more.
# Identify orders below RM50.
# Determine the highest-value order.
# Determine the lowest-value order.
# Calculate the average order value.
# Ensure every order is accounted for in the final calculations.
# Treat an order worth exactly RM150 as high-value.
# Treat an order worth exactly RM50 as not belonging to the below-RM50 group.

# Deliverable:
# total number of orders
# total sales
# average order value
# highest-value order and its customer
# lowest-value order and its customer
# list of high-value orders
# list of orders below RM50
#
# The report should make it easy for the business owner to understand the day's,
# sales activity without inspecting every raw order individually.

# Testing expectations
# Test the program against the supplied data and pay particular attention to:
# the RM150 boundary
# the RM50 boundary
# the highest and lowest order
# whether the total number of processed orders matches the input
# whether the reported total sales accounts for every order


file_name = "customer_data"

count_order = 0
total_sale = 0
high_sales_list = []
low_sales_list = []
highest_sale = 0
lowest_sale = 0
highest_value_customer = None
lowest_value_customer = None


with open(file_name,encoding="utf8") as file:
    for line in file:
        line = line.strip()

        # Parsing
        parts = line.split("—")

        count_order += 1

        value = float(parts[3])
        total_sale += value

        if value >= 150:
            high_sales_list.append(value)
        elif value < 50:
            low_sales_list.append(value)

        if value > highest_sale:
            highest_sale = value
            highest_value_customer = parts[1]
        elif lowest_sale == 0 or value < lowest_sale:
            lowest_sale = value
            lowest_value_customer = parts[1]

average_sale = total_sale / count_order

print(f"Total Orders: {count_order}")
print(f"Total Sales: RM {total_sale}")
print(f"Average Sales: RM {average_sale}")
print(f"Highest-Value Customer: {highest_value_customer} — Highest Sales: RM {highest_sale}")
print(f"Lowest-Value Customer: {lowest_value_customer} — Lowest Sales: RM {lowest_sale}")
print(f"High Sales (Above RM 150): {high_sales_list}")
print(f"Low Sales (Below RM 50): {low_sales_list}")





