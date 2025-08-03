            #Learning about the TYPECASTING AND TYPE() FUNCTION
"""
TypeCasting means the changing the datatypes of variables .
  It is of 2 types 
    1. Implict TypeCasting : In python automatically typecasting is done.
    2. Explict TypeCasting : Done manually by using diff. datatype.
"""
#Example of implict typecasting 
a = 10         # int
b = 2.5        # float
c = a + b      # Python converts 'a' to float automatically
print(c)       # Output: 12.5 (float)

#Example of Explict typecasting 

        #In program examples without output or say without print
int(3.9)  # 3.9 converted to int : 3
float(7)  # 7 is converted to float : 7.0
bool(0)   # bool to false
str(20)   # 20 is converted to the string : "20"
  

        # Examples with print 
a = "10"
b = int(a)     # str → int
print(b + 5)   # Output: 15 ---- int datatype before typecasting it was string.
print(type(b+5))

x = 5.6
y = int(x)     # float → int
print(y)       # Output: 5-----int datatype before typecasting it was float.
print(type(y))

z = 100
s = str(z)     # int → str
print(s + "0") # Output: "1000"---- 0 is added to the string 100 like 100 was already there but 100(0) is added to it as strig
print(type(s+"0"))

"""
print(   type(variable)   )
          ____________  
                |
      | here this type() function |  
      |shows the variable datatype|
      |Examples are already shown |
      |with the typecasting of    |
      |functions                  |  

"""
