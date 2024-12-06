#CFU 17
#Hailey Sooknanan
#12/6
#Period 5-6
#Sample code for scaling images

import simplegui

frame_width = int(input("width?"))
frame_height= int(input("Height?"))
show_square = True
show_circle = True
show_triangle = True
show_ellipse= True
    
def toggle_triangle():
    global show_triangle
    show_triangle = not show_triangle
    
    
frame = None #Global Reference to frame

def draw_triangle(canvas, cx, cy, size):
    #draw shape
    half_size = size/2
    canvas.draw_polygon([(cx,cy-half_size),
                         (cx-half_size, cy+half_size), 
                         (cx+half_size, cy+half_size)], 2, "blue", "blue")
def draw(canvas):
    quadrant_width = frame_width/2
    quadrant_height= frame_height/2
    draw_triangle(canvas, quadrant_width/2, frame_height - quadrant_height/2, 100)

def create_frame():
    global frame 
    frame = simplegui.create_frame("CFU #17", frame_width, frame_height)
    frame.set_canvas_background("red")
    frame.add_button("triangle", toggle_triangle, 150)
    frame.set_draw_handler(draw)
    frame.start()
create_frame()
     
