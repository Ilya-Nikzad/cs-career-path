# Task: Customer Service Queue

# level 1: Basic Version
# Start with the current customer queue.
# Process the customer who is currently at the front.
# Keep the processed customer's name so it can be recorded.
# Display the customer who was served.
# Display the remaining queue.
# Display the number of customers still waiting.

queue = [
    "Ali",
    "Sara",
    "John",
    "Maya",
    "David"
]

customer_info = []
customer = queue.pop(0)
customer_info.append(customer)
#print(f"Served customer info: {customer}")
#print(f"Remaining queue: {queue}")
#print(f"Total remaining: {len(queue)}")


# level 2: intermediate
# Continue the same customer-service system.
# Process the next two customers from the queue.
# Keep a record of every customer served so far.
# Display the complete served-customer record.
# Display the customers still waiting.
# Display the number of customers remaining.
# Preserve the original waiting order.

customer = queue.pop(0)
customer_info.append(customer)

customer = queue.pop(0)
customer_info.append(customer)

print(f"Served customer info: {customer_info}")
print(f"Remaining queue: {queue}")
print(f"Total remaining: {len(queue)}")


# level 3: Complete Version
# Add the priority customers to the existing service system.
# Priority customers must be served before the customers currently waiting.
# Process the priority customers.
# Add each served priority customer to the existing served record.
# Display the complete served-customer record.
# Display the remaining queue.
# Display the number of customers still waiting.
# Preserve the order of the priority customers.

priority_customers = [
    "Lina",
    "Omar"
]

queue[0:0] = priority_customers
customer = queue.pop(0)
customer_info.append(customer)

customer = queue.pop(0)
customer_info.append(customer)
print(f"Served customer info: {customer_info}")
print(f"Remaining queue: {queue}")
print(f"Total remaining: {len(queue)}")