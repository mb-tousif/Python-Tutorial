# Write a program to find the integer between 1 and 100 that is divisible by 7 and 5.
for i in range(1, 101):
    if i % 7 == 0 and i % 5 == 0:
        print(i) # 35
# Write a program to find the prime numbers between 1 and 100 and print them and their sum.
sum = 0
for i in range(1, 101):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i) # 1 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
        sum += i
print(sum) # 1060
# # # The else statement belongs to the for loop and is executed when the loop has exhausted iterating the list.
# # # The else statement belongs to the if statement and is executed when the condition is False.
# # A prime number is a number that is only divisible by 1 and itself. For example, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 are all prime numbers.
# # # The sum of all the prime numbers between 1 and 100 is 1060.