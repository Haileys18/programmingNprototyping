#Date : 9/24/24
#Period 5-6
#Hailey Sooknanan
#Creating a fun interactive math codes to calculate 2 numbers
# CF3
f_name= input("Please enter first name: ")
l_name = input("Please enter last name: ")
n1 = int(input("Please enter a whole number: "))
n2 = float(input("Please enter a second number: "))

add = n1 + n2
sub = n1 - n2
times = n1 * n2
divide = n1 / n2
remainder = n1 % n2
print("Hello there: " + f_name + " " + l_name + ", Your numbers are: " + str(n1)+ " "+ str(n2))
print("This is the sum of your numbers: " + str(add))
print("This is the difference of your numbers: " + str(sub))
print("This is the product of your numbers: " + str(times))
print("This is the quotient of your numbers: " + str(divide))
print("This is the remainder of your numbers: " + str(remainder))
