#Hailey Sooknanan
#Period 5-6
#4/22
#Challenge 23- Write a python program by hand that checks if the letters in a word appear in alphabetical order.

# Step 1: Define the function
def is_abecedarian(word):
    # Convert the word to a list of characters and compare with sorted version
    return list(word) == sorted(word)

# Step 2: Test the function with some examples
print(is_abecedarian("abc"))        # True
print(is_abecedarian("aegilops"))   # True
print(is_abecedarian("art"))        # True
print(is_abecedarian("loop"))       # True
print(is_abecedarian("telephone"))	# False
print(is_abecedarian("knife"))		# False


# Step 3: Count how many abecedarian words are in a list
word_list = [
    "abc", "aegilops", "art", "almost", "biopsy", "billowy",
    "chintz", "abhors", "accent", "access", "loop", "buzz", "def", "ace"
]

count = 0

for word in word_list:
    if is_abecedarian(word):
        count += 1

print("Number of abecedarian words:", count)




