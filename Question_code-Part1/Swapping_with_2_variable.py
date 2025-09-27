#Q1. Write a python code to swap a 2 no. without using the third variable .


#In this code preceeding 0 will be neglected . 
num1 = int(input("Enter the no. 1 : "))
num2 = int(input("Enter the no. 2 : "))
print(f"Before swapping ::\nnum1 : {num1}\nnum2 : {num2}")

#Swaping logic . 
num1 , num2 = num2, num1 
print(f"After swapping :: \n num1 : {num1}\n num2 : {num2}")

'''
Where can I use this code in real life :::

1.Sorting : Used in the sorting the data.
2.Low end devices : 3rd variable takes space , So in the memory limited devices we use this code.
3.cryptography : some encryption algo use this logic for cryptography .
4.Game dev : In the cordated games we use this code to quickly update the coordinates of the players. 
5. Low level system : In low level system registers are limited therefore we use swaping without 3rd variable .

6. IN WEB DEV : Drag and drop feature use this logic to swaping the file position to other. 
'''