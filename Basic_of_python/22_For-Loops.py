#                                       Basic of  for loops.


print("""
                Learning about the loops :
      
      Loops are required because we want certain line code to be executed untill the condition is true .
       |
       |--- Loops are 2 type in python.
                |
                |--- 1. for loop.
                |       
                |--- 2. while loop.

""")

print("If we want to print 1 to 100 ")

for i in range (1, 101): 

    print (i) # --, --
              #  |   |                              Here concept of step is also there in the loop just like string.
              # start , end 
for i in range (1,10,2):
    print ("with the step we can print only odd no. in 1 - 10:",i)


#print from the lists 
fruits= ["Apple", "Mango", "pineapple", "papaya "]
for i in fruits:
    print(i)

#print from the tuple
tuple=(1,2,3,5,4)
for i in tuple:
    print(i)


#print only keys From the dictinary
dictinary1 = {
    "Abhishek":"Python",
    "Ankit" : "Cpp"
}
for i in dictinary1 :
    print ("Here only keys will be printed :" ,i)

#For printing both keys and value from the dictinary.

for i ,j in dictinary1.items() :
    print ("Here both keys and values will be printed :" ,i,"--->",j)

#similarly in the we can print items from the sets .

for ch in "Python":
    print(ch) 
# Here all the character will be printed in the string = "python "-- here.
