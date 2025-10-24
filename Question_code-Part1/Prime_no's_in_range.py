num= int(input("Enter the no's for checking wether is it prime or no. : "))

if num <=1 :
    print(f"The no. {num} is not prime ")

for i in range (1,num+1):
    if num%i==0 :
        print(f"The no. {num} is not prime. ")
    else: 
        print("The no. is prime . ")
        
        
        #do it for later >>>>>>>>>>>>>>>>>>>..