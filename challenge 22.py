#Hailey Sookanan
#Period 5-6
#4/10
#Challenge 22-write a Python program by hand that checks if a word contains only a specific set of letters.

# This function checks if a word contains all required letters
def uses_all(word, required):
    i = 0
    while i < len(required):
        j = 0
        while j < len(word):
            if required[i] == word[j]:
                break
            j = j + 1
        if j == len(word):
            return False
        i = i + 1
    return True



# Test cases
print(uses_all("education", "aeiou"))      # True
print(uses_all("facetiously", "aeiouy"))   # True
print(uses_all("hello", "aeiou"))          # False
print(uses_all("sequoia", "aeiou"))        # True
print(uses_all("rhythm", "aeiouy"))        # False

# Sample word list
word_list = ["education", "facetiously", "hello", "sequoia", "rhythm", "automobile", "questionably", "authority"]

# Counters
count_aeiou = 0
count_aeiouy = 0

# Loop through words
word_index = 0
while word_index < len(word_list):
    word = word_list[word_index]
    word = word.lower()

    if uses_all(word, "aeiou"):
        count_aeiou = count_aeiou + 1

    if uses_all(word, "aeiouy"):
        count_aeiouy = count_aeiouy + 1

    word_index = word_index + 1

# Print the results
print("Words with all vowels (a, e, i, o, u):", count_aeiou)
print("Words with all vowels (a, e, i, o, u, y):", count_aeiouy)
