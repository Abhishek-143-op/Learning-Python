#                                            while loop and Control Statements 



#-------------------While loop-----------------------------------------------------------------------
print("""
        While loops are used for executing set of code until the condition is true.
      
      Format:
            Initilization
                While(conditon):
                        code
                updation 
""")
#This code will print Abhishek (5 times) until the condition is false.
i = 1
while i <= 5:
    print("Abhishek")
    i += 1

#countdown timer using while loop
i=10
while i>=1:
    print("Time left: ",i)
    i -=1
print("Time's up!.. ")

#infinite loop if break statement is not used .
while True:
    print("This will run forever")
    break # stopping it using break
  




  #************************************************VIP*************************************************************
#Code for factorial.
n=int(input("Enter the no. you want to factorial: "))
fact=1
while (n>0):
    fact *= n
    n -= 1

print("Factorial: ", fact)

  #************************************************VIP*************************************************************







#-----------------Break----------------------------------------------------------------------------------
print(
"""
 1. Break statement : It used to break or exits the loop at some value or condition .

""")
#Break → exits the loop immediately.
for i in range(10):  #Here initilization is not give as when we use range python automatically create range 0-10 internally if we use while loop we need to define intial value manually.
    if i == 5:
        break
    print(i)
#(Stops at 4)





# ----------------------Continue---------------------------------------------------------------------------------
print("""

2. Continue STatement : It used to skip certain condition of loop in code .
""")

for i in range(10):
    if i == 5:
        continue
    print(i)
#(Skips 5)






#---------------------Pass----------------------------------------------------------------------------------
print("""
3. Pass Statement : It is null statement do nothing in code.
""")
for i in range(5):
    pass   # do nothing for now
print("Loop finished")





#---------------------Special loop---------------------------------------------------------------------------
print("""
      
Special loop : loop with else statement , it runs when loop finishes normally  without break statement 
      
""")
#Here loop finishes normally. 
for i in range(5):
    print(i)
else:
    print("Loop completed! , normally ....")

#Here loop breaks donot finishes normally. 
for i in range (6):
    print(i)
    if i == 3 :
        break
else:
    print("This will be printed if loop finishes normally . ")






#----------------------NOTE-----------------------------------------------------------------------------------
print("""
        else with loops, Break , Continue :

                Works in: for ✅ and while ✅ any of them .

""")
