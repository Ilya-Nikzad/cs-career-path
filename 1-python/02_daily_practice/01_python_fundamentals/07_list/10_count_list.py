# PROJECT: Email Sender Activity Tracker
# Level: Basic Version
# Use the real mbox-short.txt file.
# Your task is to create a list of sender addresses from the message From lines,
# then use count() to determine how many messages were sent by:
# stephen.marquard@uct.ac.za

file_name = "mbox-short.txt"
with open(file_name) as file:
    emails = []
    for line in file:
        if line.startswith("From "):
            if "@" in line:
                emails.append(line.split()[1])
count_1 = emails.count("stephen.marquard@uct.ac.za")
#print(count_1)


# Level 2: Intermediate Version
# Continue from your existing project.
# The support team now wants to compare two real senders from the dataset.
# Use these two senders:
# stephen.marquard@uct.ac.za
# louis@media.berkeley.edu
# Keep your existing emails list.
# Count how many messages came from each sender.
# Display both sender counts.
# Determine which of the two senders sent more messages.
# Keep using count() for the occurrence counts.
# Do not modify the original emails list.


count_2 = emails.count("louis@media.berkeley.edu")
print(f"stephen message count: {count_1}")
print(f"louis message count: {count_2}")
if count_1 > count_2:
    print("Stephen sent more messages.")
elif count_2 > count_1:
    print("louis sent more messages.")
else:
    print("Both sent the same number of messages.")

#Level 3: Complete Version
# The team now wants a broader comparison.
# Instead of manually checking only two senders,
# create a report for three real senders from the same dataset.Use:
#
# stephen.marquard@uct.ac.za
# louis@media.berkeley.edu
# ray@media.berkeley.edu
# Continue using your existing emails list.
# Count the messages for all three senders using count().
# Store the sender/count information so it can be displayed as a report.
# Display each sender and their message count.
# Identify the sender with the highest message count.
# Keep the original emails list unchanged.
# Do not manually assume which sender has the highest count—the program must determine it from the data.

senders = ["stephen.marquard@uct.ac.za",
"louis@media.berkeley.edu",
"ray@media.berkeley.edu"]
sender_counts = []
for sender in senders:
    count = emails.count(sender)
    sender_counts.append((sender,count))
print("Sender Report:")

for sender, count in sender_counts:
    print(f"{sender}: {count} messages")

highest_sender = None
highest_count = 0

for sender, count in sender_counts:
    if count > highest_count:
        highest_count = count
        highest_sender = sender

print(f"\nHighest message count: {highest_sender} — {highest_count} messages")




