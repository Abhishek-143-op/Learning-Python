print("Write a program to find the greatest of four numbers entered by the user.")
num1=int(input("Enter the no. 1 : "))
num2=int(input("Enter the no. 2 : "))
num3=int(input("Enter the no. 3 : "))
num4=int(input("Enter the no. 4 : "))

if num1>=num2 and num1>=num3 and num1>=num4:
    print("no. 1 is Greatest of all. :",num1)
elif num2>=num1 and num2>=num3 and num2>=num4:
    print("no. 2 is Greatest of all. :",num2)
elif num3>=num2 and num3>=num1 and num3>=num4:
    print("No. 3 is Greatest of all. :",num3)
elif num4>=num1 and num4>=num2 and num4>=num3:
    print("No. 4 is Greates of all. :",num4)
else:
    print("Invalid error. ")

#NOTE - Here if we have 2 or more equal input then the python will print block of code which is found true first .
#       as in the above example if num1 and num2 are equal then num1 will be consider greatest instead of num2.




print("""Write a program to find out whether a student has passed or failed if it requires a
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
take marks as an input from the user.
""")
m1=int(input("Enter marks for subject 1:"))
m2=int(input("Enter marks for subject 2:"))
m3=int(input("Enter marks for subject 3:"))
per=(m1+m2+m3)/3

if m1>=33 and m2>=33 and m3>=33 and per>=40:
    print("Your are passed ")
else :
    print("Your are fail. ")




print("""A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
to detect these spams.
""")
spams=input("Enter the input string. : ")
spams.lower()
if "make a lot of money" or "buy now" or "subscribe this" or "click this " in spams:
    print("Your string contain a spams message.")
else:
    print("Your message do not contain a spam message.")


