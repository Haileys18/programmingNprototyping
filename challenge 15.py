#Hailey Sooknanan
#4/1
#Period 5-6
#Challenge 15
import turtle

# Function to draw a Koch curve of a given length
def koch_curve(length):
    if length < 3:
        turtle.forward(length)  # If the length is smaller than 3, just draw a straight line
    else:
        # Otherwise, break it into smaller segments
        length /= 3.0
        koch_curve(length)  # Recursively draw the first third of the curve
        turtle.left(60)  # Turn the turtle left by 60 degrees
        koch_curve(length)  # Recursively draw the second third of the curve
        turtle.right(120)  # Turn the turtle right by 120 degrees
        koch_curve(length)  # Recursively draw the third third of the curve
        turtle.left(60)  # Turn the turtle left by 60 degrees
        koch_curve(length)  # Recursively draw the final third of the curve

# Function to draw a snowflake by drawing three Koch curves
def snowflake(length):
    for _ in range(3):  # Loop 3 times to draw 3 sides of the snowflake
        koch_curve(length)  # Draw a single Koch curve with the specified length
        turtle.right(120)  # Turn the turtle right by 120 degrees to form the snowflake shape

# Create a turtle object named pepito to draw
pepito = turtle.Turtle()

# Create a screen object to control the turtle window
screen = turtle.Screen()

# Set the background color of the turtle graphics window to white
screen.bgcolor("white")

# Set the speed of the turtle to the fastest setting
pepito.speed(0)

# Move the turtle to an appropriate starting position without drawing
pepito.penup()
pepito.goto(0, 90)  # Move the turtle to the top left of the screen
pepito.pendown()

# Draw the snowflake with a side length of 300
snowflake(300)

# Hide the turtle after drawing
pepito.hideturtle()

# Keep the window open until closed by the user
screen.mainloop()
