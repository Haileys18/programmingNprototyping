#Hailey Sooknanan
#4/1
#Period 5-6
#Challenge 12-Creating a flower
import turtle
import math

def draw_petal(t, radius, angle):
    t.begin_fill()
    arc(t, radius, angle)
    t.left(180 - angle)
    arc(t, radius, angle)
    t.left(180 - angle)
    t.end_fill()

def draw_flower(t, petals, radius):
    t.fillcolor("pink")  # Set petal color
    angle = 360 / petals
    for _ in range(petals):
        draw_petal(t, radius, 60)
        t.right(angle)

def arc(t, r, angle):
    n = 40  # Number of steps for the arc
    circumference = 2 * math.pi * r
    arc_length = (angle / 360) * circumference
    length = arc_length / n
    sides = int(angle * n / 360)
    
    for _ in range(sides):
        t.forward(length)
        t.left(angle / sides)

def circle(t, radius):
    circumference = 2 * math.pi * radius
    n = 36  # Approximate a circle with 36 sides
    length = circumference / n
    polygon(t, length, n)

def polygon(t, length, n):
    angle = 360 / n
    for _ in range(n):
        t.forward(length)
        t.left(angle)




bob = turtle.Turtle()
bob.speed(0)
    
# First Flower
bob.penup()
bob.goto(0, -100)
bob.pendown()
draw_flower(bob, 7, 550)
#Second Flower
bob.penup()
bob.goto(0, 100)
bob.pendown()
draw_flower(bob,11,550)
#Third flower
bob.penup()
bob.goto(0, 50)
bob.pendown()
draw_flower(bob,21,550)
    
   
    
    
turtle.done()

