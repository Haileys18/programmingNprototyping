# A program to help count a kid's piggy bank!
# Ask the kid how many coins they have of each type
pennies = int(input("How many pennies do you have? "))
nickels = int(input("How many nickels do you have? "))
dimes = int(input("How many dimes do you have? "))
quarters = int(input("How many quarters do you have? "))
loonies = int(input("How many loonies do you have? "))
toonies = int(input("How many toonies do you have? "))


print("pennies:",pennies)
print("nickels:",nickels)
print("Dimes:",dimes)
print("Quarters:", quarters)
print("Toonies:",toonies)
print("Loonies:",loonies)

# Convert all coins to their value in cents
total_cents = pennies + (5 * nickels) + (10 * dimes) + (25 * quarters) + (100 * loonies) + (200 * toonies)

# Calculate the total amount in dollars and cents
dollars = total_cents // 100  # Integer division to get whole dollars
cents = total_cents % 100  # Remainder gives us the cents

# Display the total in a friendly format
print(f"\nWow! You have a total of ${dollars}.{cents:02d}!")

# Now break down the cents into quarters, dimes, nickels, and pennies
remaining_cents = cents
num_quarters = int(remaining_cents // 25)
remaining_cents = int(remaining_cents % 25)

num_dimes = int(remaining_cents // 10)
remaining_cents = int(remaining_cents % 10)

num_nickels = int(remaining_cents // 5)
remaining_cents = int(remaining_cents % 5)

num_pennies = int(remaining_cents)

# Display the breakdown
print(f"That's {dollars} dollars, {num_quarters} quarters, {num_dimes} dimes, {num_nickels} nickels, and {num_pennies} pennies.")
