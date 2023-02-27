                        # Nested Loops in Python
# Nested Loops means that a loop can be inside another loop. The inner loop will be executed one time for each iteration of the outer loop. The following example shows how to use nested loops in Python: 
# Example 1: Nested Loops in Python
for i in range(1, 6):
    for j in range(1, 6):
        print(i, j, sep='-', end=' ')
        # print(i*j, end=' ')
    print()

# Program to print multiplication table (from 5 to 7) in Python
for i in range(5, 8):
    for j in range(1, 11):
        print(i, 'x', j, '=', i*j)
    print()

# Write a program to print pattern in Python
for i in range(1, 5):
    for j in range(1, i+1):
        print('🐍', end=' ')
    print()

# Write a program to print a pattern where a to z is printed in the following format:
# a
# a b
# a b c
# ASCII value of a is 97 and ASCII value of z is 122. for Capital letters, the ASCII value of A is 65 and ASCII value of Z is 90.
    # For Small letters
for i in range(1, 27):
    for j in range(97, 97+i):
        print(chr(j), end=' ')
    print()

    # For Capital letters
for i in range(1, 27):
    for j in range(97, 97+i):
        print(chr(j), end=' ')
    print()