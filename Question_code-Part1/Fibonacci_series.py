
'''
Fibonacci series : It is the sum of the previous 2 terms where 1st term is 0 and 2nd term is 1.
'''

n= input("Enter n Upto where you want to continue Fibonacci series : ")
a= 0 
b=1
for i range ( 0 , n+1 ):
    print(a,end=" ")
    a= b
    b=a+b