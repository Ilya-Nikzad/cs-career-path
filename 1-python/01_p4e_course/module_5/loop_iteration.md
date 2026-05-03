## Loop Iteration (Module 7)

Loop iteration is used to repeat a set of instructions multiple times without writing the same code repeatedly.  
Loops make programs more efficient, cleaner, and easier to manage.

Python mainly uses two types of loops:

- **for loop**
- **while loop**

---

## `for` Loop

A **for loop** is used when the number of iterations is known or when looping through a fixed range or collection of items.

### Best Used For
- Repeating actions a specific number of times
- Iterating through lists, strings, tuples, or ranges
- Processing each item in a sequence

### Characteristics
- Runs through a sequence step by step
- Stops automatically when the sequence ends
- Easier to read for fixed repetition tasks
- Lower risk of creating an infinite loop

### Advantages
- Simple and clean structure
- Good for predictable repetition
- Commonly used in data processing and iteration tasks

---

## `while` Loop

A **while loop** is used when repetition depends on a condition rather than a fixed number of iterations.

The loop continues running as long as the condition remains true.

### Best Used For
- Repeating until a condition changes
- User input validation
- Menu-driven programs
- Situations where the number of repetitions is unknown

### Characteristics
- Controlled by a condition
- Continues until the condition becomes false
- Requires manual updates to avoid endless repetition
- More flexible than a for loop

### Advantages
- Useful when iteration count is not predictable
- Allows dynamic repetition based on program logic
- Common in interactive programs

---

## Difference Between `for` Loop and `while` Loop

### Iteration Type
- **for loop** → Used for fixed or known repetition
- **while loop** → Used for condition-based repetition

### Control Method
- **for loop** → Controlled by a sequence or range
- **while loop** → Controlled by a boolean condition

### Number of Repetitions
- **for loop** → Usually known before the loop starts
- **while loop** → Usually unknown and depends on a condition

### Ease of Use
- **for loop** → Easier for predictable looping tasks
- **while loop** → Better for flexible looping situations

### Infinite Loop Risk
- **for loop** → Lower risk because it stops automatically
- **while loop** → Higher risk if the condition never changes

---

## Quick Comparison

- **for loop** → used when the number of iterations is known or fixed.
- **while loop** → used when repetition depends on a condition.
- **for loop** is simpler for counting or iterating through items.
- **while loop** is better for condition-controlled repetition.

---

## Summary

Loops help automate repetitive tasks in programming.

- Use a **for loop** when repetition count is predictable.
- Use a **while loop** when repetition depends on a condition.
- Choosing the correct loop improves readability and efficiency.

# Notes: Difference Between `while` and `while True`

- `while condition` runs only when a condition is `True`
- Stops automatically when the condition becomes `False`
- Safer and easier to understand
- Best when the stopping condition is known

- `while True` runs forever
- Must use `break` to stop the loop
- More flexible
- Best for games, menus, and repeated user input

## Quick Difference
- `while condition` → automatic stop
- `while True` → manual stop with `break`

## Rule
- Use `while condition` when you know when to stop
- Use `while True` when the loop should continue until a specific event happens

# Notes: Difference Between `while` and `while True`

- `while condition` runs only when a condition is `True`
- Stops automatically when the condition becomes `False`
- Safer and easier to understand
- Best when the stopping condition is known

- `while True` runs forever
- Must use `break` to stop the loop
- More flexible
- Best for games, menus, and repeated user input

## Quick Difference
- `while condition` → automatic stop
- `while True` → manual stop with `break`

## Rule
- Use `while condition` when you know when to stop
- Use `while True` when the loop should continue until a specific event happens