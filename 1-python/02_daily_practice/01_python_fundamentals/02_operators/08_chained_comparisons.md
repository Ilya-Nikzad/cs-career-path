# `Chained Comparisons`
---

Chained comparisons let you combine comparisons in a clean way

Why use them?

They are especially useful when a value needs to be within a range.

think:

Range → chained comparison

# Important Rule — Chained Comparisons
---

a < b < c checks both comparisons.

a <= b <= c includes both boundaries.

a < b < c does not include the boundaries.

Chained comparisons are equivalent to using and between the comparisons.

They are useful for readable range checks.