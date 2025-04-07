#Hailey Sookanan
#Period 5-6
#4/6

# Define the function `gcd` which takes two parameters `a` and `b`.
# The function calculates the greatest common divisor (GCD) of `a` and `b`.
def gcd(a,b):
# Base case: If `b` is 0, return `a` because the GCD of any number and 0 is the number itself.
# If b is zero, return `a` because gcd(a, 0) = a.
    if b==0:
        return a
# Recursive case: If `b` is not 0, calculate the remainder of `a` divided by `b`.
# Then recursively call `gcd` with `b` and the remainder of `a % b`.
# This step uses the Euclidean algorithm, which states gcd(a, b) = gcd(b, a % b).
    return gcd(b, a%b)
# Test cases:
# Test 1: Call the function with 48 and 18, expected to return the GCD, which is 6.
print(gcd(48, 18))  # Expected output: 6

# Test 2: Call the function with 56 and 98, expected to return the GCD, which is 14.
print(gcd(56, 98))  # Expected output: 14

# Test 3: Call the function with 101 and 10, expected to return 1 since 101 and 10 are coprime.
print(gcd(101, 10))  # Expected output: 1

# Test 4: Call the function with 42 and 56, expected to return the GCD, which is 14.
print(gcd(42, 56))  # Expected output: 14

# Test 5: Call the function with 17 and 13, expected to return 1 since 17 and 13 are coprime.
print(gcd(17, 13))  # Expected output: 1
