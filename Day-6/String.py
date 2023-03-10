# String in python
# String is a sequence of characters. It is immutable. It is defined in single or double quotes. It can be accessed using index. It can be sliced. It can be concatenated. It can be repeated. It can be iterated. It can be compared. It can be formatted. It can be searched. It can be replaced. It can be split. It can be joined. It can be reversed. It can be converted to other data types. 
# Example:
string = "Hello World"
print(string) # Output: Hello World
# Accessing characters in string
print(string[0]) # Output: H
# Indexing means accessing characters in string using index. Index starts from 0. Index can be positive or negative. Positive index starts from left to right. Negative index starts from right to left.
# slicing means accessing characters in string using range of index. It can be done using colon(:). It can be done using positive index or negative index.
# Example:
print(string[0:5]) # Output: Hello
print(string[2::4]) # Output: l o
# Concatenation means joining two or more strings. It can be done using + operator.
# Example:
string1 = "Hello"
string2 = "World"
print(string1 + string2) # Output: HelloWorld
# Repetition means repeating a string for given number of times. It can be done using * operator. 
# Example:
print(string1 * 3) # Output: HelloHelloHello
# Iteration means accessing characters in string one by one. It can be done using for loop.
# Example:
for i in string1:
    print(i) # Output: H e l l o
# Comparison means comparing two strings. It can be done using ==, !=, >, <, >=, <= operators.
# Example:
print(string1 == string2) # Output: False
print(string1 != string2) # Output: True
print(string1 > string2) # Output: False
print(string1 < string2) # Output: True
# Formatting means formatting a string. It can be done using format() method.
# Example:
print("Hello {0}".format("World")) # Output: Hello World
# Search means searching a substring in a string. It can be done using find() method. find() method returns index of first occurrence of substring. If substring is not found, it returns -1. It can be done using index() method. index() method returns index of first occurrence of substring. If substring is not found, it raises ValueError exception. It can be done using rfind() method. rfind() method returns index of last occurrence of substring. If substring is not found, it returns -1. It can be done using rindex() method. rindex() method returns index of last occurrence of substring. If substring is not found, it raises ValueError exception. It can be done using count() method. count() method returns number of occurrences of substring in string. If substring is not found, it returns 0. 
# Example:
print(string.find("World")) # Output: 6
print(string.index("World")) # Output: 6
print(string.rfind("World")) # Output: 6
print(string.rindex("World")) # Output: 6
print(string.count("World")) # Output: 1
# Replace means replacing a substring with another substring. It can be done using replace() method. It can be done using translate() method. It can be done using maketrans() method.
# Example:
print(string.replace("World", "Python")) # Output: Hello Python
print(string.translate(string.maketrans("World", "Python"))) # Output: Hello Python
# Split means splitting a string into list of substrings. It can be done using split() method. It can be done using splitlines() method.
# Example:
print(string.split()) # Output: ['Hello', 'World']
print(string.splitlines()) # Output: ['Hello World']
# Join means joining a list of strings into a single string. It can be done using join() method. 
# Example:
print(" ".join(["Hello", "World"])) # Output: Hello World
# Reverse means reversing a string. It can be done using reversed() method. It can be done using slice operator.
# Example:
print("".join(reversed(string))) # Output: dlroW olleH
print(string[::-1]) # Output: dlroW olleH
# Convert means converting a string into other data types. It can be done using int() method. It can be done using float() method. It can be done using complex() method. It can be done using ord() method. It can be done using hex() method. It can be done using oct() method. It can be done using bin() method. It can be done using list() method. It can be done using tuple() method. It can be done using set() method. It can be done using frozenset() method. It can be done using dict() method. It can be done using bool() method. It can be done using bytearray() method. It can be done using memoryview() method. 
# Example:
print(int("123")) # Output: 123
print(float("123.456")) # Output: 123.456
print(complex("123+456j")) # Output: (123+456j)
print(ord("A")) # Output: 65
print(hex(65)) # Output: 0x41
print(oct(65)) # Output: 0o101
print(bin(65)) # Output: 0b1000001
print(list("Hello")) # Output: ['H', 'e', 'l', 'l', 'o']
print(tuple("Hello")) # Output: ('H', 'e', 'l', 'l', 'o')
print(set("Hello")) # Output: {'o', 'H', 'e', 'l'}
print(frozenset("Hello")) # Output: frozenset({'o', 'H', 'e', 'l'})
print(dict([("Hello", "World")])) # Output: {'Hello': 'World'}
print(bool("Hello")) # Output: True
print(bytearray("Hello", "utf-8")) # Output: bytearray(b'Hello')
print(memoryview(bytearray("Hello", "utf-8"))) # Output: <memory at 0x000001F1D1B8F708>
# String methods
# capitalize() method returns a copy of string with first character capitalized and rest of the characters lowercased. 
# Example:
print(string.capitalize()) # Output: Hello world
# casefold() method returns a copy of string with all characters lowercased.
# Example:
print(string.casefold()) # Output: hello world
# center() method returns a copy of string with given width and filled with given fillchar. It is centered in the string.
# Example:
print(string.center(20, "*")) # Output: ****Hello World*****
# count() method returns number of occurrences of substring in string. If substring is not found, it returns 0.
# Example:
print(string.count("l")) # Output: 3
# encode() method returns encoded version of string as bytes object.
# Example:
print(string.encode()) # Output: b'Hello World' 
# endswith() method returns True if string ends with the specified suffix. If not, it returns False.
# Example:
print(string.endswith("World")) # Output: True
# expandtabs() method returns a copy of string where all tab characters are replaced with given number of spaces.
# Example:
print("Hello\tWorld".expandtabs(4)) # Output: Hello   World