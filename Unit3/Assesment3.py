name = input("What is your first name? ")
lname = input("What is your last name? ")
print(f"Hello! {name} {lname}, welcome to the fashion chatbot!!")
import random

def fashion_chatbot():
    print("Let's figure out your fashion preferences.")
    
    # Question 1: Favorite color
    color = input("What is your favorite color to wear? ")
    if color.lower() == "black":
        print("Classic! Black goes with everything.")
    elif color.lower() == "red":
        print("Bold choice! Red always makes a statement.")
    else:
        print(f"{color.capitalize()} is a great choice for a pop of color!")
    
    # Question 2: Casual or formal
    style_preference = input("Do you prefer casual or formal outfits? ")
    if style_preference.lower() == "casual":
        print("Comfort is key, right?")
    elif style_preference.lower() == "formal":
        print("A sharp look never goes out of style.")
    else:
        print(f"{style_preference.capitalize()} sounds like a fun mix!")

    # Question 3: Favorite footwear
    footwear = input("What is your go-to footwear (e.g., sneakers, heels, boots)? ")
    if footwear.lower() == "sneakers":
        print("Sneakers are so versatile and comfy!")
    elif footwear.lower() == "heels":
        print("Heels can really elevate a look!")
    else:
        print(f"{footwear.capitalize()} are a great choice!")

    # Random response (for Question 4)
    random_response = random.randint(1, 3)
    if random_response == 1:
        print("That's in right now!")
    elif random_response == 2:
        print("Wow, so stylish!")
    else:
        print("You're really ahead of the trend!")
    
    # Question 4: Preferred season for fashion
    season = input("Which season do you love dressing for the most (e.g., summer, winter)? ")
    if season.lower() == "summer":
        print("Summer is great for bright colors and breezy outfits!")
    elif season.lower() == "winter":
        print("Winter fashion is perfect for layering and staying cozy.")
    else:
        print(f"Dressing for {season.capitalize()} must be fun!")

    # Question 5: Accessories
    accessory = input("What's your favorite accessory to complete your look (e.g., hats, scarves)? ")
    if accessory.lower() == "hats":
        print("Hats are both stylish and functional!")
    elif accessory.lower() == "scarves":
        print("Scarves add a nice touch of warmth and flair.")
    else:
        print(f"{accessory.capitalize()} really ties the whole look together!")
    
    # Random response (for Question 6)
    random_response = random.randint(1, 3)
    if random_response == 1:
        print("I love that accessory!")
    elif random_response == 2:
        print("It really pulls the outfit together.")
    else:
        print("That’s a fashion statement for sure!")

    # Question 6: Patterns or solids
    pattern = input("Do you prefer patterns or solid colors in your clothes? ")
    if pattern.lower() == "patterns":
        print("Patterns are a fun way to add personality to your outfit!")
    elif pattern.lower() == "solids":
        print("Solid colors give a sleek and classic look.")
    else:
        print(f"Mixing {pattern.lower()} adds a unique touch to your style!")

    print("Thanks for chatting! I hope you have fun with your next outfit choice!")

# Run the chatbot
fashion_chatbot()

