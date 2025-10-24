#Student Grading system : 

sb1= int(input("Enter the marks of subject 1 : "))
sb2= int(input("Enter the marks of subject 2 : "))
sb3= int(input("Enter the marks of subject 3 : "))
sb4= int(input("Enter the marks of subject 4 : "))


total= sb1+sb2+sb3+sb4
per= total/4

if sb1>=33 and sb2 >=33 and sb3>=33 and sb4>=33:
    if per>=90:
        print("Your Grade is : A ")
    elif per>=80:
        print("Your Grade is : B ")
    elif per>=70:
        print("Your Grade is : C ")
    elif per>=60:
        print("Your Grade is : D ")
    elif per>=50:
        print("Your Grade is : E ")
    elif per>=33:
        print("Your Grade is : P (Pass)")
    else :
        print("Your failed Exam !!.. ")
    
else: 
    print("You Failed the Exam!!.. ")