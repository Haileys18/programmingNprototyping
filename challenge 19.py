#Hailey Sookanan
#Period 5-6
#4/6
#Challenge 19- Creating a function to test if a word has an "e"

def filter_words_without_e(word_list):
    # List to hold words that do not contain 'e'
    words_without_e = []
    
    # Iterate over each word in the list
    for word in word_list:
        if has_no_e(word):  # Call has_no_e function to check each word
            words_without_e.append(word)
    
    # Count the total number of words and the number of words without 'e'
    total_words = len(word_list)
    count_without_e = len(words_without_e)
    
    # Calculate the percentage of words without 'e'
    if total_words > 0:
        percentage_without_e = (count_without_e / total_words) * 100
    else:
        percentage_without_e = 0
    
    # Print the results
    print(f"Words without 'e': {words_without_e}")
    print(f"Percentage of words without 'e': {percentage_without_e:.2f}%")
    
# Define the function has_no_e
def has_no_e(word):
    for letter in word:
        if letter == "e" or letter == "E":
            return False
    return True

# Define a sample list of words to test the function
sample_words = ["hello", "world", "sky", "python", "try", "air", "sun", "cucumber","jack-o-lantern"]

# Call the function with the sample word list
filter_words_without_e(sample_words)
