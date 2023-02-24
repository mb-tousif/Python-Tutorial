# Python Arithmetic Operators
# + Addition
sum = 10 + 20;
print(sum);
# - Subtraction
sub = 20 - 10;
print(sub);
# * Multiplication
mul = 10 * 20;
print(mul);
# / Division
div = 20 / 10;
print(div);
# % Modulus
mod = 20 % 10;
print(mod);
# ** Exponentiation
exp = 10 ** 2;
print(exp);
# // Floor division
floor = 20 // 10;
print(floor);
# Python Assignment Operators
# = Assignment
a = 10;
print(a);
# Python Assignment Operators
# == Equal
a = 10;
b = 10;
print(a == b);
# Python Comparison Operators
# != Not Equal
a = 10;
b = 20;
print(a != b);
# > Greater than
a = 10;
b = 20;
print(a > b);
# < Less than
a = 10;
b = 20;
print(a < b);
# >= Greater than or equal to
a = 10;
b = 10;
print(a >= b);
# <= Less than or equal to
a = 10;
b = 10;
print(a <= b);
# Python Logical Operators
# and Logical AND
a = 10;
b = 20;
c = 30;
print(a < b and b < c);
# or Logical OR
a = 10;
b = 20;
c = 30;
print(a < b or b > c);
# not Logical NOT
a = 10;
b = 20;
c = 30;
print(not(a < b and b < c));
# Python Identity Operators
# is Identity
a = 10;
b = 10;
print(a is b);
# is not Identity
a = 10;
b = 20;
print(a is not b);
# Python Membership Operators
# in Membership
a = 10;
b = [10, 20, 30];
print(a in b);
# not in Membership
a = 10;
b = [10, 20, 30];
print(a not in b);
# Python Bitwise Operators
# & Bitwise AND
a = 10;
b = 20;
print(a & b);
# | Bitwise OR
a = 10;
b = 20;
print(a | b);
# ^ Bitwise XOR
a = 10;
b = 20;
print(a ^ b);
# ~ Bitwise NOT
a = 10;
print(~a);
# << Bitwise left shift
a = 10;
print(a << 2);
# >> Bitwise right shift
a = 10;
print(a >> 2);
# Python Operator Precedence
# Operator	Precedence
# ()	Exponentiation (raise to the power)
# ~ + -	Complement, unary plus and minus (method names for the last two are +@ and -@)
# * / % //	Multiplication, division, modulo and floor division
# + -	Addition and subtraction
# >> <<	Right and left bitwise shift
# &	Bitwise 'AND'
# ^ |	Bitwise exclusive `OR' and regular `OR'
# <= < > >=	Comparison operators
# <> == !=	Equality operators
# = %= /= //= -= += *= **=	Assignment operators
# Precedence Operator
example = (10 + 20) * 30;
print(example);