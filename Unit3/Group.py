import random
import time

# Function to handle each round of the game
def guess_function(random_num, attempt, start_time, difficulty):
    user_guess = int(input(f"Guess a number between 1 and {difficulty}: "))
    attempt += 1
    
    if user_guess == random_num:
        end_time = time.time()
        print(f"Correct!! Attempts: {attempt}")
        total_time = end_time - start_time
        print(f"Time taken: {total_time:.2f} seconds")
        return attempt
    elif user_guess > random_num:
        print("Too High")
        return guess_function(random_num, attempt, start_time, difficulty)
    else:
        print("Too Low")
        return guess_function(random_num, attempt, start_time, difficulty)

# Function to play multiple rounds
def play_rounds(rounds, difficulty, total_attempts):
    if rounds == 0:
        average_attempts = total_attempts / rounds_input
        print(f"\nGame over! You averaged {average_attempts:.2f} attempts per round.")
    else:
        print(f"\nStarting round {rounds_input - rounds + 1}:")
        random_num = random.randint(1, difficulty)
        start_time = time.time()
        attempts = guess_function(random_num, 0, start_time, difficulty)
        total_attempts += attempts
        play_rounds(rounds - 1, difficulty, total_attempts)

# Main function to start the game
def main():
    global rounds_input
    rounds_input = int(input("How many rounds would you like to play? "))
    difficulty_choice = int(input("Choose difficulty (1: Easy 1-10, 2: Medium 1-50, 3: Hard 1-1000): "))
    
    if difficulty_choice == 1:
        difficulty = 10
    elif difficulty_choice == 2:
        difficulty = 50
    else:
        difficulty = 1000
    
    play_rounds(rounds_input, difficulty, 0)

# Start the game
main()
