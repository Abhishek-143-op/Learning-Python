"""Q1. Write a python function to print first n lines of the following pattern:
            ***
            ** - for n = 3
            *
"""

def pattern(symbol = "*"):
    n=int(input("Enter the no. of rows for pattern (n=3 for above pattern ): "))
    for i in range (n+1,0,-1):
        print(symbol*i)
    return symbol*i
a=pattern ()
print(a)

#                   OR
def pattern(symbol="*"):
    n = int(input("Enter the no. of rows for pattern: "))
    result = ""
    for i in range(n+1, 0, -1):
        result += symbol*i + "\n"
    return result

b= pattern()
print(b)  # prints the full pattern





#Q. Write a python function which converts inches to cms.

def conversion(a):
    conversion_result= a*2.54 #conversion of inch to cm  : ( Ans. )cm = (x)inch * 2.54
    return conversion_result
p=conversion(45)
print(p)