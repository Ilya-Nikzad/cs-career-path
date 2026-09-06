# Project: Email Sender Analyzer
# Task: Extend the email-data utility you completed in the previous lesson.
# This version will help an analyst identify and classify senders using membership checks.

# Website: Python for Everybody Code Samples
# Dataset: mbox-short.txt
# Data: Real email messages from an open-source project development environment, including sender information.

# Create a collection of monitored senders.
# Check whether each available sender is monitored.
# Count monitored messages.
# Display the count.
# Keep previous functionality.

# Level 2 — Build
# Create a collection of trusted domains.
# Identify each sender's domain.
# Count trusted-domain messages.
# Count non-trusted-domain messages.
# Keep Level 1 functionality.

# Level 3 — Add
# Create a collection of excluded domains.
# Count messages from excluded domains.
# Add all results to the final report.
# Keep Levels 1–2 functionality.


file_name = "mbox-short.txt"

available = 0
missing = 0
dict_sender = {}

monitored_senders = {
    "stephen.marquard@uct.ac.za",
    "louis@media.berkeley.edu",
    "zqian@umich.edu"
}

monitor_counter = 0

trusted_domains = {
    "umich.edu",
    "iupui.edu",
    "uct.ac.za"
}

trusted_message_counter = 0
non_trusted_message_counter = 0

excluded_domains = {
    "gmail.com",
    "yahoo.com"
}

excluded_message_counter = 0

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

for key, value in dict_sender.items():
    if key in monitored_senders:
        monitor_counter += value

for key, value in dict_sender.items():
    domain = key.split("@")[1]

    if domain in trusted_domains:
        trusted_message_counter += value
    else:
        non_trusted_message_counter += value

    if domain in excluded_domains:
        excluded_message_counter += value

total_email = available + missing
percentage = (available / total_email) * 100
distinct_senders = len(dict_sender)

print("Sender available:", available)
print("Sender missing:", missing)
print("Sender dict sender:", dict_sender)
print("Total email:", total_email)
print("Percentage:", percentage)
print("Distinct senders:", distinct_senders)
print("Monitor counter:", monitor_counter)
print("Trusted messages:", trusted_message_counter)
print("Non-trusted messages:", non_trusted_message_counter)
print("Excluded messages:", excluded_message_counter)