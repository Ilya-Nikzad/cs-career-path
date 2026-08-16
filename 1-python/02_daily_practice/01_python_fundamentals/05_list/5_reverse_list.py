# Task: Support Ticket Review Queue
# It uses a stack (LIFO) the most recent ticket is reviewed first.

# Level 1: Basic Version
# Store the day's support tickets in a list.
# Change the review order so the newest ticket is reviewed first.
# Display the review queue.
# Display how many tickets need to be reviewed.

tickets = [
    "Login problem",
    "Payment failed",
    "Password reset",
    "Account locked",
    "Missing invoice"
]

review_order = tickets[::-1]

#print("Review queue:", review_order)
#print("Number of tickets:", len(review_order))



# Level 2: intermediate
# Integrate the newly received tickets into the existing ticket data.
# The support team must still be able to review the newest ticket first.
# The original arrival data must remain available because the manager uses it for the end-of-day report.
# The final program should clearly show the updated data and the review order.

new_tickets = [
    "Two-factor authentication issue",
    "Refund request"
]

tickets.extend(new_tickets)

review_order = tickets[::-1]

#print("Arrival order:", tickets)
#print("Review queue:", review_order)
#print("Number of tickets:", len(review_order))


# Level 3: Complete Version
# Integrate the urgent-ticket information into the existing system.
# Produce a final review queue where urgent tickets are handled before non-urgent tickets.
# Within each group, preserve the appropriate existing order.
# Keep the original arrival data available for reporting.
# Display the final review queue clearly.
# Make sure the system still works if there are no urgent tickets.

urgent_tickets = ["Account locked", "Refund request" ]

urgent = []
non_urgent = []
for ticket in tickets:
    if ticket in urgent_tickets:
        urgent.append(ticket)
    else:
        non_urgent.append(ticket)
urgent.reverse()
non_urgent.reverse()
review_order = urgent + non_urgent
print("Arrival order:", tickets)
print("Final review queue:", review_order)
print("Number of tickets:", len(review_order))

