#Hailey Sookanan
#Period 5-6
#4/8
#Challenge 20-write a Python program by hand to filter words based on forbidden letters.

# Step 1: Define the 'avoids' function
def avoids(word, forbidden_letters):
    # Check if any letter in 'word' is in 'forbidden_letters'
    for letter in word:
        if letter in forbidden_letters:
            return False
    return True

# Step 2: Prompt the user for forbidden letters
forbidden_letters = input("Enter a string of forbidden letters: ")

# Step 3: Define a list of words to process
words = ["apple", "banana", "cherry", "date", "grape", "kiwi", "orange"]

# Step 4: Count how many words do not contain forbidden letters
count = 0
for word in words:
    if avoids(word, forbidden_letters):
        count += 1

# Step 5: Print the total count of words that passed the filter
print(f"Total number of words that passed the filter: {count}")


# Step 1: Define the 'avoids2' function
def avoids2(word, forbidden_letters):
    # Check if any letter in 'word' is in 'forbidden_letters'
    for letter in word:
        if letter in forbidden_letters:
            return False
    return True

# Step 2: Define a predefined list of words
words = ["apple", "banana", "cherry", "date", "grape", "kiwi", "orange"]

# Step 3: Define a list of manually selected combinations of 5 forbidden letters
combinations = [
    "abcde", "fghij", "klmno", "pqrst", "uvwxy",  # Example combinations
    "abcdf", "ijklm", "nopqr", "stuvw", "xyzae"
]

# Function to test the best combination of forbidden letters
def find_best_forbidden_letters():
    min_excluded_count = len(words)  # Start with the worst case (all words excluded)
    best_combination = None

    # Test each combination
    for forbidden_letters in combinations:
        excluded_count = 0
        for word in words:
            if not avoids2(word, forbidden_letters):  # Changed to 'avoids2'
                excluded_count += 1
        
        # Check if this combination excludes fewer words
        if excluded_count < min_excluded_count:
            min_excluded_count = excluded_count
            best_combination = forbidden_letters

    return best_combination, min_excluded_count

# Step 4: Run the function and print the best combination of forbidden letters
best_combination, min_excluded_count = find_best_forbidden_letters()
print(f"The best combination of forbidden letters is: {best_combination}")
print(f"Number of words excluded: {min_excluded_count}")
