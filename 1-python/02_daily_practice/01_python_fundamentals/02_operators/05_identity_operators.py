# Project: Data Quality Checker
# Task: Task: Build a small utility that examines real email-archive data and identifies records,
# where an expected piece of information is unavailable,
# so a data analyst can distinguish usable records from records with missing values.
#
# Website: Python for Everybody Code Samples
# Dataset: mbox-short.txt
# Data: Real email activity from an open-source project development team.
# The dataset contains email messages and metadata such as senders, subjects,
# and spam-confidence information.

# Level 1: Build the foundation of the data-quality checker.
# Read through mbox-short.txt.
# Examine the email records and identify the sender information associated with each message.
# Store the sender information for processing.
# Represent a sender that is unavailable as None.
# Produce a summary showing:
# how many messages have sender information available
# how many messages have no sender information available
# Your program must distinguish a missing value from an ordinary value.

# Level 2: For messages with available sender information, count how many messages come from each sender.
# Ignore messages whose sender information is unavailable when producing the sender-frequency results.
# Display the sender counts so the analyst can see which senders appear most frequently.
# Keep the Level 1 missing-information summary.

# Level 3: Count the total number of messages.
# Calculate the percentage of messages that have sender information.
# Count how many different senders there are.
# Display these results as a clear report.

file_name = "mbox-short.txt"

available = 0
missing = 0
dict_sender = {}

with open(file_name) as f:
    for line in f:
        line = line.strip()

        if line.startswith("From "):
            parts = line.split()

            if len(parts) > 1:
                email = parts[1]
                available += 1
            else:
                email = None
                missing += 1

            if email is not None:
                if email in dict_sender:
                    dict_sender[email] += 1
                else:
                    dict_sender[email] = 1

total_email = available + missing
percentage = (available / total_email) * 100
distinct_senders = len(dict_sender)

print("Sender available:", available)
print("Sender missing:", missing)
print("Sender dict sender:", dict_sender)
print("Total email:", total_email)
print("Percentage:", percentage)
print("Distinct senders:", distinct_senders)
