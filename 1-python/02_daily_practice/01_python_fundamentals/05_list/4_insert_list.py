# Task: Customer Queue Manager
# Level 1:  Basic Version:
# Store the current customer queue.
# Support adding a customer who needs a specific place in the queue.
# Keep the existing customers in their correct relative order.
# Display the updated queue.
# Make the result useful for a staff member who needs to know who is waiting and in what order.

queue = ["Ali", "Sara", "John", "Maya"]
queue.insert(1, "David")
print(queue)
for number, customer in enumerate(queue,start=1):
    if 11 <= number % 100 <= 13:
        suffix = "th"
    elif number % 10 == 1:
        suffix = "st"
    elif number % 10 == 2:
        suffix = "nd"
    elif number % 10 == 3:
        suffix = "rd"
    else:
        suffix = "th"
    print(f"{str(number)}{suffix}: {customer}")



# Level 1: Intermediate
# Keep the current customer queue.
# Add Fatima directly before Maya.
# Add Kevin to the end of the queue.
# Display the updated queue.
# Display each customer with their current position.

queue = ["Ali", "Sara", "David", "John", "Maya"]

priority_customer = "Fatima"
normal_customer = "Kevin"
queue.insert(-1, priority_customer)
queue.append(normal_customer)
print(queue)
for position, customer in enumerate(queue,start=1):
    if 11 <= position % 100 <= 13:
        suffix = "th"
    elif position % 10 == 1:
        suffix = "st"
    elif position % 10 == 2:
        suffix = "nd"
    elif position % 10 == 3:
        suffix = "rd"
    else:
        suffix = "th"
    print(f"{position}{suffix}. {customer.upper()}")




# Level 3: Complete Version
# The customer currently at the front is served and leaves the queue.
# David cancels and leaves the queue before being served.
# A new appointment customer, "Nora", must be placed directly before "John".
# Two walk-in customers, "Omar" and "Lina", arrive and join the queue.
# Your existing queue-position system should continue to work with the updated queue.

queue = ["Ali", "Sara", "David", "Fatima", "John", "Maya", "Kevin"]

appointment_customer = "Nora"
walk_in_customers = ["Omar", "Lina"]
cancelling_customer = "David"

queue.pop(0)
queue.remove(cancelling_customer)
queue.insert(2, appointment_customer)
queue.extend(walk_in_customers)
for position , customer in enumerate(queue, start=1):
    if 11 <= position % 100 <= 13:
        suffix = "th"
    elif position % 10 == 1:
        suffix = "st"
    elif position % 10 == 2:
        suffix = "nd"
    elif position % 10 == 3:
        suffix = "rd"
    else:
        suffix = "th"
    print(f"{position}{suffix}. {customer.upper()}")