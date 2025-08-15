        #Question practice on the Previous concepts. 
print("""Q1. Write a program to create a dictionary of Hindi words with values as their English
translation. Provide user with an option to look it up!\n""")

print("WELCOME Hindi to English Dictinory Translater .\n")
my_dictinory = {
         "madad":"help",
         "chudail": "bitch",
         "gaadi":"car",
         "kursi":"chair",
         "manza": "bed",
         "pankha":"fan",
         "kitab":"book",
         "fulka": "roti",
         "kapda":"clothe"
}

print("The words in my Dictinory are:\n",
      ",".join(my_dictinory.keys()))
word=input("Enter the word you want you want to Translate from hindi to English from dictinory: ").strip().lower()


"""********************** Using try and exect valueError is not efficient code as :*********************
   try and expect will not give value error because checking will give error if word in the dictinory not
   there then it will give key error which means no such key is there in code. 
         Therefore try and except block is useless.

         Insted we can use if else block 

"""
# try:
#     word in my_dictinory
#     print (my_dictinory.get(word))
# except ValueError:
#     print("Invalid input-- The word you enter not in dictinory.\n SORRY!")


#Method 1 : Using if else 
if  word in my_dictinory :
    print (my_dictinory.get(word)) 
else:
    print("Invalid input: \n, Please Enter word from dictinory.(as shown) ")

#Method 2 : Using default dictinory function
print(my_dictinory.get(word, "no such word found!"))

print("""
Q2.  Write a program to input eight numbers from the user and display all the unique
     numbers (once).
""")
User_input = set()
I1=int(input("Enter the unique Integer no. : "))
I2=int(input("Enter the unique Integer no. : "))
I3=int(input("Enter the unique Integer no. : "))
I4=int(input("Enter the unique Integer no. : "))
I5=int(input("Enter the unique Integer no. : "))
I6=int(input("Enter the unique Integer no. : "))
I7=int(input("Enter the unique Integer no. : "))
I8=int(input("Enter the unique Integer no. : "))

User_input.add(I1)
User_input.add(I2)
User_input.add(I3)
User_input.add(I4)
User_input.add(I5)
User_input.add(I6)
User_input.add(I7)
User_input.add(I8)
print("All the Unique no. you Entered will be displayed:\n ",User_input)




print("\nQ3. Can we have a set with 18 (int) and '18' (str) as a value in it?\n")

#****************************Wrong answer : Here I done is directory Not set***********************************************
print("The answer of above question is yes as shown:")
int_dictinory = {18 : "18"}
print(int_dictinory)
#*****************************************************************************************************************

print("The Right Answer is :")
Int_set= set()
Int_set.add(18)
Int_set.add("18")
print(Int_set)





print("Q4. What will be the length of following set s:")
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?
#answer before runing code : According to me -- is 3
#answer after runing code : The Length of the s is 2 I am wrong.


#**********************VIP-Concept***************************
print(len(s))#output is 2.*********because int and float is considered as equal if there values are equal.**********

print("""\n Q5.     p = {}
                What is the type of 's'?
""")
p={}
# Before runing code According to me : s is empty dictinory.
print(type(p))
#After runing code I am right .. Yeahhhh!!!!!!!     :}