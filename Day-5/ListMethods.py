# add two lists in one list
a=[1,2,3,4,5]
b=[6,7,8,9,10]
c=a+b
print(c)
# Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # Delete List Elements
# # There are several ways in which we can delete one or more items from a list in Python. The simplest way is to use the keyword del. We can also use the remove() method or the pop() method. The del statement can also be used to delete slices from a list or clear the entire list. All of these methods are described below. 
# # Example:
list = ['physics', 'chemistry', 1997, 2000]
print (list)
del list[2]
print ("After deleting value at index 2 : ")
print (list)
# Output:
# ['physics', 'chemistry', 1997, 2000]
# appending a list
a=[1,2,3,4,5]
b=[6,7,8,9,10]
a.append(b)
print(a)
# Output:
# [1, 2, 3, 4, 5, [6, 7, 8, 9, 10]]
# # Basic List Operations
# # There are several operators that work with list to perform different computation. The most common operators are membership and identity operators. 
# # Membership Operators
# # The membership operators in Python are used to test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary). There are two membership operators as explained below −
# # Example:
list = [1, 2, 3, 4, 5 ];
if ( 3 in list ):
    print ("3 is available in the given list")
else:
    print ("3 is not available in the given list")
if ( 6 not in list ):
    print ("6 is not available in the given list")
else:
    print ("6 is available in the given list")
# Output:   
# 3 is available in the given list
# 6 is not available in the given list
# # Identity Operators
# # Identity operators compare the memory locations of two objects. There are two Identity operators as explained below −
# # Example:
a = 20
b = 20
if ( a is b ):
    print ("a and b have same identity")
else:
    print ("a and b do not have same identity")
if ( id(a) == id(b) ):
    print ("a and b have same identity")
else:
    print ("a and b do not have same identity")
b = 30
if ( a is b ):
    print ("a and b have same identity")
else:
    print ("a and b do not have same identity")
if ( a is not b ):
    print ("a and b do not have same identity")
else:
    print ("a and b have same identity")
# Output:
# a and b have same identity
# a and b have same identity
# a and b do not have same identity
# a and b do not have same identity 
# # Built-in List Functions & Methods
# # Python includes the following list functions −
# # cmp(list1, list2)
# # Compares elements of both lists.
# # len(list)
# # Gives the total length of the list.
# # max(list)
# # Returns item from the list with max value.
# # min(list)
# # Returns item from the list with min value.
# # list(seq)
# # Converts a tuple into list.
# # Python includes the following list methods −
# # list.append(obj)
# # Appends object obj to list
# # list.count(obj)
# # Returns count of how many times obj occurs in list