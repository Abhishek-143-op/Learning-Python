#Q1.  Question practice on Function and recursion .

print("Write a program using functions to find greatest of three numbers.")

def greatest():
    a=int(input("Enter the no. a : "))
    b=int(input("Enter the no. b : "))
    c=int(input("Enter the no. c : "))

    if a>=b and a>=c :
        print("The greatest no. is : ",a)
    elif b>=a and b>=c:
        print("The greatest no. is : ",b) 
    else:
        print("The Greatest no. is : ",c)
    
greatest()
#                                   OR
def greatest2(a,b,c):

    if a>=b and a>=c :
       return a 
    elif b>=a and b>=c:
        return b
    else:
        return c 
    
print("The Greatest no. using function is : ", greatest2(5,6,64))






#Q2. Write a python program using function to convert Celsius to Fahrenheit

def conversion():
    x= int(input("Enter the temp in celsius : "))
    Fahrenheit= ((9/5)*x) + 32
    return Fahrenheit   
temp= conversion()
print("The Temp in Fahrenheit is : " , temp)






#Q3. Write a recursive function to calculate the sum of first n natural numbers.
def sum(n):
    if n==0:
        return 0
    else :
        return n + sum(n-1)
    
print("The sum of natural no. is :",sum(5))