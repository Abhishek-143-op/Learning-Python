#       Conditional statement : IF STATEMENT



#Normal conditional Statement.
age=int(input("Enter your age:"))
if (age>=18) :
    print("You are an adult.")
else:
    print("You are minor.")




#Leader if-elif statement.
marks=int(input("Enter yours marks :"))
if(marks>=90):
    print("Your grade is A")
elif(marks>=80):
    print("Your Grade is B")
elif(marks>=70):
    print("Your Grade is C")
elif(marks>=80):
    print("Your Grade id D")
else :
    print("Your are Fail.")



#Nested if else statement.
print("Checking voting elgibility.")
Citizen=input("Are you Indian.- Yes/No ")
C=Citizen.lower()
if (age>=18):
    if(C=="yes"):
        print("You are eligible for vote.")
    elif(C=="no"):
        print("you are not elgibile for Vote.")
    else:
        print("Invalid Input!!")
else:
    print("You are not elgible for vote.")


#Short if else statement.
ages=input("Enter your age again.")
print("adult") if ages >=18  else print ("minor")



#Logical operator with conditional statement.
x = 10
if x > 5 and x < 15:
    print("x is between 5 and 15")


#Membetship operatoe with conditional Statement.
fruits = ["apple", "banana", "mango"]
if "apple" in fruits:
    print("Apple is available!")
