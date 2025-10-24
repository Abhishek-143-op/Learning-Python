# Write the code to compare graetest of 3 no.'s ?

num1 = int(input("Enter the no. 1 for comparison : "))
num2 = int(input("Enter the no. 2 for comparison : "))
num3 = int(input("Enter the no. 3 for comparison : "))

if num1> num2 and num1 >num3 : 
    print(f"Num1 {num1} is the greatest of all . ")
    
    
elif num2> num1 and num2 >num3 : 
    print(f"Num3 {num2} is the greatest of all . ")
    
    
elif num3> num2 and num3 >num1 : 
    print(f"Num3 {num3} is the greatest of all . ")
    
else:
    print("something went wrong!!...")