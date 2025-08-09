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



#day 2:  TYPECASTING WITH EXAM POV

"""
           📌 Definition (Exam Answer Format):
Type casting is the process of converting one data type into another using built-in functions like int(), float(), str(), etc.

             🧠 Why is Type Casting Used?
To perform operations between different data types (like string and integer).

To ensure compatibility in expressions and functions.

📂 Types of Type Casting:
1. Implicit Type Casting
✅ Done automatically by Python.

🔹 Example:
"""

a = 5      # int
b = 2.0    # float
c = a + b  # Python converts a to float automatically
print(c)   # Output: 7.0
# ➡️ Here, int is implicitly converted to float.

"""
2. Explicit Type Casting
✅ Done manually by the programmer using functions.
"""

#         new_data = desired_type(existing_data)

m=10        #datatype is int 
n=float(m)  #datatype is float of m.
p= str(m)   #dataype is string of m.

"""
With these above example we able to know that 1 datatype is converted into many 
Therefore when we can use 1 single data in different types of dataypes like string , 
float etc. According to the situation.


"""
