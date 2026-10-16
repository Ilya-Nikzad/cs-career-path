# Project: Customer Support Message Analyzer
# Client Request: A small online retailer receives customer-support messages through email and its website.
# Staff currently read each message manually to identify order references, contact details, and urgent requests.

# The support manager wants a small Python utility that analyzes the messages and produces a quick report.
# The utility should help staff identify which orders need attention and retrieve useful information without,
# manually searching every message.

# Data Source
# No external dataset is required.
# The sample messages are illustrative customer-support records created for this project.
# They provide realistic examples of repeated order references, contact information, urgent requests,
# duplicate references, and missing information.

# Business Rules
# The support manager has specified these requirements:
# 1. Order reference extraction: Identify order references that follow the format ORD- followed by exactly five digits,
# such as ORD-10482.
# 2. Contact extraction: Identify email-like strings in the messages so that staff can locate,
# customer contact information. These results do not need to guarantee that every address is a valid,
# deliverable email address.
# 3. Urgent-message identification: Determine whether the message batch contains messages that begin with URGENT!.
# A message mentioning urgency somewhere in the middle should not automatically qualify.
# 4. Refund-request identification: Find messages that end with the exact phrase Refund requested.
# This phrase is a business signal for the support team.
# 5. Repeated order references: The same order reference may appear in multiple messages.
# The manager wants to know which references occur more than once,
# because repeated reports could indicate an unresolved customer issue.
# 6. Missing order information: Some messages will not contain an order reference.
# These messages should be recognized as lacking that information rather than being assigned an invented reference.
# 7. Unexpected content: Messages may contain different names, numbers, punctuation, spacing, and email-like strings.
# The utility should not depend on the exact sample values remaining unchanged.

# Deliverable
# Create a working Python program that produces a readable Customer Support Analysis Report.
# The report should include:
# - All order references identified in the message batch.
# - All email-like contact strings identified.
# - The messages that meet the manager's urgency requirement.
# - The messages that end with the refund-request phrase.
# - Order references that appear repeatedly, along with their occurrence counts.
# - An indication of which messages do not contain an order reference.
# The report should make it easy for a support employee to identify potential priorities and,
# retrieve the information needed to follow up with customers.

# Testing expectations
# Before considering the utility complete, verify its behavior against these situations:
# - A message contains several numbers, but only one is a correctly formatted order reference.
# - An order reference appears twice in different messages.
# - A message contains no order reference.
# - An urgent word appears in the middle of a message rather than at the beginning.
# - A message mentions a refund but does not end with the required phrase.
# - A message contains more than one email-like string.
# - No email-like strings or order references are found.
# - An order reference has four digits or six digits instead of the required five.
# The program should distinguish matches that satisfy the client's rules from text that merely looks similar.


