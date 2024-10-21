#Hailey sooknanan
#Period-5-6
#10/21
#Have the user guess the generated number, give them hints if it is to high or 
#to low while the amount of attempts increase and prints when they are correct
import random
random_num = random.randint(1,10)
    
  
def guess_function(attempt):
    
    user_guess = int(input("Guess a number between 1-10"))
    attempt += 1
    if user_guess == random_num:
        print("Correct!! Attempts: " + str(attempt))
    elif user_guess > random_num:
        print("Too High")
        guess_function(attempt)
    else: 
        print("Too Low")
        guess_function(attempt)
        
guess_function(0)
    
