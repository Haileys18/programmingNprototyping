#Hailey Sooknanan
#3/20
#Period 5-6
#Challenge 11
import turtle
import math
# Function to draw a recursive pattern
def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.forward(length * n)  # Move forward by length * n
    t.left(angle)           # Turn left by angle
    draw(t, length, n-1)    # Recursive call to draw smaller pattern
    t.right(2 * angle)      # Turn right by 2 * angle (100 degrees)
    draw(t, length, n-1)    # Recursive call to draw another smaller pattern
    t.left(angle)           # Turn left by angle to return the turtle to original direction
    t.backward(length * n)  # Move backward by length * n to return to original position

# Function to draw a square with dynamic side length
def square(t, length):
    for _ in range(4):
        t.forward(length)  # Move the turtle forward by the given length
        t.left(90)          # Turn the turtle left by 90 degrees
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
def arc(t, r, angle):
    n = 40  # Number of steps for the arc, can be adjusted for smoother arcs
    circumference = 2 * math.pi * r  # Calculate the circumference of the circle
    arc_length = (angle / 360) * circumference  # Calculate the length of the arc
    length = arc_length / n  # Calculate the length of each step
    sides = int(angle * n / 360)  # Calculate how many steps for the given angle
    
    for _ in range(sides):  
        t.forward(length)  # Move the turtle forward by the calculated length
        t.left(angle / sides)  # Turn the turtle by a fraction of the angle
# Create a turtle object named 'bob'
bob = turtle.Turtle()
bob.speed(0)  # Fastest drawing speed
bob.delay(0.01)  # Reduce delay to speed up the drawing
# Call the square function to draw a square with a side length of 150
square(bob, 150)
square(bob,50)


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
# Call the draw function to create the recursive pattern
draw(bob, 10, 5)
# Test the circle function with different radii
bob.penup()
bob.goto(0,0)  # Move to a smaller location on the left side
bob.pendown()

# Test with radius 50
circle(bob, 50)

# Move bob to a new location to test a larger radius
bob.penup()
bob.goto(0,0)  # Move to a smaller location on the right side
bob.pendown()

# Test with radius 100
circle(bob, 80)

# Move bob to a new location to test an even larger radius
bob.penup()
bob.goto(0,0)  
bob.pendown()

# Test with radius 150
circle(bob, 100)
# Keep the window open

# Call the arc function to draw an arc with a radius of 100 and an angle of 90 degrees
bob.penup()
bob.goto(0, 0)  # Move to a different location on the screen
bob.pendown()

arc(bob, 100, 360)  # Draw an arc with radius 100 and 90-degree angle
turtle.done()
