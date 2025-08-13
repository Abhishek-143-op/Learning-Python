            #Learning about the function and library 

print("""
Library are like the toolbox which contain the function (like tool ) and 
      function are written in a particular syntax.

Library
 ├── Functions  (do tasks directly)
 ├── Classes    (blueprints)
      └── Objects (real instances)
           └── Methods (functions inside objects)

""")

print (""" How to use the Functions :  
       
        Step 1  Identify the task: Ask "What exactly do I want to do?"
           Example: Want to find the length of a list → Need a counting tool.
           
              
                 Step 2  Check the library’s purpose:
                     Example: math → mathematical operations;
                     os → operating system tasks;
                     string → text manipulation.
      
    *****VIP********        Step 3  Search within the library:(as shown) 
          
                                    ->dir(any_library) : Shows all the library attributes like function , classes, name , variable etc. -----------------only by name.
       
                                   -> help(any_library): Shows detailed documentation of the modules or library--What it is, what it does, and descriptions for all functions/constants.

       """)        
import math
print(dir(math))  # Shows all Attributes in math by name only 
help(math) # Shows detailed description about math library 
print(type(math.sqrt)) 



#********************************************************************************************************************

print("How to recal the Attributes like function ,class, constant etc. ")

print("""
                            You don’t need to remember all functions — only patterns.
      
            1.----------Library_name.function_name(arguments if any )--------------------------->For function calling.
      
            2.----------Library_name.constant_name --------------------------------->For Constant calling.
      
            3.----------object_name = library_name.ClassName(arguments)------------------->For Creating object form Class.

            4.----------Calling specific function without calling specific funtion ------------->(as shown in EX.)
                                  
""")
from math import sqrt, pi
print(sqrt(25),"\nExample for the the calling specific funtion without calling specific function ")   # No need for math.sqrt
print(pi,"\nExample for the the calling specific funtion without calling specific function ")

#********************************************************************************************************************
print("""
                             Universal Rule:

             -->   thing = container.item(parameters)      Where,
                             ->   container = library/module/object,
                             ->   item = function/constant/class,
                             ->   parameters = the data you give it.
      
""")

#*****************************************************************************************************************************************************************************************************************************************
"""                 FOR NOW JUST REMEMBER UNIVERSAL RULE FOR CALLING NAME OF SOMETHING                """            





print("""
Things we should know before calling the Attributes from the library (class , objects, How Objects Differ from Functions,How They Work Together.)---> Leave these for now study later 
      
            1. Class :   A class is a blueprint — it defines:

                  What data something will have (attributes)
                  
                  What actions it can perform (methods, which are just functions inside a class)

""")



