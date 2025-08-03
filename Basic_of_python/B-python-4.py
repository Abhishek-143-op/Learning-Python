               #Learning about the operators 
#Arithmatic operators 
"""
+  Addition operators 
-  Substraction operators 
/  Division operators 
*  Multiplication operators 
%  Modulus operators -- returns the remainder after the division
// Floor division -- returns the integer while division .
** Exponentiation operators 
"""
#Examples of each operators.
a=30.2
b=5.2

#Addition
print("Addition of a+b:",a+b)

#Substraction
print("Substraction of a-b:",a-b)

#Division
print ("Division of a/b:",a/b)

#Multiplication
print("Multiplication of a*b:",a*b)

#Modulus
print("Modulus of a%b :",a%b)

#Floor division
print("Floor division of a//b:",a//b)

#Exponent operators 
print("Exponent  of a**b:",a**b)

#COMPARISIONAL OPERATORS
"""
== : Equal to operator.
!= : Not equal to operator.
>  : Greater than operators.
<  : Less than operators.
>= : Greater than equal to operators.
<= : Less than equal to operators.
"""
#EXAMPLES
"""
Common sense hai exaples ki jrurat nahi hai . 
There is no need for the examples for comprasional operators .

"""
# Assignment operators 
"""
=  : Assign value 
+= : Add than assign value
-= : Substract than assign value
*= : Multiply than assign value
/= : Divide than assign value
//=: Floor divide than assign value
%= : Modulus than assign value
**=: Exponent than assign value
"""
#EXAMPLES 

#Assignment operators =
x = 10
print(x)  # Output: 10 

#Add than assign value +=
x = 5
x += 3      # same as x = x + 3
print(x)    # Output: 8

#Subs than assign value -=
x = 10
x -= 4      # same as x = x - 4
print(x)    # Output: 6

#Multiply than assign value *=
x = 6
x *= 2      # same as x = x * 2
print(x)    # Output: 12

#Divide than assign value /=
x = 8
x /= 2      # same as x = x / 2
print(x)    # Output: 4.0 (Note: Result is always float)

#Floor divide than assign //=
x = 9
x //= 2     # same as x = x // 2
print(x)    # Output: 4

#Modulus than assign %=
x = 10
x %= 3      # same as x = x % 3
print(x)    # Output: 1

#Exponent than assign **=
x = 2
x **= 3     # same as x = x ** 3
print(x)    # Output: 8

#LOGICAL OPERATORS
"""
and : used like common statements in the English Language 
or  :    --------Same----------
not :    --------Same----------
"""
#EXAMPLES

#and operator
x = 5
print(x > 2 and x < 10)  # True (both are true)
print(x > 10 and x < 20) # False (first is false)

#or operator
x = 5
print(x > 2 or x > 10)   # True (first is true)
print(x < 2 or x > 10)   # False (both are false)

#not operator
x = 5
print(not (x > 2))       # False (because x > 2 is True)
print(not (x < 2))       # True  (because x < 2 is False)

#Membership operator 
"""
Used to check value , or something like data present in the collection of data 

in---- Return true if value or searched data exist in collection of data.
not in --- Return true if value or searched data donot exist in the collection of data.
"""
#EXAMPLES

#in and not in operator
my_list = [1, 2, 3, 4]

print(2 in my_list)       # True
print(5 in my_list)       # False
print(10 not in my_list)  # True

name = "Abhishek"
print("s" in name)        # True
print("z" not in name)    # True

#Identity operator : Used if 2 variable refers to same object 
"""
is --- Returns True if both variables refer to the same object.
is not --- Returns True if they do not refer to the same object.
"""

#EXAMPLES

a = [1, 2, 3]
b = a          # b and a point to same object
c = [1, 2, 3]  # c is a new object

print(a is b)       # True (same object)
print(a is c)       # False (different objects, even if contents are same)
print(a is not c)   # True



#-------- Bitwise operators----------: Study later on (can be used in the advanced concepts.)
"""
              Bitwise Operators
Used to perform bit-level operations on integers.

They work on binary numbers (0s and 1s).
Example: 5 → binary: 0101
"""
a = 5      # Binary: 0101
b = 3      # Binary: 0011

print(a & b)     # 1   (0001) → AND --- if both input are 1 then output is 1 
print(a | b)     # 7   (0111) → OR --- if any bit is 1 then output is 1
print(a ^ b)     # 6   (0110) → XOR--- if both bits are diff then output is 1 otherwise 0
print(~a)        # -6  (inverts all bits) → NOT--- it flips 0-->1 and 1-->0

print(a << 1)    # 10  (shifts 0101 → 1010) --- moves 2 bits to left (*2)
print(a >> 1)    # 2   (shifts 0101 → 0010) --- moves 2 bits to right (/2)


