                        #Learning about the input funcion
"""
            Defination:
    The input funtion is used in python for taking the user input from the keyboard as 

-------- --variable = Datatype(input"Enter your input message here like Enter the no. ")----------------------------- 
          |____________________________________________________________________________|
                                                |       
                                                |
                                              VIP
---------------------------------------------------------------------------------------------------------------------

          If we donot use datatype then by default it takes the input as string as shown in above example

"""

name = input ("Enter your name : ")  # Here we donot define the datatype so by default it takes the input as string .

print ("Welcome ,", name )

age = int (input (f"{name},Enter your age : ")) # Here input dataype is defined so it will take input as integer.

if age>18:
 print(name, "You are an adult ")
else:
 print(name, "your are not an adult ")
  
  # OTHERE WAY OF INPUTING THE VARIABLE IN THE STRING :

print(f"Hello, dear ,{name}")
"""                 |----|
                     |
                     here we directly use the variable in the string   

          """

print(
r"""NOTE : 
1.  fstring : fstring is used to embeded the variable , function , class inside the strings 
                     synatax :
                               f"some text {expression}" #placing the f in front of the string 
2. rstring: rstring is used to print the raw Whatever written iside of it . It ignores embeded varible, funtion , class, and escaping 
             sequence like \n , \t etc. 

3. If i find more will be updated . 

""")