#Hailey Sooknanan
#3/6
#Period 5-6
#Challenge 5

def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn’t work.")

# Get user input
a = int(input("Enter a positive integer for a: "))
b = int(input("Enter a positive integer for b: "))
c = int(input("Enter a positive integer for c: "))
n = int(input("Enter an integer greater than 2 for n: "))

# Call the function with user input
check_fermat(a, b, c, n)