#Hailey Sooknanan
#3/14
#Period 5-6
#Challenge 8
import turtle

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

# Create a turtle object named 'bob'
bob = turtle.Turtle()

# Call the square function to draw a square with a side length of 150
square(bob, 150)

# Move bob to a different location for the next drawing
bob.penup()
bob.goto(-200, 0)  # Move to the left side of the screen
bob.pendown()

# Call the draw function to create the recursive pattern
draw(bob, 10, 5)

# Keep the window open
turtle.done()
