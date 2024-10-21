#Hailey sooknanan
#Period-5-6
#10/21
#Have the user guess the generated number, give them hints if it is to high or to low

def random_function():
    random_num = random.randint(1,50)

def input_function():
    user_guess = int(input("Guess a number between 1-50"))
  
def guess_function():
    attempts=0
    if input_function == random_function:
        attempts += 1
    
