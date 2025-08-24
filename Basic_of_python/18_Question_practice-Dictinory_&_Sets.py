print("""Q1. Create an empty dictionary. Allow 4 friends to enter their favorite language as
value and use key as their names. Assume that the names are unique \n""")

Fav_Lang={}
Friend1=input("Enter the name of Friend 1:")
Language1=input("Enter your fav language:")

Friend2=input("Enter the name of Friend 2:")
Language2=input("Enter your fav language:")


Friend3=input("Enter the name of Friend 3:")
Language3=input("Enter your fav language:")


Friend4=input("Enter the name of Friend 4:")
Language4=input("Enter your fav language:")



Fav_Lang[Friend1]=Language1
Fav_Lang[Friend2]=Language2
Fav_Lang[Friend3]=Language3
Fav_Lang[Friend4]=Language4

print(Fav_Lang)

"""
**********************************************NOTE*****************************************************************
-If the Name of friend is same (keys are same) : Then the friend name is overwritten to the newest Name Entered     value (Key)
               Hence: Keys in the dictinory should be unique if not then overwritten.
-It is not necessary to have a unique value just key should be necessary
*********************************************************************************************************************
"""

print("""Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}""")

#s = {8, 7, 12, "Harry", [1,2]}
#           |
#           |
#           |
# Here we will error as set's elements should be immutable (cannot be changed). Therefore ERROR!!!