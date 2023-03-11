# Problem-1 String sorting in Python
# Example-1:
string = "HelloWorld"
temp =sorted(string.casefold())
print("".join(temp)) # Output: deHllloorW
# Example-2:
text = input("Enter a string: ")
temp =sorted(text.casefold())
print("".join(temp)) # input: Enter a string: Tousif. Output: fiosTu

# Problem-2 Palindrome string checking in Python
# Example-1:
text = input("Enter a string: ")
if text.casefold() == "".join(reversed(text.casefold())):
    print("Palindrome string")
else:
    print("Not a palindrome string")
# input: Enter a string: Tousif. Output: Not a palindrome string

# Problem-3 String reverse in Python
# input: Enter a string: I am MERN Dev Tousif.
# Example-1:
text = input("Enter a string: ")
text=text.split(" ")
temp =[]
for i in text:
    temp.append(i[::-1])
print(" ".join(temp)) # Output: I ma NREM veD fisuoT.
