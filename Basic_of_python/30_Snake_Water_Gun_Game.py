import random
choices = ['s', 'w', 'g']

comchoice = random.choice(choices)

# User input
userchoice = input("Enter your choice (S = Snake, W = Water, G = Gun): ").lower()

print(f"Computer chose: {comchoice}")

# Check for tie
if userchoice == comchoice:
    print("It's a Draw!")

# Snake vs Water
elif userchoice == 's' and comchoice == 'w':
    print("You Win! Snake drinks Water.")

# Water vs Gun
elif userchoice == 'w' and comchoice == 'g':
    print("You Win! Water damages Gun.")

# Gun vs Snake
elif userchoice == 'g' and comchoice == 's':
    print("You Win! Gun kills Snake.")

# Cases where computer wins
elif comchoice == 's' and userchoice == 'w':
    print("Computer Wins! Snake drinks Water.")

elif comchoice == 'w' and userchoice == 'g':
    print("Computer Wins! Water damages Gun.")

elif comchoice == 'g' and userchoice == 's':
    print("Computer Wins! Gun kills Snake.")

# Invalid input
else:
    print("Invalid input! Please choose S, W, or G.")



#-----------------------------------------------------OR--------------------------------------------------------------


"""
In such games and codes sometime we create patterns like here for wining and losing : due to which we 
can replace multiple lines of codes with very few lines which make code simpler but complex to the(USER-who codes) new person 
completely unfamilar with code . 

Which can be efficient in some cases (Here in this code there is no pattern as code is written in well defined 
any user understand able way . :} )

"""
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]

# By now we have 2 numbers (variables), you and computer

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("Its a draw")

else:
    '''
     if(computer ==-1 and you == 1): (computer - you) = -2
        print("You win!")

    elif(computer ==-1 and you == 0): (computer - you) = -1
        print("You Lose!")

    elif(computer == 1 and you == -1): (computer - you) = 2
        print("You lose!")

    elif(computer ==1 and you == 0): (computer - you) = 1
        print("You Win!")

    elif(computer ==0 and you == -1): (computer - you) = 1
        print("You Win!")

    elif(computer == 0 and you == 1): computer - you) = -1
        print("You Lose!") 

        The below logic is written on the basis of the value of computer - you
 
    '''
    if((computer - you) == -1 or  (computer - you) == 2 ):
        print("You lose!")
    else:
        print("You win!") 