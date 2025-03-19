#Hailey Sooknanan
#3/18
#Period 5-6
#Challenge 10

import turtle
import math

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

# Function to draw an approximate circle using the polygon function
def circle(t, radius):
    # Calculate the circumference of the circle
    circumference = 2 * math.pi * radius
    
    # Choose a number of sides for the polygon approximation
    n = 36  # More sides = closer to a perfect circle
    length = circumference / n  # Calculate the side length for the polygon
    
    # Draw the circle using the polygon function
    polygon(t, length, n)

# Function to draw a square with dynamic side length
def square(t, length):
    for _ in range(4):
        t.forward(length)  # Move the turtle forward by the given length
        lt(t, 90)          # Turn the turtle left by 90 degrees

# Create a turtle object named 'bob'
bob = turtle.Turtle()
bob.speed(0)  # Fastest drawing speed
bob.delay(0.01)  # Reduce delay to speed up the drawing

# Test the circle function with different radii
bob.penup()
bob.goto(-100, 0)  # Move to a smaller location on the left side
bob.pendown()

# Test with radius 50
circle(bob, 50)

# Move bob to a new location to test a larger radius
bob.penup()
bob.goto(50, 0)  # Move to a smaller location on the right side
bob.pendown()

# Test with radius 100
circle(bob, 100)

# Move bob to a new location to test an even larger radius
bob.penup()
bob.goto(0, -100)  # Move to a smaller location below the center
bob.pendown()

# Test with radius 150
circle(bob, 150)

# Keep the window open
turtle.done()
