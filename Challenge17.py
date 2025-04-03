#Hailey Sooknanan
#Period 5-6
#4/3
#Challenge 17-Checking if a is a power of b
# Define a function named is_power that takes two parameters: a and b.
def is_power(a,b):
# This function checks if 'a' is a power of 'b'.
# Base case: if a is smaller than b, it cannot be a power of b.
# If a is less than b, return False because a cannot be a power of b.
    if a<b:
        return False
# Base case: if a equals b, return True because a is b^1.
# If a equals b, then 'a' is exactly 'b' raised to the power of 1.
    if a==b:
        return True
# Recursive case: check if a is divisible by b.
# If a is divisible by b, divide a by b and recursively check if the quotient is also a power of b.
    if a%b==0:
        return is_power(a//b,b)
# If a is not divisible by b, return False because a cannot be a power of b.
    return False
# Test cases:
print(is_power(16,2)) #Test 1: Check if 16 is a power of 2(expected True, since 16 = 2^4).
print(is_power(27,3))#Test 2: Check if 27 is a power of 3 (expected True, since 27 = 3^3).
print(is_power(9,2))#Test 3: Check if 9 is a power of 2 (expected False, because 9 is not divisible by 2).
print(is_power(81,3))#Test 4: Check if 81 is a power of 3 (expected True, since 81 = 3^4).
print(is_power(32,5))#Test 5: Check if 32 is a power of 5 (expected False, because 32 is not divisible by 5).
