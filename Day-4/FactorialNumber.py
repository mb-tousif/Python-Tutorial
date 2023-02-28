# Factorial of a number
# Write a program to find the factorial of a number.
# Factorial means the product of all the numbers from 1 to that number. For example, the factorial of 3 is 1*2*3 = 6.

userNumber = int(input("Enter a number: "))
factorial = 1
for number in range(1, userNumber+1):
    factorial = factorial * number
print("Factorial of", userNumber, "is", factorial)