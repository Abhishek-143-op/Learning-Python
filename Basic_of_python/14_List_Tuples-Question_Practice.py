            #     Question practice on the list and tuples 

print("""         
1. Write a program to store seven fruits in a list entered by the user.
      """)

fruit = []

f1=input("Enter  fruit in list : ")
fruit.append(f1)
f2=input("Enter  fruit in list : ")
fruit.append(f2)
f3=input("Enter  fruit in list : ")
fruit.append(f3)
f4=input("Enter  fruit in list : ")
fruit.append(f4)
f5=input("Enter  fruit in list : ")
fruit.append(f5)
f6=input("Enter  fruit in list : ")
fruit.append(f6)
f7=input("Enter  fruit in list : ")
fruit.append(f7)

print("The list with the user input : ",fruit)

print("""Q2. Write a program to accept marks of 6 students and display them in a sorted
manner.""")

marks = []

m1=input("Enter the marks of studets  1:")
m2=input("Enter the marks of studets  2:")
m3=input("Enter the marks of studets  3:")
m4=input("Enter the marks of studets  4:")
m5=input("Enter the marks of studets  5:")

marks.append(m1)
marks.append(m2)
marks.append(m3)
marks.append(m4)
marks.append(m5)
print(marks)
print(marks.sort())     #---------|              Here marks.sort() will sort the marks list but will return none,
                        #         |----          as it just sorted and donot return to original string  and 
                        #---------|              without returning to original string we just prints Therefore it returns none.
                       
marks.sort()            #---------|              Here marks sort will sort the marks and return to original list.
print(marks)            #         |                                                  but
                  #  VIP          |              Here marks datatype is string as we donot assign the datatype with input.
                        #         |              so python interpreture will consider lists elements as string.
                        #         |                          and
                        #         |              When we peform the list function like .sort , .count, .etc
                        #         |              Then it will use funtions as string funtion 
                        #         |              as in the above marks.sort()---- it sorts the marks as the string datatype.
                        #---------|                                                  # Ascending order 
"""
If we want to input as the different datatypes (as per our need we need to define with
 the input function)
"""

Markswithintdatatype = []
try:
    marks1=int(input("Enter the marks of studets  1:"))
    marks2=int(input("Enter the marks of studets  2:"))
    marks3=int(input("Enter the marks of studets  3:"))
    marks4=int(input("Enter the marks of studets  4:"))
    marks5=int(input("Enter the marks of studets  5:"))
except ValueError:
    print("Invalid input, Enter the Valid integer value ")


Markswithintdatatype.append(marks1)
Markswithintdatatype.append(marks2)
Markswithintdatatype.append(marks3)
Markswithintdatatype.append(marks4)
Markswithintdatatype.append(marks5)
print("Before sorting :", Markswithintdatatype)
Markswithintdatatype.sort()
print("After sorting the marks:", Markswithintdatatype)
