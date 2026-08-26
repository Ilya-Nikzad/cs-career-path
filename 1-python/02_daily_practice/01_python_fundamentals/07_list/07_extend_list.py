#Level 1: Basic Version
# Start with the team's existing task list.
# Add the tasks received from the morning planning meeting.
# Keep all tasks in their existing order.
# Display the consolidated task list.
# Display the total number of tasks

team_tasks = [
    "Fix login bug",
    "Update documentation",
    "Review pull request"
]

morning_tasks = [
    "Prepare test data",
    "Check server logs",
    "Update project board"
]

team_tasks.extend(morning_tasks)
print(f"Consolidated tasks: {team_tasks}")
print(f"Total number of tasks: {len(team_tasks)}")


# level 2: intermediate
# Integrate the afternoon tasks into the existing consolidated task list.
# Preserve the order in which task groups were received:
# Existing team tasks
# Morning tasks
# Afternoon tasks
# The consolidated list should contain every task exactly once.
# The task count should automatically reflect the expanded list.

afternoon_tasks = [
    "Test payment system",
    "Review error reports",
    "Prepare deployment notes"
]

team_tasks.extend(afternoon_tasks)
print(f"Consolidated tasks: {team_tasks}")
print(f"Total number of tasks: {len(team_tasks)}")


# level 3: Complete Version
# Integrate the department's tasks into the existing consolidated task list.
# Integrate the urgent tasks as a separate incoming batch.
# Preserve the order within each incoming batch.
# The final task list should contain every task from the project so far.
# The system should continue to report the correct total number of tasks.
# The final result should make it clear which tasks are currently
# in the team's consolidated workload.

department_tasks = [
    "Review security settings",
    "Check database backups",
    "Update API documentation"
]

urgent_tasks = [
    "Fix production outage",
    "Investigate failed payments"
]

team_tasks.extend(department_tasks)
team_tasks.extend(urgent_tasks)
print(f"Consolidated tasks: {team_tasks}")
print(f"Total number of tasks: {len(team_tasks)}")