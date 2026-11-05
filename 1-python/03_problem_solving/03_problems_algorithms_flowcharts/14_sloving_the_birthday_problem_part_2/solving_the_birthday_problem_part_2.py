# Task:
# Compute the GCD of two numbers (48 and 42), use it to define a grouping size,
# select elements that fit exactly into that size,
# and generalize the method for any two numbers X and Y using pseudocode.

#BEGIN
# Function GCD
def GCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Main function for birthday problem
def solve(x, y, siblings_list):
    # Step 1: Target number of people
    TARGET = GCD(x,y)

    # Step 2: Convert siblings into group sizes
    group_size = []

    for s in siblings_list:
        group_size.append(1 + s)


    # Step 3: Stores the best valid set of guests found so far
    best_solution = []
    # Stores the maximum number of guests in the best valid solution
    best_count = 0
    # Number of guests (size of the group_size list)
    number_guests = len(group_size)

    # Step 4: Step: check all possible subsets
    for mask in range(1 << number_guests):
        subset = []
        total_people = 0

        # Loop through each guest to apply the mask pattern (include or skip each one)
        for i in range (number_guests):
            # Check whether the i-th guest is selected (ON = 1) or not (OFF = 0) in the current mask
            if mask & (1 << i):
                subset.append(i + 1)
                total_people += group_size[i]

        # Step 4: Check if valid solution
        if total_people == TARGET:

            # keep best (maximum guests)
            if len(subset) > best_count:
                best_solution = subset
                best_count = len(subset)

    return best_solution


# Example Input (Part 2)

X = 48
Y = 42

siblings_list = [0, 2, 1, 0, 1, 1]
result = solve(X, Y, siblings_list)
print("Best guests to invite:", result)






