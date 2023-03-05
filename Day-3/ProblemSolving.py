# Write a program to print the multiplication table of 9.
for i in range(1, 11):
    print("9 x", i, "=", 9*i)

# Write a program to print Vowel in list if it is present in the string.
string = "Hello, have you tried our tutorial section yet?"
vowels = ['a', 'e', 'i', 'o', 'u']
for i in string:
    if i in vowels:
        print(i) # e o u i o u e o u i o

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

# a> 0, a%10 = last digit, a//10 = remaining digits
# Write a program to find the length of digits in a number.
# Method 1
num = int(input("Enter a number: "))
count = 0
while num > 0:
    num = num//10
    count += 1
print(count) # 5
# Method 2
num = input("Enter a number: ")
print(len(num)) # 5

# Write a program to check if a number is an Armstrong number or not.
# Armstrong Number is a number that is equal to the sum of cubes of its digits.
# For example 0, 1, 153, 370, 371, 407 etc.
# Method 1
num = int(input("Enter a number: "))
num_len = len(str(num))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** num_len
    temp //= 10
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
# Method 2
num = int(input("Enter a number: "))
num_len = len(str(num))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** num_len
    temp //= 10
print(num, "is an Armstrong number") if num == sum else print(num, "is not an Armstrong number")