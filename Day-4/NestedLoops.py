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