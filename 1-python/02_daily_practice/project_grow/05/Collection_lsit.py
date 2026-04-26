# Task 1: Create a list of 5 numbers and print each one using a loop.
list_num = [12,4,6,25,6]
result = ",".join(map(str, list_num))
print(result)

# Task 2: Create a list of names. add a new name remove one name print final list
name_list = ["apple","mango","grape"]
name_list.remove("grape")
name_list.append("orange")
print(",".join(name_list))

# Task 3: Find sum of a list using loop.
count = 0
list_num = [12, 4, 6, 25, 6]
for item in list_num:
    print("current", count, "+", item)
    count += item
print("Final answer =", count)

# Task 4: Find the maximum number in a list (without using max())
list_num = [12, 4, 6, 25, 6]
maximum = 0
for item in list_num:
    if maximum < item:
        maximum = item
print (maximum)

# Task 5:Task 5 (REAL SYSTEM THINKING) Create a Task List system:
# list of tasks,add new task,remove completed task print all tasks
workout_list = ["Tomorrow is rest","Today is leg exersice","Shoulder exersice","Chest exersice","Take vitamins"]
print ("Previous Task:",','.join(workout_list))
workout_list.append("Tomorrow is shoulder day")
workout_list.remove("Tomorrow is rest")
print ("Added task: Tomorrow is shoulder day")
print ("Removed task: Tomorrow is rest")
print (",".join(workout_list))
