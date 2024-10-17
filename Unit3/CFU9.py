#Hailey Sooknanan
#5-6
#10/17
#Ask user to guess what number will be rolled
import random

x = random.randint(1,6)
plays = int(input("How many rolls do you want to play?"))
print("Amount of rolls: " + str(plays))
def roll_dice():
    score = 0
    guess = int(input("Guess a number from 1-6"))
    print("Dice Rolled!!: "+ str(x))
    print("Your Guess!!: " + str(guess))
    if guess == x:
        print("You guessed correct!!")
        score = score + 6
    else:
        print("You guessed wrong.")
        score = score - 1
    print(score)
    
    
roll_dice()
    
      

