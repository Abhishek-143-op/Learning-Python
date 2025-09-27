n=int(input("Enter the no. for getting sum of it's digits : "))

sum=0
while n>0:
    digits = n%10
    sum += digits
    n //=10
    
    
print(f"The Sum of the digits in number : {sum}")