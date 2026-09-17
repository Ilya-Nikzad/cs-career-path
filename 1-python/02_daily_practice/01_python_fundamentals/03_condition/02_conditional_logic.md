# Conditional Logic
---

This section is about making conditions work together and choosing the correct decision structure.

1. `Combining Conditions: You can combine conditions with and, or, and not.`

Both → and

Either/at least one → or

Opposite/not true → not

2. `Condition Order: Python evaluates conditional branches from top to bottom.`

Must see: Which condition should be checked first?

3.  `Complex Conditional Logic: You can combine multiple operators and conditions.`

like: if age >= 18 and (has_ticket or is_member):

Parentheses can make the intended logic clearer.

Think of complex logic as breaking a requirement into smaller questions:

Is the person an adult?

Do they have a ticket or membership?

Are both requirements satisfied?

4. `Conditional Expressions: A conditional expression is the one-line form of a simple if/else.`

like: status = "Pass" if score >= 60 else "Fail"

Use it when the decision is simple.

Avoid turning complicated logic into a difficult one-line expression.

# Important Rule — Conditional Logic
---
and → all required conditions must be true.

or → at least one condition must be true.

not → reverses a condition.

if/elif conditions are checked top to bottom.

Put more specific conditions before broader ones when necessary.

Use parentheses when complex logic needs to be clear.

Conditional expressions are best for simple two-way decisions.



# From your lesson:
# 
# Create a Review classification.
# It should happen when an AQI threshold and another relevant data condition are satisfied.
# Use and when both conditions must be true.
# Use or when either condition can qualify.
# Use not when you need to invert a condition.
# Test that every valid record gets the intended classification.
# 
# So Level 2 is mainly about logical operators and combining conditions.
# 
# Level 3 — Complex Conditions
# 
# From your lesson:
# 
# Create a more complex classification using multiple logical operators.
# Carefully order your if/elif branches so specific cases are checked before broader ones.
# 
# Use a conditional expression for one simple two-way decision:
# 
# value = x if condition else y
# Produce a final report containing:
# total records
# AQI category totals
# Review totals
# your additional classification
# Test that every valid record is accounted for.
