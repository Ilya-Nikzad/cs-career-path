# `Identity Operators`
---

Identity operators check whether two variables refer to the same object, 

not merely whether they contain equal values.

is → same object

is not → different objects

== → same value

!= → different value

The most important real-world use is checking for None:

result = find_something()

if result is None:

    print("Nothing found")

For ordinary values such as numbers and strings, use == for equality.

Don't use is just because two values look the same.

if value == None:

---

# Important Rule — Identity Operators

is → checks object identity.

is not → checks that two references are not the same object.

== → checks value equality.

!= → checks value inequality.

Use is None to check whether a value represents no value / missing value.

Don't normally use is for ordinary number or string comparisons.

When a requirement says something like "check whether the value is absent", think about None and identity.

---