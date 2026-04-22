# Easy:
# 1: Take name + age → print a sentence

name = "Hanna"
age = 21
print(f"Name: {name}.\nAge: {age}")

# 2: Take two numbers → print multiplication
first_name = 15
second_name = 5
total = first_name + second_name
print(f"Total: {total}")



#Medium:
# 1: Take age → print age + 10
sum_age = int(input("Please, enter your age: "))
print(f"After 5 yeas will be {sum_age + 5}")

# 2: Take 3 numbers → calculate average
first_num = int(input("Please, enter your average number: "))
second_num = int(input("Please, enter your average number: "))
third_num = int(input("Please, enter your average number: "))
total = first_num + second_num + third_num
average = total / 3
print(f"Average: {average}")



#Real (Interview level):
# 1: Take name,age,add 5 and if less than 18 print minor
real_name = input("Please, enter your name: ")
real_age = int(input("Please, enter your age: "))
if real_age < 18:
    print(f"{real_name} you are minor in 5 years will be {real_age + 5}")
else:
    print(f"{real_name} you are adult in 5 years will be {real_age + 5}")

#Mini Build: Take name,age,add 5, favorite color and print a summary:
name = input("Please, enter your name: ")
age = int(input("Please, enter your age: "))
favourite_number = input("Please, enter your favourite number: ")
add_age = age + 5
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Favourite number: {favourite_number}")
print(f"In 5 years: {add_age}")







