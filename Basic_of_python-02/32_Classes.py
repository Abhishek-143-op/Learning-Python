#---------------------------------Classes-----------------------------------------------------------
'''
Classes : It is the blueprint of the method also known as the template.


Syntax : 
            Class Class_name :
                    #code 
                    
Important terms about the class 
1. Objects : Specific intstance or class also known as the instance .

        Dog= Animals() ----> Here Dog is the object or instance of the class Animals .
        Cat= Animals() ----> Here Cat is the other object or instance of the class Animals.
        
2. Attributes : Variable  that belongs to the class or objects .

        Ex...
            Class Animals () :  # ---- > Animals class 
                def __init__(self, species , color): 
                    self.species = species
                    self.color = color 
        
3. Method : A method is function defined inside a class 
        Ex...
             Class Animals () :  # ---- > Animals class 
                def __init__(self, species , color): 
                    self.species = species
                    self.color = color 
        
                def describe (self):
                    print(f"This is a {self.color} {self.species}")
            
4. Constructor : Special method used to inilize the attribute when the object is created 
        Syntx : 
                def __init__( self, Attribute1 , Attribute2 ):
                
        If Not Created then What happened : 
                -Python automatically create  default constructor contain only sef attribute.  
                -It donot initilize any other attribute . 

5. Self : Refer to current instance of the class . 
            Used to access the attribute and methods in the class 
            
'''

#Attributes : 
class Animals () :  # ---- > Animals class 
    
                #This __init__(): is known as the constructor 
                def __init__(self, species , color): 
                    
                    #self : It is the attribute used to access the other attributes/ Method  of the class
                    self.species = species   # Attribute 1 
                    self.color = color       # Attribute 2 
                    
                    #This is known as the method 
                def describe (self):
                    print(f"This is a {self.color} {self.species}")
            
                    
                    
                    
# Dog is instance or object of Class Animals                    
Dog=Animals("Dogs", "borwn")   
print(Dog.species)             
print(Dog.color)

# Real life Examplar of class : 

class Bank_Account ():
    
    def __init__(self, Account_holder_name , balance = 0 ):
        self.Account_holder_name =Account_holder_name
        self.balance = balance
        
    def deposite (self , amount):
        self.balance += amount 
        print(f"Your account balance is {self.balance}")
        
    def withdrawl (self , amount):
        self.amount= amount
        if amount <= self.balance :
             self.balance -= amount 
             print(f"Your account balance is {self.balance}")
        else:
             print("Insufficient balance !! ")
             
    def Info (self):
        print (f"Account holder name : {self.Account_holder_name} and balance : {self.balance}")
             
Ankit = Bank_Account("Ankit",1000 )
Ankit.deposite(500)
Ankit.withdrawl(300)
Ankit.Info()