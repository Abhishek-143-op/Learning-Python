
#Checking a Entered no. is Palindrome or not. 

num = int(input("Enter the no. to check if it is Palindrome or not  : "))
temp_num = num 
rev=0 
while num>0 :
    digit = num % 10 
    rev = rev* 10 + digit
    num //=10 

print(rev)
if temp_num== rev : 
    print(f"The no. is Palindrome no. : {temp_num}")
else:
    print(f"The no. is not a Palindrome no. : {temp_num}")


    
#Create a Palindrome no. 
'''
Logic : Palindrome no. must have 2 or more than 2 digits in it 

we will divide the any random generated no. into half then then mirror the first half to the last half .
EX:
12 

::: we want Palindrome no. for 3 digits 
step 1: divide no. into half(as per no. of digits we want in Palindrome no. )  --> 1___2 
step 2: mirror the 2nd half to the end of no. : (mirroring the 1 into the last )--> 1_2_1 Therefore Palindrome no. 

::: WE want Palindrome no. for 4 digits 
step 1 : Divide no. into half ( as per no. of digits we want in Palindrome no.) --> 12___
step 2 : mirror the first half to the end of no. : 12__21-->1221 (Palindrome no. )

'''

import random 

n= int(input("Enter the no. of digits of which you want to create Palindrome no. : "))

if n==1 :
    print(f"The Palindrome no. is : {random.randint(0,9)}")
elif n==2 :
    print(f"The Palindrome no. is : {(random.randint(1,9))*11}")
elif n==3:
    
    print(f"The Palindrome no. is : ")
    pass
# do it for later ..... 