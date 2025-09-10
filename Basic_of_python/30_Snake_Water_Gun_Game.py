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
