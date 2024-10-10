#Hailey Sooknanan
#10/10/2024
#Period 5-6
#Creating two functions to find the sum of three numbers and average of the three numbers the user inputs.
x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
z = int(input("Enter a number: "))

def sum_function():
    add = x + y + z
    print("The sum of all yours numbers is: " + str(add))
    return add
def avg_function():
    divide = (x + y + z) / 3
    print("The average of all yours numbers is: " + str(divide))
    return divide

sum_function()
avg_function()
