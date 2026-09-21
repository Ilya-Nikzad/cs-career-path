# Conditions & Data
---

1. `Conditions with Numbers`: Use comparisons when a business rule depends on a numeric value.`

like also in range: if 60 <= score < 80:

2. `Conditions with Strings`: Real data often contains categories or statuses.

like: if status == "active":

Remember that string comparisons are case-sensitive.

3. `Conditions with Lists`: A list can itself be tested in a condition.

like: orders = ["A102", "A103"]

if orders:

    print("Orders exist")

An empty list is considered false, while a non-empty list is considered true.

Python's truth-value rules also treat None, numeric zero, and empty strings/containers as false.

4. `in and not in`: Membership conditions are useful when a value needs to be checked against a group.

like: if status in allowed_statuses:

in tests membership and not in tests the opposite

like: if status not in allowed_statuses:

5. `Truthiness`: Python allows many values to be evaluated directly as conditions.

Common falsy values include: False, None, 0 , 0.0, "", []

6. `None in Conditions`: None represents the absence of a value.

like: if delivery_date is None:

          print("No delivery date")

When specifically checking for None, use:

value is None

or:

value is not None

# Important Rule — Conditions & Data
---

Numbers → numeric comparisons.

Categories/statuses → string comparisons.

Group membership → in / not in.

Empty collections → falsy.

Non-empty collections → truthy.

0 → falsy.

None → absence of a value.

Use is None when specifically checking for None.

Do not automatically treat missing, empty, and zero as the same thing.
