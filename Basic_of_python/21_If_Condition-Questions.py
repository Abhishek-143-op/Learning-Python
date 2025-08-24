print("""
Write a program to find whether a given username contains less than 10
characters or not.
""")
username= input("Enter Your Username : ")
if len(username)>=10:
    print("Your Username contain 10 characters.")
else:
    print("Your Username contain characters less than 10.")


print("""
      Write a program which finds out whether a given name is present in a list or not.
""")
username_list=["Abhishek","Ankit","Tushar","Vansh","Suresh","Abhay thakur","prince", "Abhishek dogra", "Abhinav", "Abhinay","Vishant"]
Username=input("Enter the Username to check in list : ")

if Username in username_list :
    print("The Entered Username is in the List.")
else:
    print("The Entered Username not in the List. ")

    