# Task: Daily Task Manager

# Level 1: Basic Version
# Store the current tasks in a list.
# Support the addition of new individual tasks during the day.
# Display the updated task list.
# Display how many tasks are currently planned.

tasks = [
    "study Python",
    "finish homework",
    "clean desk"
]

tasks.append("review notes")
tasks.append("practice exercises")
print("Task list:", tasks)
print("Number of tasks:", len(tasks))



# Level 2: Intermediate Version
# Keep the existing task list.
# Add the teacher's new tasks to the student's task list.
# Make sure each new task becomes an individual task in the list.
# Display the complete updated task list.
# Display the total number of tasks.
# Keep the original task order.
teacher_tasks = [
    "read chapter 3",
    "complete quiz",
    "submit assignment"
]
tasks.extend(teacher_tasks)
print("Complete task update:", tasks)
print("Number of tasks:", len(tasks))


# Level 3: Complete Version
# Start with the student's existing tasks.
# Add the individual tasks received during the day.
# Add the teacher's batch of tasks.
# The student decides that one existing task is no longer needed.
# The student also wants to know which task is currently next to work on.
# Display the final task list.
# Display the total number of remaining tasks.
# Display the task the student should work on next.

tasks = [
    "study Python",
    "finish homework",
    "clean desk"
]

teacher_tasks = [
    "read chapter 3",
    "complete quiz",
    "submit assignment"
]
tasks.append("review notes")
tasks.append("practice exercises")