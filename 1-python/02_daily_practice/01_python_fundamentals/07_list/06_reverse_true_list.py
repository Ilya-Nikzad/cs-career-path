# Task: Product Sales Report
# Level 1: Basic Version
# Store the product sales data.
# Create a report showing products ordered from highest sales to lowest sales.
# Display the original sales data as well.
# Display the best-selling product.
# Display the total number of products in the report.

sales = [45, 82, 31, 96, 67, 54, 73]
report = sorted(sales, reverse=True)
print(f"Report highest to lowest: {report}")
print(f"Original sales: {sales}")
print(f"Best sales: {report[0]}")
print(f"Total number of products: {len(sales)}")





# Level 2: intermediate
# Connect each product with its sales amount.
# Produce a report showing the products from highest-selling to lowest-selling.
# Keep the original product and sales data available.
# Make the report understandable to the shop manager.

products = ["Keyboard", "Mouse", "Monitor", "Headset", "Webcam", "Speaker", "USB Hub"]
sales = [45, 82, 31, 96, 67, 54, 73]
products_sales = zip(products, sales)

sales_high_to_low = sorted(products_sales,key= lambda pair:pair[1],reverse=True)
print("Report: Highest-selling to Lowest-selling")
for number, (product, sale) in enumerate(sales_high_to_low,start=1):
    #print(f"{product}. {sale}")
    print(f"{number}. {product} — {sale} sales")




# Level 3: Complete Version
# Expand your existing sales report to include each product's sales target.
# Keep the highest-selling products first.
# Identify which products are below their sales target.
# Identify which products met or exceeded their target.
# Keep the original data available.
# Make the final report useful enough for a manager to see both performance and products needing attention


products = [
    "Keyboard",
    "Mouse",
    "Monitor",
    "Headset",
    "Webcam",
    "Speaker",
    "USB Hub"
]

sales = [45, 82, 31, 96, 67, 54, 73]

targets = [50, 70, 40, 80, 60, 50, 75]

zip_data = zip(products, sales,targets)

sales_high_to_low = sorted(zip_data,key= lambda pair:pair[1],reverse=True)

for products, sales, targets in sales_high_to_low:
    if sales < targets:
        print(f"{products} sold {sales} against a target of {targets} → needs attention")

    else:
        print(f"{products} sold {sales} against a target of {targets} → target met.")

