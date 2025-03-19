#Hailey Sooknanan
#3/18
#Period 5-6
#Challenge 9

import turtle

# Function to turn left by a specified angle (default 90 degrees)
def lt(t, angle=90):
    t.left(angle)

# Function to turn right by a specified angle (default 90 degrees)
def rt(t, angle=90):
    t.right(angle)

# Function to draw a regular n-sided polygon
def polygon(t, length, n):
    # The exterior angle for an n-sided polygon
    angle = 360 / n
    for _ in range(n):
        t.forward(length)  # Move the turtle forward by the given length
        lt(t, angle)       # Turn left by the exterior angle


# Function to draw a square with dynamic side length
def square(t, length):
    for _ in range(4):
        t.forward(length)  # Move the turtle forward by the given length
        t.left(90)          # Turn the turtle left by 90 degrees

# Create a turtle object named 'bob'
bob = turtle.Turtle()

# Call the square function to draw a square with a side length of 150
square(bob, 150)

# Move bob to a different location for the next drawing
bob.penup()
bob.goto(-200, 0)  # Move to the left side of the screen
bob.pendown()



# Move bob to a new location to draw a polygon
bob.penup()
bob.goto(50, 0)  # Move to the right side of the screen
bob.pendown()

# Call the polygon function to draw a 6-sided polygon with a side length of 100
polygon(bob, 100, 6)

# Keep the window open
turtle.done()
