#Hailey Sooknanan
#Period 5-6
#CFU 15-use the  method   #canvas.draw_polygon([(x1,y1),(x2,y2),(x3,y3)], line_width, color) to  draw a happy  face 
#title of the frame to CFU15 Happy Shapes

import simplegui 
def draw_handler(canvas):
    #all drawing happens here 
    #use the  method   
    #canvas.draw_polygon([(x1,y1),(x2,y2),(x3,y3)], line_width, color) 
    canvas.draw_polygon([(75,25),(100,25),(85,60)], 10, "red")
    canvas.draw_polygon([(115,25),(140,25),(125,60)], 10, "red")
    canvas.draw_polygon([(75,120),(100,120),(125,120)], 10, "red")
#library.create_frame(title,width,height)
frame = simplegui.create_frame("CFU15 Happy Shapes",200,200)
#python colors will be the name of the frame 
frame.set_canvas_background("white") 
frame.set_draw_handler(draw_handler) 
frame.start()
