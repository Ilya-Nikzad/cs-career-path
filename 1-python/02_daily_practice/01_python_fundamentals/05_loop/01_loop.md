# What Are Loops?
---

`Core Idea`: A loop lets a program repeat an action without you writing the same code again and again.

Instead of manually processing one item at a time, you describe what should happen repeatedly,

and Python handles the repetition. The two main loop types are for and while.

1. `for loop`: A for loop is useful when you want to process items one at a time from something you can go through,

such as a list or a string.

Like : fruits = ["apple", "banana", "orange"]

for fruit in fruits:

`When is for useful?`: Whenever you have a collection of items and want to perform an action for each item.

Important idea: The variable after for represents the current item.

2. `while Loops`: A while loop repeats as long as a condition remains True.

like: number = 1

while number <= 5:

Once number becomes 6, the condition is false and the loop stops.

`When is while useful?`

A while loop is useful when repetition depends on a condition,

rather than simply going through every item in a sequence.

For example, you might repeatedly ask for information until a condition is satisfied.

3. `for vs while`

for:

Goes through items, Common for sequences, Often has a known set of items

while: 

Repeats while a condition is true, Common for condition-based repetition, Number of repetitions may depend on what happens

4. `range()`: It produces a sequence of numbers that can commonly be used with for.

like: for number in range(5):

Notice that 5 isn't included.

Starting and stopping: You can specify a starting value and a stopping value:

like: for number in range(2, 6):

Adding a step: You can also specify how much the number changes each time:

for number in range(0, 10, 2):

5. `Looping Through Sequences`: Python allows you to loop through different kinds of sequences.

Like: List, Strings Other sequences

The important general idea is that a for loop can take items from a sequence one at a time.

6. `Looping Through Numbers vs Looping Through Items`:

Use a list loop when you want to work with the things in a list.

Use range() when you want to repeat something a certain number of times.

7. `The Indented Block`:

The code belonging to a loop is determined by indentation.

Like: for number in range(3):
          print(number)
          print("Processing")

Both print() statements run during every iteration.

---

# Important Rules

for loops process items from a sequence or iterable.

while loops continue while their condition is True.

range() generates a sequence of numbers.

range(start, stop) includes start but excludes stop.

range(start, stop, step) controls the starting point, ending boundary, and increment.

A for loop can process items directly without manually accessing their positions.

Indentation determines which statements belong to a loop.

Choose the loop based on the problem, not simply because one loop is newer or easier.