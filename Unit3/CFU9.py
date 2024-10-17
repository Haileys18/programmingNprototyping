#Hailey Sooknanan
#5-6
#10/17
#Ask user to guess what number will be rolled
import random

def roll_dice():
    score = 0
    # Ask user how many times they want to roll the dice
    plays = int(input("How many rolls do you want to play? "))
    print("Amount of rolls: " + str(plays))
    
    # Loop for the number of plays
    for roll in range(plays):
        x = random.randint(1, 6)  # Generate a random number between 1 and 6
        guess = int(input(f"Roll {roll + 1} - Guess a number from 1-6: "))
        print("Dice Rolled!!: " + str(x))
        print("Your Guess!!: " + str(guess))
        
        # Compare guess with the random dice roll
        if guess == x:
            print("You guessed correct!!")
            score - score + 6  # Add 6 points for a correct guess
        else:
            print("You guessed wrong.")
            score = score - 1  # Subtract 1 point for a wrong guess

    # Print final score after all rolls
    print(f"Final Score: {score}")

# Run the game
roll_dice()
