person = {
    "name": "Hanna",
    "age": 20,
    "city": "New York",
}
#It controls what goes between values. Default: sep=" " space,sep="" nothing,sep="-" → dash
print("name:", person["name"], "\nage:", person["age"], "\ncity:", person["city"], sep="")

#Access value:
print(person["name"])
#Remove Value:
del person["city"]
# Add value:
person["city"] = "New York"

person = {
    "name": "Hanna",
    "age": 20,
    "city": "New York",
}

# 1: Loop for keys only
print("KEYS:")
for key in person:
    print(key)

print()

# 2: Loop for values only
print("VALUES:")
for value in person.values():
    print(value)

print()

# 3: Loop for both key and value
print("KEY-VALUES:")
for key, value in person.items():
    print(f"{key}:{value}")
