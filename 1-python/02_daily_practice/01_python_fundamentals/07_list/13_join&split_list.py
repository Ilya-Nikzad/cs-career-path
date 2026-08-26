# PROJECT: Real Email Header Formatter

# Level 1: The team wants to create a cleaner display of the real email sender records.
# Read the real mbox-short.txt dataset.
# Find the message From lines.
# Extract the sender address from each line.
# For each sender, split the email address into:
# username
# domain
# Display each sender in this format: username | domain
# Example structure: stephen.marquard | uct.ac.za

# Level 2: The team now wants the formatter to handle the domain more clearly.
# Keep your existing sender extraction and formatting logic.
# Separate the domain into its individual parts using ..
# Rebuild the domain using " → " between its parts.
# Display the username and formatted domain using " | ".
# Example structure: stephen.marquard | uct → ac → za

# Level 3: The team now wants to make the email directory more useful by grouping senders by domain.
# Keep your existing email extraction and formatting logic.
# Create a collection of unique domains found in the real dataset.
# Preserve the order in which each domain first appears.
# Display each unique domain using " → " between its parts.
# Number the unique domains starting from 1.
# Use enumerate() for the numbering.
# Do not modify the original email data.


file_name = "mbox-short.txt"

with open(file_name) as f:
    domains = []

    for line in f:
        line = line.strip()

        if line.startswith("From "):
            email = line.split()[1]
            parts = email.split("@")
            username = parts[0]

            formatted_domain = parts[1].split(".")
            formatted_domain = " → ".join(formatted_domain)

            if formatted_domain not in domains:
                domains.append(formatted_domain)

for number, domain in enumerate(domains, start=1):
    print(f"{number}. {domain}")