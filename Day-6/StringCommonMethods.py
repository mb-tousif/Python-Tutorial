# String Methods in Python
string = "HelloWorld"
# lower() method returns a copy of string with all characters lowercased.
# Example:
print(string.lower()) # Output: hello world
# islower() method returns True if all characters in string are lowercased. Otherwise, it returns False.
# Example:
print(string.islower()) # Output: False
# upper() method returns a copy of string with all characters uppercase.
# Example:
print(string.upper()) # Output: HELLO WORLD
# isupper() method returns True if all characters in string are uppercased. Otherwise, it returns False.
# Example:
print(string.isupper()) # Output: False
# isalpha() method returns True if all characters in string are alphabets. Otherwise, it returns False.
string1 ="aysshd"
# Example:
print(string1.isalpha()) # Output: True
# isalnum() method returns True if all characters in string are alphanumeric. Otherwise, it returns False.
# Example:
print(string.isalnum()) # Output: False
# swapcase() method returns a copy of string with all uppercase characters lowercased and all lowercase characters uppercase.
# Example:
print(string.swapcase()) # Output: hELLO wORLD
# title() method returns a copy of string with first character of each word capitalized and rest of the characters lowercased.
# Example:
print(string.title()) # Output: Hello World
# istitle() method returns True if string is title cased. Otherwise, it returns False.
# Example:
print(string.istitle()) # Output: False
# isdigit() method returns True if all characters in string are digits. Otherwise, it returns False.
# Example:
string2 = 12345 # string2 = "12345"
print(string2.isdigit()) # Output: True
# join() method returns a string by joining all the elements of an iterable, separated by a string separator.
# Example:
print(" ".join(["Hello", "World"])) # Output: Hello World