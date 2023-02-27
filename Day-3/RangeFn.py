                        # range()
# # The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number. It takes 3 parameters: start, stop, and step. The start parameter is optional, and defaults to 0. The step parameter is optional, and defaults to 1. The stop parameter is required.
# # Example of range() function in Python.
# # write a program to print all the numbers from 0 to 10
for i in range(11):
    print(i) # 0 1 2 3 4 5 6 7 8 9 10
for i in range(1, 11):
    print(i) # 1 2 3 4 5 6 7 8 9 10
for i in range(1, 11, 2):
    print(i) # 1 3 5 7 9
for i in range(10, 0, -1):
    print(i) # 10 9 8 7 6 5 4 3 2 1
# # The range() function returns a range object with numbers, the default start value is 0, and the default increment is 1 (default values can be overridden). The range() function is used when a user needs to perform an action for a specific number of times.