#Variables for user to input amount of each coin
pennies = int(input("How many pennies do you have?"))
nickels = int(input("How many nickels do you have?"))
dimes = int(input("How many dimes do you have?"))
quarters = int(input("How many quarters do you have?"))
toonies = int(input("How many toonies do you have?"))
loonies = int(input("How many loonies do you have?"))

#outputs the amount of coins for each
print("pennies:",pennies)
print("nickels:",nickels)
print("Dimes:",dimes)
print("Quarters:", quarters)
print("Toonies:",toonies)
print("Loonies:",loonies)

total_value = (pennies + 5*nickels + 10*dime + 25*quarters + 100*loonies + 200*toonies)/100

print("Total value of coins: $" + "{:.2f}".format(total_value))
