# Question practice on the previous concepts 

print ("Q1.  Write a program to detect double space in a string.")

a="This is string with the  single space  and double space in between somewhere "

if a in "  " :
    print("There is some double space present is somewhere in above string ")
else:
    print("There is no double space present in somewhere in above string ")

print("""--------------ADVANCED QUESTION WITH RESPECT TO SPACE ---------------------------
      \n 
      Q. Show Position of Double Space 
      
      """)
# Take input
text = input("Enter a string: ")

# Find index of double space
index = text.find("  ")  # index = -1 if no double space is there and index = (value no. of time double space is there )

if index != -1:                  #-1 means false : This question is done using string function index used for  finding the character in string.                         

    print("Double space found at position:", index)
else:
    print("No double space found.")

#----------------------------------------NOTE: from previous question ---------------------------------------------------
"""
1. How the positioning of the double space is done in the text variable (string):
                             text = "Hi  there"
                                     01234567 
                        H i _ _ t h e r e
                            ↑↑  
                            double space starts at index 2.

2. Multiple double spaces in the string then Why code print only 1 position of double space ?
      Here in the code the interpreter will stop at lowest index where double space is found if we want to 
      find all the double in the string then we need to use loop statement (not studied yet )
    
3. using the Index function we can find anything in the string and as the Value present in above string 
   we can perform the various tasks like replacing using: replace(old, new ) function
   and many others.


"""

print("\n Q. Replace the double space from the above string  ")

print("Replacing the double space with the single space : ",text.replace( "  " ," " ))
