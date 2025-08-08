                         #Learning about the strings.

print("""
String: It is datatype in python and other coding language .
            Which actually is sequence of characters in a quotes ("____"or '____' or """ """)
Strings are primarilly written in 3 ways :
\n 
1.  Inside : single quotes '_____'        -----   need \ for using '' inside string 
2.  Inside : double quotes "_____"        -----   normal 
3.  Inside : triple quotes """"___"""""   -----   multilines strings 
\n
""")
# NOTE :There is no difference between the all these 3 but In the single quotes if we want single quotes in string inside single quoted string then must use \ as shown above 

somestring= 'That\'s string ' # here we use \ to use ' inside the string 


#---------------------------------------STRING SLICING --------------------------------------------
                                      #Day 2 on string 
print("SLICING: means extraction the portion or  substring from the stirng using the indexes.\n ")

"""
Syntax of the string slicing : sl[  start : stop : step ]
      Start : Index where to start the Slicing.
      stop  : Index where to stop the Slicing.
      step  : How many steps to move by default --- 1  .---- it means How many indexes you want in substring like if 
               step is 2 then  substring will exclude every 2nd index from it.
                Therefore it is like condition for including all indexes or not .

                          text = "Python"
                      P   y   t   h   o   n
                      0   1   2   3   4   5   → positive indexes
                     -6  -5  -4  -3  -2  -1   → negative indexes


"""
print ("""
                P  Y  T  H  O  N 
+ve Indexes:    0  1  2  3  4  5 
-ve Indexes:   -6 -5 -4 -3 -2 -1   
       
  To print substring we use   VARIABLE[starting  index : Ending index  ]
                                       |______________|  |____________|
                                            |                 |
                             Starting index is included     Ending index in excluded 
                                  in substring .            (not included) in the string 

""")
s="Abhishek"
print("Now if we want to print substing of above string Abhishek\n")
print("\t \t ", s[0:3])  #It include index 0 to 2 with normal condition inculdint all indexes , here step is default 1
print(" \t \t ", s[0:7:2]) #it will print index 0 to 3 with condition excluding every 2nd index ,here step is 2 (given by us )
print("\t \t ", s[:]) # it include all the index as we are not given starting and ending point to slicing.
print("\t \t ", s[3:]) #it include all the index after the starting index 3 .
print("\t \t ", s[:6]) #it include all the index till the index 6 from the starting.

#Examples for the negative slicing
print(s[-1])   # Output: k
print(s[-2])   # Output: e                                       s = "Abhishek"
print(s[-3:])  # Output: hek                         # Indexes:   A  b  h  i  s  h  e  k
print(s[:-1])  # Output: Abhishe                     # Positive:  0  1  2  3  4  5  6  7
print(s[-6:-2])# Output: hish                        # Negative: -8 -7 -6 -5 -4 -3 -2 -1             

#Example for the negative and reverse slicing 
print(s[::-1])   # Output: kehsihbA
print(s[::-2])   # Output: kseeA
print(s[4::-1])  # Output: sihbA
print(s[-1:3:-1])  # Output: kehs


#Mixing +ve and -ve slicing 
print(s[2:-1])  # Output: hishe
print(s[-6:6])  # Output: hish




#-----------Note 1.: If the starting and stoping is greater than the length then------------------------------------- 
"""                       SPECIAL CASE : """
print(s[10:])     # Output: ''---- nothing or empty string will be printed without showing the error
print(s[2:100])   # Output: 'thon'------- no error start from the index 2 then go the last index if further excedes than it print empty string 


#---------Note 2. : If we are Using the step in the string slicling then that concept is also known as the slicing with skip value
                                                                                                        #  |_____________________|                           
                                                                                                               #      |                
                                                                                                               # Important





print("Length of the string can be using the 'len' keyword")
print (""" 
Length is the total no. of value in the string or total no. of indxes in string starting from the 1
              or 
       total length of the given Identifier 
       
       Little confusing hai but jo bhi hai yehi hai toh thik h chalega 

 """,len(s))

practice="jaidslj;olav aejvyfeo ju"
print(practice[2::3])




                                                                                                               
                                                                       
                                           


