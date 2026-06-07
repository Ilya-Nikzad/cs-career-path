# BEGIN

# Function: Perform column addition on two numbers represented as strings
def column_addition(num_1, num_2):

    # Step 1: Find the maximum length of the two input strings
    max_length = max(len(num_1), len(num_2))

    # Step 2: Pad the shorter number with leading zeros so both have equal length
    num_1 = num_1.zfill(max_length)
    num_2 = num_2.zfill(max_length)

    # Step 3: Create an empty list to store result digits
    result = []

    # Step 4: Initialize carry to 0
    carry = 0

    # Step 5: Process digits from right to left
    for i in range(max_length - 1, -1, -1):

        # Step 6: Add corresponding digits and the carry
        sum_digits = int(num_1[i]) + int(num_2[i]) + carry

        # Step 7: Calculate the result digit (sum mod 10)
        result_sum = sum_digits % 10

        # Step 8: Update carry (sum div 10)
        carry = sum_digits // 10

        # Step 9: Append the result digit to the result list
        result.append(str(result_sum))

    # Step 10: If a carry remains after the loop, append it
    if carry > 0:
        result.append(str(carry))

    # Step 11: Reverse the result list because digits were added from right to left
    result.reverse()

    # Step 12: Join the digits into a single string and return it
    return "".join(result)


# Step 13: Call the function with two numbers
result = column_addition("123", "123")

# Step 14: Display the result
print(result)

# END