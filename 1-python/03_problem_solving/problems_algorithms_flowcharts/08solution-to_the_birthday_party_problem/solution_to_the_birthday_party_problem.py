def gcd(a, b):
    # Euclidean algorithm (subtraction-based method)

    # Repeat until both numbers become equal
    while a != b:

        # Compare the two numbers
        if a > b:
            # If a is larger, reduce it by subtracting b
            # This keeps the GCD unchanged
            a = a - b
        else:
            # If b is larger, reduce it by subtracting a
            # This keeps the GCD unchanged
            b = b - a

        # After each step, the numbers get closer to each other

    # When a == b, both values are equal
    # and that value is the GCD
    return a


# Example usage
print(gcd(48, 18))  # Output: 6




# Euclidean algorithm (modulo method)
def gcd(a, b):

    while b != 0:

        # Calculate remainder of a divided by b
        temp = a % b

        # Move current value of b into a
        a = b

        # Store remainder into b for next step
        b = temp

    # When b becomes 0, a is the GCD
    return a


print(gcd(48, 18))  # Output: 6