# Task: GCD + Subset Selection Using Bitmasking

---

## Objective:
Compute the GCD of two numbers (48 and 42), use it to define a grouping size,
select elements that fit exactly into that size,
and generalize the method for any two numbers X and Y using pseudocode.

FUNCTION GCD(a, b)
    WHILE b is not 0
        a, b ← b, a mod b
    RETURN a
END FUNCTION


FUNCTION solve(x, y, siblings_list)

    TARGET ← GCD(x, y)

    group_size ← empty list

    FOR each s in siblings_list DO
        ADD (1 + s) to group_size
    END FOR


    best_solution ← empty list
    best_count ← 0
    number_guests ← length of group_size


    FOR mask from 0 to (2^number_guests - 1) DO

        subset ← empty list
        total_people ← 0


        FOR i from 0 to number_guests - 1 DO

            IF (mask AND (1 shifted left from i)) is not 0 THEN
                ADD (i + 1) to subset
                total_people ← total_people + group_size[i]
            END IF

        END FOR


        IF total_people equals TARGET THEN

            IF length of subset > best_count THEN
                best_solution ← subset
                best_count ← length of subset
            END IF

        END IF

    END FOR

    RETURN best_solution

END FUNCTION


X ← 48
Y ← 42

siblings_list ← [0, 2, 1, 0, 1, 1]

result ← solve(X, Y, siblings_list)

PRINT result


What to remember
✔ 2 choices per guest (pick / not pick)
✔ 6 guests → 2⁶ = 64 combinations
✔ Each number from 0–63 = one subset
✔ Binary form shows exactly who is selected
✔ This is called bitmasking / subset generation