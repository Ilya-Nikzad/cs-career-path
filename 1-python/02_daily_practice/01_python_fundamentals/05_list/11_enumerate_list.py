# ============================================================
# PROJECT: Email Sender Directory
# Level 1: Basic
# - Read the dataset
# - Extract sender addresses
# - Store them in emails
# - Display senders with enumerate()
# - Start numbering from 1
# - Preserve original order


# level 2: intermediate
# - Display senders in uppercase
# - Display total sender records
# - Keep emails unchanged

# Level 3: Complete version
# - Find unique senders
# - Count unique senders
# - Display unique senders with enumerate()
# - Preserve first-appearance order

file_name = "mbox-short.txt"

with open(file_name) as file:
    emails = []

    for line in file:
        line = line.strip()

        if line.startswith("From "):
            emails.append(line.split()[1])


# Sender directory
for index, email in enumerate(emails, start=1):
    print(f"{index}. {email.upper()}")

print(f"Total emails: {len(emails)}")


# Unique senders
unique_emails = []

for email in emails:
    if email not in unique_emails:
        unique_emails.append(email)

print(f"Unique senders: {len(unique_emails)}")

for index, email in enumerate(unique_emails, start=1):
    print(f"{index}. {email.upper()}")