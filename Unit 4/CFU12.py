# Hailey Sooknanan
# Period 5-6
# 10/29
# Asking the user what the password is and if they get it wrong, gives them
# three more tries with one hint per try

guess = 0
user_guess = ""

while user_guess != "simonsnyc" and guess < 3:
    user_guess = input("Enter the password: ")
    guess += 1
    
    if user_guess == "simonsnyc":
        print("Correct! You may enter….")
    elif guess == 1:
        print("Hint: one word connected with 's'.")
    elif guess == 2:
        print("Hint: blue chipmunk from Alvin and the Chipmunks.")
    elif guess == 3:
        print("Hint: The city that has five boroughs.")

if user_guess != "simonsnyc":
    print("You have exceeded the maximum number of attempts.")
