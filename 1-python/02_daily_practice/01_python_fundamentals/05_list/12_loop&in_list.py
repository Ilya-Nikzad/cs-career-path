# Project: Real Email Sender Filter
# Level 1: The team wants to identify messages sent by members of a specific monitoring group.
# Use these real sender addresses:
# stephen.marquard@uct.ac.za
# louis@media.berkeley.edu
# Read the real mbox-short.txt dataset.
# Extract sender addresses from the message From lines.
# Store the sender addresses in a list.
# Loop through the sender list.
# Check whether each sender is in the monitoring group.
# Display only the matching senders.
# Preserve the original sender order.


# level 2: The team now wants to check multiple sender groups.
# Add a second group called priority_group.
# Put these real senders in it:
# ray@media.berkeley.edu
# cwen@iupui.edu
# Loop through the existing sender_list.
# Identify whether each sender belongs to the monitoring group or the priority group.
# Display the sender together with the group they belong to.
# Ignore senders who belong to neither group.
# Preserve the original sender order

# Level 3: If a sender belongs to neither group, classify them as Other.

file_name = "mbox-short.txt"
with open(file_name) as f:
    sender_list = []
    for line in f:
        line = line.rstrip()
        if line.startswith("From "):
            sender_list.append(line.split()[1])
monitoring_group = [
    "stephen.marquard@uct.ac.za",
    "louis@media.berkeley.edu"
]
priority_group = ["ray@media.berkeley.edu"
,"cwen@iupui.edu"]
for sender in sender_list:
    if sender in priority_group:
        print(f"Priority: {sender}")
    elif sender in monitoring_group:
        print(f"Monitoring: {sender}")
    else:
        print(f"other: {sender}")
