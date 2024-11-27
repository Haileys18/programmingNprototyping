#Hailey Sooknanan
#Period 5-6
#CFU 16-Using circles to create a happy face

import simplegui 
def draw_handler(canvas):
    #all drawing happens here 
    #use the  method   
    #canvas.draw_cirlce(centerXY, radius, line_width, color)
    canvas.draw_circle((150,150), 150, 3, "purple")
    canvas.draw_circle((120,120), 20, 3, "purple")
    canvas.draw_circle((200,120), 20, 3, "purple")
    canvas.draw_circle((165,150), 10, 3, "purple")
    canvas.draw_circle((120,180), 30, 3, "purple", "black")
    canvas.draw_circle((160,200), 30, 3, "black", "black")
    canvas.draw_circle((200,180), 30, 3, "purple","black")
#library.create_frame(title,width,height)
frame = simplegui.create_frame("CFU16 Happy circle",300,300)
#python colors will be the name of the frame 
frame.set_canvas_background("white") 
frame.set_draw_handler(draw_handler) 
frame.start()
