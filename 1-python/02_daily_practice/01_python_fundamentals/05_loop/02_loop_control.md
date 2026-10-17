# Loop Control

## Core Idea

Loop control lets you change what happens during repetition.

Instead of allowing a loop to always process every iteration normally, Python gives you ways to:
- stop the loop early with break
- skip the current iteration with continue
- intentionally do nothing with pass

The key distinction is:
- break = leave the loop
- continue = skip this iteration
- pass = do nothing here
---

## 1. break

break immediately terminates the loop containing it.

```
for number in range(10):
    if number == 5:
        break

    print(number)
```
When number becomes 5, break ends the loop.

When is break useful?

It is particularly useful when you have found what you're looking for or when continuing the loop is no longer necessary.
```
names = ["Ali", "Sara", "John", "Maya"]

for name in names:
    if name == "John":
        print("Found")
        break
```

Important behavior: break only affects the loop it is directly inside.

With nested loops, this matters:
```
for x in range(3):
    for y in range(3):
        if y == 1:
            break
        print(x,y)
```
---
## 2. continue

continue skips the rest of the current iteration and moves to the next iteration.
```
for number in range(6):
    if number == 3:
        continue

    print(number)
```
The iteration where number is 3 is skipped.

---
## 3. pass

pass means: Do nothing.
```
for number in range(5):
    if number == 2:
        pass

    print(number)
```
Why does pass exist?

In Python, a block needs code inside it, and the code must be indented. if empty will case error

It can therefore be useful when you deliberately want a block to have no action yet.

---
## Loop Control Inside while

break, continue, and pass work the same in both for and while loops. However,

continue in a while loop can cause an infinite loop if the loop variable isn't updated.

```
number = 1

while number <= 5:
    if number == 3:
        print("Still running...")
        continue

    print(number)
    number += 1
```
This is problematic because when number becomes 3, the continue happens before number += 1.

The value never changes, so the loop continues indefinitely, repeatedly printing "Still running...".

This is one reason continue requires extra care with while loops.

---
## Important Rules
- break immediately exits the nearest enclosing loop.
- continue skips the remainder of the current iteration.
- continue then moves toward the next iteration.
- pass performs no action.
- pass does not stop or skip a loop.
- break and continue can be used with both for and while.
- In nested loops, break affects the nearest enclosing loop.
- Be especially careful with continue inside while loops so the loop can still make progress.