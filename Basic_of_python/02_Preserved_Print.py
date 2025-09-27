# Learning to print in a preserved format 
print ("""Hello , this is 2nd python code. 
and here I am learning to print things like 
text , string , varible etc.. (multi-lines)  
       
     IN A PRESERVED FORMAT      """)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  This also can be done @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

variable = """\n \n  Hello, this is wnd python code. and here I am learning to print 
                         like text, string, variable, etc... (multi-lines)"""
print (variable)# strings can be given to variable 




#Generally we will use the f strings but sometime we will be use to .format() function to make our code more handy
name = "Abhishek"
greeting = "How are you, {}"# Here we are given with the {} further which python put name variable  into it 
name_greeting = greeting.format(name)
print(name_greeting)

#Or 
greeting = "How are you, {name}" #this is not a f string so we use greeting.format(name="Ankit")
name_greeting = greeting.format(name="Ankit")
print(name_greeting)