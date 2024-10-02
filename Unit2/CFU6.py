import math 
import random
print("Welcome To The Random Number Calculator")
print("I will generate a number between 1 to 100.")
num1 = float(input("Enter a number: "))
num2 = random.randint(1,100)
print(f"\nYour random number is: {num2}")
print(f"Your number you chose is: {num1}")


add = num1 + num2
diff = num2 - num1
product = num2 * num1
divi = num2 / num1
remain = num2 % num1
srqrt = math.sqrt(num2)
power = math.pow(num1, num2)
print("\nResults-")
print(f"The sum of the numbers is: {add}")
print(f"The difference of the numbers is: {diff}")
print(f"The product of the numbers is: {product}")
print(f"The quotient of the numbers is: {divi}")
print(f"The remainder of the numbers is: {remain}")
print(f"The square root of the numbers is: {srqrt}")
print(f"Your number to the power of random number is: {power}")
