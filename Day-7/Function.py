# Function in Python
# A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result. In Python, a function is defined using the def keyword: 
# Example:
def my_function():
    print("Hello from a function")
# To call a function, use the function name followed by parenthesis:
# Example:
my_function() # Output: Hello from a function
# Information can be passed into functions as arguments. Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
# Example:
def my_function(fname):
    print(fname + " Refsnes")
my_function("Emil") # Output: Emil Refsnes

# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less. 
# Example:
def my_function(fname, lname):
    print(fname + " " + lname)
my_function("Emil", "Refsnes") # Output: Emil Refsnes
# If you try to call the function with 1 or 3 arguments, you will get an error: 
# Example:
def my_function(fname, lname):
    print(fname + " " + lname)
my_function("Emil") # Output: TypeError: my_function() missing 1 required positional argument: 'lname'

#  Function Types in Python
#  There are two types of functions in Python:
#  1. Built-in functions
#  2. User-defined functions
#  Built-in functions
#  Python has a set of built-in functions, which are always available for use. 
#  Example:
#  abs() - Returns the absolute value of a number
#  all() - Returns True if all items in an iterable object are true
#  any() - Returns True if any item in an iterable object is true
#  ascii() - Returns a readable version of an object. Replaces none-ascii characters with escape character
#  bin() - Returns the binary version of a number
#  bool() - Returns the boolean value of the specified object
#  bytearray() - Returns an array of bytes
#  bytes() - Returns a bytes object
#  callable() - Returns True if the specified object is callable, otherwise False
#  chr() - Returns a character from the specified Unicode code.
#  classmethod() - Converts a method into a class method
#  compile() - Returns the specified source as an object, ready to be executed
#  complex() - Returns a complex number
#  delattr() - Deletes the specified attribute (property or method) from the specified object
#  dict() - Returns a dictionary (Array)
#  dir() - Tries to return a list of valid attributes of the object
#  divmod() - Returns the quotient and the remainder when argument1 is divided by argument2
#  enumerate() - Takes a collection (e.g. a tuple) and returns it as an enumerate object
#  eval() - Executes the specified code (or object)
#  exec() - Executes the specified code (or object)
#  filter() - Use a filter function to exclude items in an iterable object
#  float() - Returns a floating point number
#  format() - Formats a specified value
#  frozenset() - Returns a frozenset object
#  getattr() - Returns the value of the specified attribute (property or method)
#  globals() - Returns the current global symbol table as a dictionary
#  hasattr() - Returns True if the specified object has the specified attribute (property/method)
#  hash() - Returns the hash value of a specified object
#  help() - Executes the built-in help system
#  hex() - Converts a number into a hexadecimal value
#  id() - Returns the id of an object
#  input() - Allow user input
#  int() - Returns an integer number
#  isinstance() - Returns True if a specified object is an instance of a specified object
#  issubclass() - Returns True if a specified class is a subclass of a specified object
#  iter() - Returns an iterator object
#  len() - Returns the length of an object
#  list() - Returns a list
#  locals() - Returns an updated dictionary of the current local symbol table
#  map() - Returns the specified iterator with the specified function applied to each item
#  max() - Returns the largest item in an iterable
#  memoryview() - Returns a memory view object
#  min() - Returns the smallest item in an iterable
#  next() - Returns the next item in an iterable
#  object() - Returns a new object
#  oct() - Converts a number into an octal
#  open() - Opens a file and returns a file object
#  ord() - Converts an integer representing the Unicode of the specified character
#  pow() - Returns the value of x to the power of y
#  print() - Prints to the standard output device
#  property() - Gets, sets, deletes a property
#  range() - Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
#  repr() - Returns a readable version of an object
#  reversed() - Returns a reversed iterator
#  round() - Rounds a numbers
#  set() - Returns a new set object
#  setattr() - Sets an attribute (property/method) of an object
#  slice() - Returns a slice object
#  sorted() - Returns a sorted list
#  @staticmethod() - Converts a method into a static method
#  str() - Returns a string object
#  sum() - Sums the items of an iterator
#  super() - Returns an object that represents the parent class
#  tuple() - Returns a tuple
#  type() - Returns the type of an object
#  vars() - Returns the __dict__ property of an object
#  zip() - Returns an iterator, from two or more iterators
#  __import__() - Used to import a module
#  User-defined functions
#  You can create your own functions with the def keyword.
#  Example:
def my_function():
    print("Hello from a function")
#  Calling a Function
#  To call a function, use the function name followed by parenthesis:
#  Example:
def my_function():
    print("Hello from a function")
my_function() # Output: Hello from a function
#  Arguments
#  Information can be passed into functions as arguments. Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma. 
#  The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:
#  Example:
def my_function(fname):
    print(fname + " Refsnes")
my_function("Emil") # Output: Emil Refsnes
my_function("Tobias") # Output: Tobias Refsnes
my_function("Linus") # Output: Linus Refsnes
#  By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
#  Example:
def my_function(fname, lname):
    print(fname + " " + lname)
my_function("Emil", "Refsnes") # Output: Emil Refsnes
#  If you try to call the function with 1 or 3 arguments, you will get an error:
#  Example:
def my_function(fname, lname):
    print(fname + " " + lname)
my_function("Emil") # Output: TypeError: my_function() missing 1 required positional argument: 'lname'
#  Arbitrary Arguments, *args
#  If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
#  This way the function will receive a tuple of arguments, and can access the items accordingly:
#  Example:
def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus") # Output: The youngest child is Linus
#  If the number of arguments is unknown, add a * before the parameter name:
#  Example:
def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus") # Output: The youngest child is Linus
