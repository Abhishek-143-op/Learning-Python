#                              Nested for loop 

print("""
                for outer_variable in outer_sequence:
                    for inner_variable in inner_sequence:
                              # code block

""")
#Here loops will print the same output in above 2 upcoming codes.

#Nested for loop.
for i in range(1, 4):        # outer loop
    for j in range(1, 4):    # inner loop
        print(f"i={i}, j={j}")

#Nested while loop.
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i={i}, j={j}")
        j += 1
    i += 1

#Mixed for and while nested loop.
for i in range(1, 4):
    j = 1
    while j <= 2:
        print(f"i={i}, j={j}")
        j += 1





"""
Question: print 
*
* *
* * *
* * * *
* * * * *
"""
rows = 4
for i in range(1, rows+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()  # new line after each row


#********************************************NOTE*****************************************************************
print("""                  To print loop content in the same line 
            print(value, end=" ")

               end=" " → adds a space instead of a newline after each print.

                 You can use any string in end, like ",", "-", or even "" (nothing).
""")
#*******************************************************************************************************************




"""
Question : print 
1->1
1->2
1->3

2->1
.
.
.

.
.
5->3
"""
i=1 
while(i<=5):
    j=1
    while(j<=3):
        print(i,"->",j)
        j=j+1
    print()
    i=i+1 

print("""
Write a program to print the following star pattern.
  *
 ***
***** for n = 3
""")
#With normal for loop 
n=3
for i in range (1,n+1):
    print(" "*(n-i),end ="")
    print("*"*(2*i-1))


print("""
Write a program to print the following star pattern.
* * *
*   *  for n = 3
* * *
""")
n=3
for i in range (1,n+1):
    for j in range (1,n+1):
        if i==1 or i==n or j==1 or j==n :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()