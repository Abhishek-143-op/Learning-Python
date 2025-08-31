#                               Learning about the functions 
#Things to understand here is : how to define funtion , What and Why  is return value in funtion and Sometimes why not., Advantages of funtion w.r.t (Exam POV)

print("""
Defination : -A function in Python is a block of reusable code that performs a specific task.
            - It helps in modularity, code reusability, and readability. Functions are executed only when they are called.
🔹 Types of Functions:
        1. Built-in Functions → Already available in Python.
             Example: print(), len(), type(), input().

        2. User-defined Functions → Created by the programmer using the def keyword.
      

🔹 Types of User-defined Functions Examples:   (With respect to parameters )

                   1.  Without parameters, without return
                            Example:
                            def greet():
                                 print("Hello!")
                            greet()

                   2.  With parameters, without return
                             def greet_user(name):
                                 print("Hello", name)
                             greet_user("Abhi")

                    3. With parameters, with return
                              def add(a, b):
                                  return a + b
                              print(add(5, 3))

                    4.Without parameters, with return

                              def pi_value():
                                  return 3.14159
                              print(pi_value())

      
SYNTAX: 
          def function_name(parameters):
        # block of statements
        return value  # optional
      
                                  (a) --def → keyword to define a function.
                                  (b) --function_name → identifier for the function.
                                  (c) --parameters → inputs to the function (optional).
                                  (d) --return → outputs from the function (optional).
      
Why In function we req. return value and why not in some cases :
      
      1.  Without return → Useful when only performing a task (printing, displaying info, saving to file).

      2. With return → Useful when the output needs to be used later in calculations or logic.

🔹 Advantages of Functions : 

                Reusability → Code can be used multiple times.
                Modularity → Breaks program into smaller units.
                Readability → Easy to understand and maintain.
                Reduced Code Size → Avoids repetition.
                Debugging → Errors can be traced easily.
""")

#normal function and function calling 
def greet():
    print("Hello, Dear !! ")   
greet()


#Greet person with username
def greet_user(name):
    print("Hello ,", name )
greet_user("Abhishek")


#adding the 2 no. using the function 
def add(a, b):
    return a + b   
print("The sum of a + b is : " , add(5,3))

#defining constant value using the function 
def pi_value():
    pi=3.14
    return pi
print("The value of pi is : ",pi_value())





#function Example  with the exam POV :
def factorail(a):
    fact=1 
    for i in range (1,a+1):
        fact *= i
    return fact 
print("The factorial of no. using funtion is : ", factorail(5))





#Function with default parameter value :
def second_greet(name = "Stranger") :
    gr= "Welcome " + name 
    return gr
z= second_greet() #Here if we donot add any other value then it will take name = Stranger (By Default)

print (z)