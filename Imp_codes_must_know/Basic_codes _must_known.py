n=int(input("Enter the no. : "))
for i in range (1,n+1):
    print("*"*i)
      
for i in range (n+1,1 ,-1):
    print("*"*i)
    
for i in range (1,n+1):
    print((n-i)*" ", end ="")
    print(i*"*")

for i in range (1,4):
    for j in range (1,4):
        print(j,end=" ")
    print()
    
for i in range (1,n+1):
    print((n-i)*" ",end=" ")
    print("*"*((2*i)-1))

def info(name, age):
    print(f"Name: {name}, Age: {age}")

info(age=22, name="Abhishek")

x = 10  # Global

def change_x():
    global x
    x = 20  # Modify global x

change_x()
print(x)  # Output: 20
