                     # LEARNING ABOUT THE VARIABLES, DATATYPES AND INDENTIFIERS 
 #variable is a named container or amazon box with named What inside of it .


#variable with the int datatype 
a= 89                   
b= 1
print (a+b)

# variable with string datatype and strings are always written in the "________".
c= "Abhishek" 
print(c)
 
# variable with float datatype.
d= 5.23   
e= 55e4     #scientific float point no. where e__    means 10^something.
print(e,"and sum of d+e",d+e)

#variable with boolean datatype 
f=True 
g=False

#variable with none or special datatype 
h=None
# None type variable means variable donot contain any value in it.


#  RULES FOR NAMING AN INDENTIFIER (NAME OF THE VARIABLE LIKE IN ABOVE VARIABLE = a,b,c,d,e,f,g,h.)
"""
1. Indentifier starts with the LETTER OR UNDERSCORE(_).
2. Indentifier can contain only LETTERS , UNDERSCORE(_) AND NUMBERS(0-9)
3. Indentifier donot contain whitespace in between the name Ex. User name= "Abhishek" is wrong but Username="Abhishek"
4. Indentifier cannot use special character Ex. User$name="Abhishek " is wrong 
5. Indentifier cannot be python keywords (already defined meaning works like if , for , while , class etc..)
6. Indentifier are case sensitive like Username and username are two different Indentifiers.

7* For our conventions make indentifiers readables 


EX. for the GOOD Indentifers :
age = 20
_name = "Abhi"
marks2025 = 88
user_name = "Raj"

Ex. for BAD Indentifers :
1roll = 5         # starts with digit
user-name = "A"   # contains special character
for = 100         # Python keyword

MEMORY TIP JUST IN CASE OF NAMEING INDENTIFERS 
Letter, Underscore, Digits, OnlY ---------------- LUDO
"""




#DAY 2

a,b,c = 18, "Abhishek" , 6.9 #Multiple input in a single line are possible as shown 

a=b=c="Abhishek"  # Multiple variable with the single input Here string type input 
