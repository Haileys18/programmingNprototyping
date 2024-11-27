#Hailey Sooknanan
#Period 5-6
#CFU 13-draw a canvas of 200 by 200 px use the  method draw_point([x,y],"color") to  draw a happy  face
#change the title of the frame to CFU13 Happy Dots

import simplegui 
def draw_handler(canvas):
    #all drawing happens here #canvas.draw_point([x,y], "color") 
    canvas.draw_point([74,75], "white") 
    canvas.draw_point([75,75], "white") 
    canvas.draw_point([76,75], "white") 
    canvas.draw_point([76,76], "white")
    canvas.draw_point([75,76], "white") 
    canvas.draw_point([74,76], "white") 
    canvas.draw_point([110,75], "white") 
    canvas.draw_point([110,76], "white")
    canvas.draw_point([109,75], "white") 
    canvas.draw_point([109,76], "white") 
    canvas.draw_point([111,75], "white") 
    canvas.draw_point([111,76], "white")
    canvas.draw_point([95,85], "white") 
    canvas.draw_point([96,85], "white") 
    canvas.draw_point([75,100], "white") 
    canvas.draw_point([80,105], "white")
    canvas.draw_point([83,107], "white") 
    canvas.draw_point([90,107], "white") 
    canvas.draw_point([95,107], "white") 
    canvas.draw_point([100,107], "white")
    canvas.draw_point([105,107], "white") 
    canvas.draw_point([109,104], "white") 
    canvas.draw_point([114,100], "white") 
#library.create_frame(title,width,height)
frame = simplegui.create_frame("CFU13 Happy Dots",200,200)#python colors will be the name of the frame frame.set_canvas_background("rgb(0,249,255)")
frame.set_draw_handler(draw_handler) 
    
frame.start()
