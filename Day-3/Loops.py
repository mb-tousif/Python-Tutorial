                    # Loop in Python
                    # For Loop
# For Loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

# write a program to print all the numbers from 0 to 10
for i in range(11):
    print(i) # 0 1 2 3 4 5 6 7 8 9 10
                    # While Loop
# While Loop is used to iterate over a block of code as long as the test expression (condition) is true. In Python, the while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1. We also need to define the number of times we want to iterate through the loop, in this example we want to print 10 times, so we set the test expression to run while i is less than or equal to 10. The while loop will continue to iterate as long as i is less than or equal to 10, each time it iterates it will add 1 to i. When i is no longer less than or equal to 10, the loop has completed its execution. 
# write a program to print all the numbers from 0 to 10
i = 0
while i <= 10:
    print(i) # 0 1 2 3 4 5 6 7 8 9 10
    i += 1
                    # Nested Loops
# A nested loop is a loop inside a loop. The "inner loop" will be executed one time for each iteration of the "outer loop". 
# write a program to print all the numbers from 0 to 10
for i in range(11):
    for j in range(11):
        print(i, j)
                    # Break Statement 
# With the break statement we can stop the loop even if the while condition is true: 
# write a program to print all the numbers from 0 to 10
i = 0
while i <= 10:
    print(i) # 0 1 2 3 4 5 6 7 8 9 10
    i += 1
    if i == 5:
        break
                    # Continue Statement
# Continue Statement is used to tell Python to skip the current block, and to continue to the next block.
# write a program to print all the numbers from 0 to 10
for i in range(11):
    if i == 5:
        continue
    print(i) # 0 1 2 3 4 6 7 8 9 10

                    # Pass Statement
# Pass Statement is used when a statement is required syntactically but you do not want any command or code to execute.
# write a program to print all the numbers from 0 to 10
for i in range(11):
    if i == 5:
        pass
    print(i) # 0 1 2 3 4 5 6 7 8 9 10

                    # Loop Control Statements
# Loop control statements change execution from its normal sequence. When execution leaves a scope, all automatic objects that were created in that scope are destroyed. Python supports the following control statements.
# Example Loop Control Statements in Python

            # Expression 	Description
# break 	Used to terminate the loop statement and transfers execution to the statement immediately following the loop.
# continue 	Used to skip the rest of the code inside a loop for the current iteration only. Loop does not terminate but continues on with the next iteration.
# pass 	The pass is a null operation; nothing happens when it executes. The pass is also useful in places where your code will eventually go, but has not been written yet (e.g., in stubs for example).
