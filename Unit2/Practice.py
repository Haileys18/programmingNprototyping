#Getting the length from the user
length= int(input("What is the length of the rectangle?"))
width= int(input("What is the width of the rectangle?"))
perimeter = 2 * (length + width)
print("The perimeter is " + str(perimeter))

import math
r = int(input("What is the radius of your cirle?"))
C = 2*r*math.pi
A = math.pi*r**2
print("C=" ,C," A=" ,A)

import math
r = int(input("What is the radius of your radius?"))
h = int(input("What is the radius of your height?"))
V = math.pi*r**2*h
print("V=" ,V)


import math 
print("What are the factors of 2x^2 + 6x - 20")
a = int(input("What is the a value: "))
b = int(input("What is the b value: "))
c = int(input("What is the c value: "))
x =int((-b+ math.sqrt(b**2-(4*a*c)))/(2*a))
x2 =int((-b- math.sqrt(b**2-(4*a*c)))/(2*a))
print("The first root is: " +str(x))
print("The second root is: "+ str(x2))
