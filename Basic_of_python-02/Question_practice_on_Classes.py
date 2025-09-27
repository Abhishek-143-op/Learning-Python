
#Q1.  Create a class “Programmer” for storing information of few programmers working at Microsoft.

class programer():
    def __init__ (self, name , language):
        self.name = name 
        self.language = language 
        
    def info(self):
        print(f" {self.name} working at microsoft . \n specialized in {self.language}")
        
        
Employee1 = programer("Abhishek","Python")
Employee1.info()

Employee2 = programer("Ankit", "cpp")
Employee2.info()

Employee3 = programer("Tushar", "cpp")
Employee3.info()

Employee4 = programer("Krish", "Java")
Employee4.info()



#q2.   Write a class “Calculator” capable of finding square, cube and square root of a number.

class Calculator() :
    
    def __init__ (self, num1 ):
        self.num1= num1
    
    #finding Square 
    def square (self):
        print(f" {self.num1*self.num1}")
    
    #finding cube
    def cube (self):
        print(f" {self.num1*self.num1*self.num1}")
    
    #finding sq root
    def sq_root(self):
        print(f" {self.num1**(1/2)}")
    
calculation1 = Calculator(4)
calculation1.square()
calculation1.cube()
calculation1.sq_root()



#Q3.   Create a class with a class attribute a; create an object from it and set ‘a’
#       directly using ‘object.a = 0’. Does this change the class attribute?

class myclass :
    a=10  # class attribute a from myclass 


#creating an object 'a1' from the myclass
a1= myclass()

#setting the value of 'a'  using the object 
a1.a=0 

print (f"attribute a using only class : {myclass.a}")
print(f"attribute a  using a1.a : {a1.a}")
    
    
#Q4.   Add a static method in problem 2, to greet the user with hello.

class Calculator() :
    
    @staticmethod 
    def greet():
        print("Hello every one ! \n Nice to meet you...")
    
    
    def __init__ (self, num1 ):
        self.num1= num1
    
    #finding Square 
    def square (self):
        print(f" {self.num1*self.num1}")
    
    #finding cube
    def cube (self):
        print(f" {self.num1*self.num1*self.num1}")
    
    #finding sq root
    def sq_root(self):
        print(f" {self.num1**(1/2)}")
        
        
Calculator.greet()    
calculation1 = Calculator(4)
calculation1.square()
calculation1.cube()
calculation1.sq_root()
