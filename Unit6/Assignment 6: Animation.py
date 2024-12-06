#Hailey Sooknanan
#12/5
#Period 5-6
#Animation assignment- Child builds a snowman
import simplegui
import random

# Global variables
progress = 0
num_snowflakes = 50  # Fixed number of snowflakes
snowflakes = [(0, 0)] * num_snowflakes  # Initialize list

# Initialize snowflakes
def init_snowflakes():
    global snowflakes
    for i in range(num_snowflakes):
        snowflakes[i] = (random.randint(0, 400), random.randint(0, 500))

# Draw handler
def draw(canvas):
    global progress, snowflakes

    # Snowflakes falling
    for i in range(num_snowflakes):
        x, y = snowflakes[i]
        canvas.draw_circle((x, y), 2, 1, "White", "White")
        # Update position to fall downward
        snowflakes[i] = (x, y + 2 if y < 500 else -10)
    canvas.draw_polygon([(0,300),(400,300), (400,500), (0,500)], 1, "black", "white")

    # Snowman parts and child animation
    if progress >= 1:
        # Child moves to place the bottom snowball
        canvas.draw_circle((100, 300), 20, 1, "black", "grey")  # Head
        canvas.draw_line((100, 320), (100, 380), 2, "grey")    # Body
        canvas.draw_line((100, 340), (80, 360), 2, "grey")     # Left arm
        canvas.draw_line((100, 340), (120, 360), 2, "grey")    # Right arm
        canvas.draw_line((100, 380), (80, 400), 2, "grey")     # Left leg
        canvas.draw_line((100, 380), (120, 400), 2, "grey")    # Right leg
        canvas.draw_circle((200, 300), 50, 1, "black", "White")  # Bottom snowball

    if progress >= 3:
        # Child moves to place the middle snowball
        canvas.draw_circle((150, 230), 20, 1, "black", "grey")  # Head
        canvas.draw_line((150, 250), (150, 310), 2, "grey")    # Body
        canvas.draw_line((150, 270), (130, 290), 2, "grey")    # Left arm
        canvas.draw_line((150, 270), (170, 290), 2, "grey")    # Right arm
        canvas.draw_line((150, 310), (130, 330), 2, "grey")    # Left leg
        canvas.draw_line((150, 310), (170, 330), 2, "grey")    # Right leg
        canvas.draw_circle((200, 230), 40, 1, "black", "White")  # Middle snowball
        # Add arms to middle snowball
        canvas.draw_line((200 - 40, 230), (140, 200), 2, "brown")  # Left arm
        canvas.draw_line((200 + 40, 230), (260, 200), 2, "brown")  # Right arm
        # Add buttons to middle snowball
        canvas.draw_circle((200, 215), 5, 1, "Black", "Black")  # Top button
        canvas.draw_circle((200, 230), 5, 1, "Black", "Black")  # Middle button
        canvas.draw_circle((200, 245), 5, 1, "Black", "Black")  # Bottom button

    if progress >= 5:
        # Child moves to place the head snowball
        canvas.draw_circle((180, 170), 20, 1, "black", "grey")  # Head
        canvas.draw_line((180, 190), (180, 250), 2, "grey")    # Body
        canvas.draw_line((180, 210), (160, 230), 2, "grey")    # Left arm
        canvas.draw_line((180, 210), (200, 230), 2, "grey")    # Right arm
        canvas.draw_line((180, 250), (160, 270), 2, "grey")    # Left leg
        canvas.draw_line((180, 250), (200, 270), 2, "grey")    # Right leg
        canvas.draw_circle((200, 170), 30, 1, "black", "White")  # Head snowball

    if progress >= 7:
        # Child moves to add the hat, face, and features
        canvas.draw_circle((180, 140), 20, 1, "black", "grey")  # Head
        canvas.draw_line((180, 160), (180, 220), 2, "grey")    # Body
        canvas.draw_line((180, 180), (160, 200), 2, "grey")    # Left arm
        canvas.draw_line((180, 180), (200, 200), 2, "grey")    # Right arm
        canvas.draw_line((180, 220), (160, 240), 2, "grey")    # Left leg
        canvas.draw_line((180, 220), (200, 240), 2, "grey")    # Right leg

        # Hat
        canvas.draw_polygon([(170, 140), (230, 140), (230, 160), (170, 160)], 1, "Black", "Black")
        canvas.draw_polygon([(180, 120), (220, 120), (220, 140), (180, 140)], 1, "Black", "Black")

        # Eyes (circles)
        canvas.draw_circle((190, 160), 5, 1, "Black", "Black")  # Left eye
        canvas.draw_circle((210, 160), 5, 1, "Black", "Black")  # Right eye

        # Smile (small circles)
        for i in range(-2, 3):  # Positions for the smile
            canvas.draw_circle((200 + i * 5, 175), 2, 1, "Black", "Black")

        # Nose (orange triangle)
        canvas.draw_polygon([(200, 170), (200, 180), (220, 175)], 1, "Orange", "Orange")

    # Increment progress for animation
    progress += 0.2  # Slower progression
    if progress > 10:  # Reset after animation is complete
        progress = 0


# Frame setup
frame = simplegui.create_frame("Building a Snowman", 400, 500)
frame.set_canvas_background("#87CEEB")
# Register the draw handler
frame.set_draw_handler(draw)

# Initialize snowflakes and start the frame
init_snowflakes()
frame.start()
