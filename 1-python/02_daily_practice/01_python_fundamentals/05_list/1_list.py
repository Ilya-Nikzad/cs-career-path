# Task 1: A collection of tasks.
# A task that is no longer needed.
# A task whose wording needs correcting.
# Checking a particular task by its position.
tasks = ["study Python", "finish homework", "clean desk"]
tasks.remove("clean desk")
tasks[1] = "finish math homework"
#print(tasks[0])
#print(tasks)


# Task 1:The student now wants the task manager to handle a busier day.
# "clean desk" is cancelled.
# "finish homework" becomes "finish math homework".
# A new task called "review notes" needs to be added.
# The student wants to know what the second task is after all these changes.
# Finally, the program should display the updated task list.

tasks = ["study Python", "finish homework", "clean desk"]
tasks.remove("clean desk")
tasks[1] = "finish math homework"
tasks.append("review notes")
#print(tasks[1])
#print(tasks)



# Task 3: The student now wants to make the task manager more useful.
# "clean desk" is cancelled.
# "finish homework" becomes "finish math homework".
# "review notes" needs to be added.
# The student also remembers another task: "practice exercises".
# The student wants to check the first task and the last task.
# The program should display the final number of tasks as well as the complete list.

tasks = ["study Python", "finish homework", "clean desk"]
tasks.remove("clean desk")
tasks[1] = "finish math homework"
tasks.append("review notes")
tasks.insert(-1, "practice exercises")
print(f"First : {tasks[0]} Last : {tasks[-1]}")
print(f"Total tasks: {len(tasks)} Task list: {tasks}")




