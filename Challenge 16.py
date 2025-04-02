#Hailey Sooknanan
#Period 5-6
#4/2
#Challenge 16-Returning parts of a word and checking if its a palndrome
# Function to return the first letter of the word
def first_letter(word):
    # This function takes a string and returns the first character of the string.
    if word:
        return word[0]
    return None

# Function to return the last letter of the word
def last_letter(word):
    # This function takes a string and returns the last character of the string.
    if word:
        return word[-1]
    return None

# Function to return the middle part of the word
def middle_part(word):
    # This function takes a string and returns the substring that excludes the first and last characters.
    if len(word) > 2:
        return word[1:-1]
    return ''

# Function to check if a word is a palindrome
def is_palindrome(word):
    # This function recursively checks if a word is a palindrome.
    
    # Base case: If the word is empty or has one letter, it is considered a palindrome.
    if len(word) <= 1:
        return True
    
    # Recursive case: The function compares the first and last letters of the word.
    if word[0] == word[-1]:
        # If they match, it recursively checks if the middle part of the word is also a palindrome.
        return is_palindrome(word[1:-1])
    else:
        # If the first and last letters don't match, the word is not a palindrome.
        return False

# Test cases
# These tests are used to verify that the is_palindrome function works correctly:
print(is_palindrome("noon"))         # Expected output: True
print(is_palindrome("redivider"))    # Expected output: True
print(is_palindrome("hello"))        # Expected output: False
print(is_palindrome("a"))            # Expected output: True
print(is_palindrome(""))             # Expected output: True
