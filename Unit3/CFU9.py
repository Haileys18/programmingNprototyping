#Hailey Sooknanan
#5-6
#10/17
#Ask user to guess what number will be rolled
import random
num_rolls = int(input("Let's play dice! How many rolls do you want to play?"))


def guess(total):
     user_guess = int(input("What number do u think you rolled?"))
     random_num = random.randint(1,6)
     roll = random_num
     print("You guessed: " + str(user_guess) + " Dice rolled: " + str(roll))
     if user_guess == roll:
        total += 6
     else:
        total -= 1
        return total

def rolls(num_rolls, total = 0):
    if num_rolls == 0:
        return total
    else:
        total = guess(total)
        return rolls(num_rolls-1, total)

total = 0
final_total = rolls(num_rolls, total)
print("Your score is: " + str(final_total))
    
