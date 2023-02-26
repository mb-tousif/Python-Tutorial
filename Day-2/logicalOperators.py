                        # Logical Operators
            # Logical operators are the and, or, and not operators.
# The and operator returns True if both its operands are True.
# write a program to check if a number is positive and even
num = int(input("Enter a number: "))
if num > 0 and num % 2 == 0:
    print("The number is positive and even")
else:
    print("The number is either negative or odd or both")
# The or operator returns True if either of its operands is True.
# write a program to check if a number is positive or even
num = int(input("Enter a number: "))
if num > 0 or num % 2 == 0:
    print("The number is positive or even")
else:
    print("The number is either negative or odd or both")
# The not operator returns True if its operand is False.
# write a program to check if a number is not positive
num = int(input("Enter a number: "))
if not num > 0:
    print("The number is not positive")
else:
    print("The number is positive")