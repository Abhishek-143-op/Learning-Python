            #Practice program According to the previous codes 

print("\n Q1. --Write a python program to add two numbers.\n")

a=int(input("Enter the number 1 you Want to sum: "))
b=int(input("Enter the number 2 you Want to sum: "))

print("The sum of number 1 + number 2 is :", a+b,"\n")


#--------------------------------------------------------------------------------------------
print ("\n Q2.  --Write a python program to find remainder when a number is divided by z  \n")


try: 
    num1= float(input("Enter the no.1 you want to dividend : "))                      
    z= float(input("Enter the no.2 you want to divisor : "))                                                    

    if (z!=0):
         print("The remainder after dividing 2 no. is :", num1%z)
    else:
        print("The division is not possible as divisor cannot be zero : Invalid choice!!")
except ValueError :
 print("opps! the divisor cannot be zero...\n ")


#---------------------IMPORTANT INFORMATION ABOUT NEW KEYWORDS -------------------------------
"""
try :
    ___something(code)____  -------If there is some code where might unexpected error can occur then this we use try block where if in case we donot get error then the code under the try will execute and if error is there then code under except will be executed 


except ValueError:
    _____if unepected error found this code is occur---- This block is excuted .______

    """

#NOTE : both try and except keywords should be at same level as above other wise code will not be excuted it shows the error .Hence there should be well defined str. of code should be there for proper execution . The str. should look like the as above (Well defined str. means --- What spacing should be  given. )



#-------------------------------------------------------------------------------------------
print("\nQ3. Check the type of variable assigned using input () function.\n")

a=40
b=float(a)
c=str(a)
print(type(a))
print(type(b))
print(type(c))
x=int(input("Enter the no.1 :"))
y=int(input("Enter the no.2 :"))
z=float(x+y)
print("The sum of the no.1 + no.2:",z,"The type() of the datatype in variable (z -- as input in int datatype ) = ",type(z))

#x and y are of type int. Their sum is also an int, but then it is explicitly converted to float using the float() function, and stored in z. Only z is a float, not x or y.


#---------------------------------------------------------------------------------------------
print("\nQ.4: Use comparison operator to find out whether ‘p’ given variable a is greater than ‘q’ or not. Take p = 34 and q = 80\n")

p=34
q=80
if(p>q):
    print("p is greater than q")
else:
    print("q is greater than p ")

#---------------------------------------------------------------------------------------------------
print("\nQ5. Write a python program to find an average of two numbers entered by the user.\n")    

r=int(input("Enter the no.1 for finding the average :"))
s=int(input("Enter the no.2 for finding the average :"))

print("The average of above 2 no. is :",(r+s)/2,"\n")


