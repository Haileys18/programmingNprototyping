#Hailey Sooknanan
#4/1
#Period 5-6
#Challenge 13-Creating hexagons
import turtle
import math

def draw_polygon(t, sides, size):
    """Draws a regular polygon and returns the list of vertex positions."""
    vertices = []  # Store vertex coordinates
    angle = 360 / sides  # Exterior angle of the polygon

    for _ in range(sides):
        vertices.append(t.pos())  # Save the current position
        t.forward(size)
        t.right(angle)

    return vertices  # Return the list of vertex positions

def draw_polygon_star(t, sides, size):
    """Draws a polygon and connects its center to each vertex."""
    t.penup()
    t.goto(-size / 2, (math.sqrt(3) / 2) * size / 3)  # Adjust starting position
    t.pendown()

    # Get the vertices of the polygon
    vertices = draw_polygon(t, sides, size)

    # Calculate the true center of the polygon
    center_x = sum(v[0] for v in vertices) / sides
    center_y = sum(v[1] for v in vertices) / sides
    center = (center_x, center_y)

    # Draw lines from the center to each vertex
    t.penup()
    t.goto(center)  # Move to center
    t.pendown()

    for vertex in vertices:
        t.penup()
        t.goto(center)  # Move to center
        t.pendown()
        t.goto(vertex)  # Draw line to vertex

# Set up the turtle
bob = turtle.Turtle()
bob.speed(0)



# Draw a hexagon figure
draw_polygon_star(bob, 8, 50)


# Finish drawing
turtle.done()

