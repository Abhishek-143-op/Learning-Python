#----------------------Advanced question practice 2.
'''
The game() function in a program lets a user play a game and returns the score
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.
'''

import random 
import os 


#creating function named game ()
def game():
    num_to_guess = random.randint(1,20)
    
    attempts = 0
    print("Welcome to number guessing game  ")
    print("\n Rules of the game : ")
    print("""\n 
                computer will guess the 1 no. Between 1-20 
                and you will also guess the no. between 1-20 
                if your guess =computer guess you win 
                The lesser no. of attempt you take to guess no.
                the more will be your high score . \n
          """)
    
    while True:                 #while Ture will create infinite loop untill we break 
        try:                    #Used to Handle unexpected value error 
            userguess = int(input ("Enter the no. between 1-20 : "))
            
            if userguess<=20:  

                    #Logic of the game and information for better functionality.
                print("Computer guess is : ",num_to_guess )
                print("Your guess is : ", userguess)
                attempts +=1 


                if userguess>num_to_guess:
                    print("Try Again !! Your Guess is too high ")
                elif userguess < num_to_guess  :
                    print("Try Again !! Your Guess is too low ")
                else:
                    print(f"CONGRATULATION... , You Guessed the no. in {attempts} attempts .")
                    break


            else :
                print("You Entered no. above 20 , Please Enter no. Between 1-20 ")
        except ValueError:
            print("Something went Wrong ....")

#Here showing the score of the User  below 
    score= max(20-attempts+1,0) #Here we use Max Because we not want score in negative max score should be 0 
    print("Your score is : ",score,"\n")
    return score 


#Here we create file and folder for storing the high score 
hi_score_file = "Basic_of_python-02/random folder-for_files/high_score_file"
if os.path.exists(hi_score_file ):
    with open (hi_score_file,'r') as f:
        content= f.read().strip()
        if content.isdigit():
            high_score= int(content)
        else:
            high_score= 0         
else:
    high_score=0
print(f"Previous high score is : {high_score}")

        
new_score=game()

if new_score > high_score:
    print(" New Hi-score achieved!")
    with open(hi_score_file, 'w') as file:
        file.write(str(new_score))
else:
    print("Keep trying to beat the Hi-score!")

print(f" Current Hi-score: {max(new_score, high_score)}")

