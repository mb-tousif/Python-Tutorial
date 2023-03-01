                    # Fibonacci Series
# Fibonacci Series is a series of numbers in which each number is the sum of the two preceding numbers. For example, the first 5 numbers in the Fibonacci Series are 0, 1, 1, 2, 3. The 6th number is 5, the 7th number is 8, and so on. The first two numbers in the Fibonacci Series are 0 and 1. 
# Write a program to print the Fibonacci Series up to a given number.
# For example, if the user enters 5, the output should be 0, 1, 1, 2, 3, 5.

number = int(input("Enter a number: "))
firstNumber = 0
secondNumber = 1
print(firstNumber)
print(secondNumber)
for i in range(2, number+1):
    thirdNumber = firstNumber + secondNumber
    print(thirdNumber)
    firstNumber = secondNumber
    secondNumber = thirdNumber