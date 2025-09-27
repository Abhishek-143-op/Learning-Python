#Q Write a python code to reverse a no. 123 --> 321 


#*************************************************************************************************************
#CODE 1 :::  Here in this code preeceding 0 will be neglected ( if contained in num):::: 

num1 = int(input("Enter the no. you want to rev : ")) # will be used for code 1 and code 2 both . 


temp= num1 # we creating this temp variable because if we directly use num1 in CODE 2 then num1 ==0 while code1 is executed so always if block (num1==0 ): print("0") will be worked instead of else code 


rev= 0
while num1> 0 :
    digit1 = num1 %10 
    rev = rev* 10 + digit1 
    num1 = num1 // 10  # Here code will be ended when num1 == 0 therefore we cannot directly use num1 in code 2. 
print(f"The reveresed no. without preeceding 0's : {rev}")
    
    
    
#*************************************************************************************************************


#CODE 2 ::: Here in this code preeceding 0 will not be neglected ( if contained in num) ::::

rev_str =""
if temp == 0 :
    print("0")
else:
    while  temp>0:
        digit2 = temp %10
        rev_str += str(digit2)
        temp //=10 
    print(f"The reversed no. with preeceding 0's included : {rev_str}")



'''
                        Use of this above code in real life problems :

1. Real-Life Applications LOGIC BUILDING ::: 

(a) Palindrome Checks :
        Many apps require checking if a number is a palindrome (same forwards & backwards).
        Example: Bank systems, ticket numbers, or ID verification.

(b) Number-Based Puzzles & Games :
        Reverse a number logic is used in games or educational apps to create challenges.
        Digital Security & Encryption

(c) Some encryption schemes or hashing mechanisms might reverse digits as part of scrambling data.
    Mathematical Calculations :
        Calculating mirrored numbers, lucky numbers, or special sequences in finance, lottery systems, or coding competitions.

(d) Data Transformation in Devices :
        In calculators, embedded systems, or microcontrollers, reversing digits might be used for display formatting or processing sensor IDs.
    
2. Web Development Use Cases :::

(a) Form Validation & Data Processing :
        You might reverse user input numbers for validation, like checking credit card or ticket IDs.

(b) Interactive Number Games in Browser :
        E.g., build a “Guess the Number” game, or educational apps that teach math by reversing numbers.

(c) Sorting / Ranking Visualization :
        Reversing numbers could help in reversing leaderboard positions for UI display.

(d) Data Transformation Before Display :
        Sometimes you need to reverse numeric IDs for front-end formatting or creating “mirrored effects” in UI.

(e) Algorithm Demonstrations / Coding Platforms :
        On web apps like CodePen or JSFiddle, reversing a number is a common example to teach loops, modulus operations, and string/number manipulations.
'''