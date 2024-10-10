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
