# for loop repeats code fixed times
for i in range(10):
    print(i)

print() # make a whitespace line

#range(5) → 0,1,2,3,4 (5 not included)
for i in range(5):
    print(i)

print() # make a whitespace line

#"*" * i makes repeating pattern
for i in range(5):
    print("*" * i)

#Nested for loop:
for i in range(1,6):
    for h in range(i):
        print("*", end="")  # end="" keeps output on the same line (no newline after each "*")
    print()  # moves to the next line after the inner loop finishes (new row for each i)


#Now we learn how to shrink the pattern instead of growing it.
for i in range(5,0,-1): #(start,stop,step)
    for h in range(i):
        print("*", end="")  # end="" keeps output on the same line (no newline after each "*")
    print()  # moves to the next line after the inner loop finishes (new row for each i)

