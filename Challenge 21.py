#Hailey Sookanan
#Period 5-6
#4/10
#Challenge 21-Write a python program by hand that checks if a word contains only a specific set of letters.

def uses_only(word, allowed):
    """Returns True if the word contains only letters from the allowed set."""
    for x in range(len(allowed)):
        if word[x] == allowed[x]:
            return True
    return False
# Test cases
print(uses_only("hello", "b"))       # True (all letters in 'hello' are in 'helo')
print(uses_only("world", "c"))       # False (missing 'r' in allowed)
print(uses_only("apple", "o"))       # True
print(uses_only("banana", "ban"))       # True
print(uses_only("grape", "grap"))       # False (missing 'e')
