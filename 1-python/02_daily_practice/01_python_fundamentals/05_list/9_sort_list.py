# Task: Employee Performance Report

# level 1: Basic Version
# Store the employee performance data.
# Create a separate ranking from highest score to lowest score.
# Keep the original performance data unchanged.
# Display the original data.
# Display the ranked report.
# Display the highest-performing employee.

employees = [
    ("Ali", 78),
    ("Sara", 95),
    ("John", 84),
    ("Maya", 91),
    ("David", 73)
]

ranking_score = sorted(employees, key=lambda x: x[1], reverse=True)
#print(f"Employee Data: {employees}")
#print(f"Ranking Score: {ranking_score}")
#print(f"Highest-performing employee: {ranking_score[0][0]} — {ranking_score[0][1]}")


# level 2: Intermediate Version
# Continue using the existing employee ranking.
# Identify employees who meet or exceed the passing score.
# Identify employees who are below the passing score.
# Keep both groups in the same highest-to-lowest performance order.
# Display the two groups clearly for management.
# Keep the original employees data unchanged.

passing_score = 80

meeting_passing = []
below_passing = []

for employee, score in ranking_score:
    if score >= passing_score:
        meeting_passing.append((employee, score))
    else:
        below_passing.append((employee, score))

print(f"Meeting or exceeding 80:")
for employee, score in meeting_passing:
    print(f"{employee} — {score}")

print("\nBelow 80:")
for employee, score in below_passing:
    print(f"{employee} — {score}")


# level 3: Complete Version
# Continue using your existing ranked employee data.
# Keep the meeting-passing and below-passing groups from Level 2.
# Identify the high-performing employees within the existing ranking.
# Display the high-performing employees separately.
# Display each employee's rank in the overall ranking.
# Keep the original employees list unchanged.
# Preserve highest-to-lowest order in every report.

high_performers = []

for employee, score in ranking_score:
    if score >= 90:
        high_performers.append((employee, score))

print("High-performing employees:")

for rank, (employee, score) in enumerate(ranking_score, start=1):
    if score >= 90:
        print(f"Rank {rank}: {employee} — {score}")