#Hailey Sooknanan
#Period 5-6
#Thanksgiving motif


import simplegui

# Frame setup
frame = simplegui.create_frame("Thanksgiving Motif", 600, 400)

# List of leaves and their positions for animation
leaves = [(x, y) for x in range(0, 601, 50) for y in range(-400, 0, 50)]

# Helper function to draw the turkey
def draw_turkey(canvas):
    # Feathers (explicitly placed)
    canvas.draw_circle((250, 300), 25, 1, "Red", "Red")
    canvas.draw_circle((260, 280), 25, 1, "Orange", "Orange")
    canvas.draw_circle((280, 270), 25, 1, "Yellow", "Yellow")
    canvas.draw_circle((320, 270), 25, 1, "Green", "Green")
    canvas.draw_circle((340, 280), 25, 1, "Purple", "Purple")
    canvas.draw_circle((350, 300), 25, 1, "Pink", "Pink")
    # Body
    canvas.draw_circle((300, 300), 40, 1, "Brown", "Brown")
    # Head
    canvas.draw_circle((300, 250), 20, 1, "Brown", "Brown")
    # Beak
    canvas.draw_polygon([(295, 245), (305, 245), (300, 235)], 1, "Orange", "Orange")
    # Eye
    canvas.draw_circle((295, 230), 3, 1, "Black", "Black")
    canvas.draw_circle((305, 230), 3, 1, "Black", "Black")
    

# Helper function to draw a pumpkin
def draw_pumpkin(canvas):
    # Pumpkin body
    canvas.draw_circle((500, 350), 30, 1, "Orange", "Orange")
    canvas.draw_circle((470, 350), 25, 1, "Orange", "Orange")
    canvas.draw_circle((530, 350), 25, 1, "Orange", "Orange")
    # Pumpkin stem
    canvas.draw_line((500, 320), (500, 300), 5, "Green")

# Draw handler function
def draw(canvas):
    # Background sky
    canvas.draw_polygon([(0, 0), (600, 0), (600, 400), (0, 400)], 1, "SkyBlue", "SkyBlue")
    # Grass
    canvas.draw_polygon([(0, 350), (600, 350), (600, 400), (0, 400)], 1, "Green", "Green")

    # Draw animated falling leaves
    for i in range(len(leaves)):
        x, y = leaves[i]
        canvas.draw_polygon([(x, y), (x - 5, y + 10), (x + 5, y + 10)], 1, "Orange", "Orange")
        # Move leaves downward
        leaves[i] = (x, y + 2 if y < 400 else -10)  # Reset leaves to top when they exit canvas

    # Draw turkey
    draw_turkey(canvas)
    # Draw pumpkin
    draw_pumpkin(canvas)

# Assign draw handler to the frame
frame.set_draw_handler(draw)

# Start the frame
frame.start()
