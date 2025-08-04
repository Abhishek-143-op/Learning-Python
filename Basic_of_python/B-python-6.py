                        #Learning about the input funcion
"""
            Defination:
    The input funtion is used in python for taking the user input from the keyboard as 

          variable = Datatype(input"Enter your input message here like Enter the no. ") 
          |____________________________________________________________________________|
                                                |       
                                                |
                                              VIP


          If we donot use datatype then by default it takes the input as string as shown in above example

"""

name = input ("Enter your name : ")  # Here we donot define the datatype so by default it takes the input as string .

print ("Welcome ,", name )

age = int (input ("Enter your",name,"age : ")) # Here input dataype is defined so it will take input as integer.

if age>18:
 print(name, "You are an adult ")
else:
 print(name, "your are not an adult ")
  
  