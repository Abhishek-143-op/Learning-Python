#                                          Pattern Qustion from the loop 

print("""
                To print loop content in the same line 
            print(value, end=" ")

               end=" " → adds a space instead of a newline after each print.

                 You can use any string in end, like ",", "-", or even "" (nothing).
""")






#Question 1: 
"""
Print a square of stars
Example Output:

* * * *
* * * *
* * * *
* * * *
"""

for i in range (4):
    for j in range (4):
        print("*",end=" ")
    print()






# Question 2.  Print a right-angled triangle of stars:
"""
Example Output:
*
* *
* * *
* * * *
"""
for i in range (4):
    for j in range (0 , i+1):
        print("*",end=" ")
    print()

    
    
    
    
    


    
    #Question 3. Print a number triangle
"""
Example Output:

1
12
123
1234
"""

for i in range (5):
    for j in range (1 , i+1 ):
        print(j,end="")
    print()






    #Question 4 : . Print a reverse number triangle
"""
Example Output:

1234
123
12
1
"""
for i in range (4,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()





 #Question 5 : print the above pattern:
"""
1234
 123
  12
   1
"""
n=4
for i in range(n, 0, -1):       # i controls how many numbers to print
    for j in range(n - i):      # spaces before numbers
        print(" ", end="")
    for k in range(1, i+1):     # numbers from 1 to i
        print(k, end="")
    print()



print("""
Write a program to print multiplication table of n using for loops in reversed
order.
""")
#printing table in a reverse order 
n= int(input("Enter the no. you want to get full table :"))
for i in range (10,0,-1):
    print(n,"* ",i," =",n*i)

# Normal Table using while loop
n=int(input("Enter the no. : "))
i=1 
while i<=10:
    print(f"{n}* {i} ={n*i} ")
    i=i+1

 # multiplication of table using for loop 
n= int(input("Enter the no. : "))
for i in range (1,11):
    print(f"{n} * {i} = {n*i}")



#printing pattern:
print("""
Write a program to print the following star pattern.
  *
 ***
***** for n = 3
""")
#With normal for loop 
n=int(input("Enter the length of pramid (for above pattern enter 3 ):"))
symbol=input("Enter symbol , which can be used to create pyramid :" )
for i in range (1,n+1):
    print(" "*(n-i),end ="")
    print(symbol*(2*i-1))








#printing squre pattern .
print("""
Write a program to print the following star pattern.
* * *
*   *  for n = 3
* * *
""")
n=int(input(r"Enter the no.'-n' (for length of sq. ) :"))
for i in range (1,n+1):
    for j in range (1,n+1):
        if i==1 or i==n or j==1 or j==n :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()






#Factorial clasic question 
print("""
Write a program to calculate the factorial of a given number using for loop.
""")
num= int(input("Enter the no. for factorial: "))
fact=1
for i in range (1,num+1):
    fact=fact*i
print(f"The factorail of no. ,{num} is :",fact)






print("""
Write a program to find the sum of first n natural numbers using while loop.
      
""")
#without loop using maths logic.
sum1=int(input("Enter the 'n' no. Whose sum you want to do : "))
print(sum1/2*((sum1)+(1)))  #sn= n/2{2a+(n-1)d} general formula for sum of series .

#with loop 
# Program to find sum of first n natural numbers using while loop

o = int(input("Enter a positive integer: "))
sum = 0
i = 1
while i <= o:
    sum += i   # add current number to sum
    i += 1     # move to next number
print(f"The sum of first {o} natural numbers is: {sum}")
