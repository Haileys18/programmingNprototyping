#Hailey Sooknanan
#Period 5-6
#CFU 14-use the  method   #canvas.draw_line([point1], [point2], line_with, Line_color) to  draw a happy  face
#change the title of the frame to CFU14 Happy Lines

import simplegui 
def draw_handler(canvas):
    #all drawing happens here 
    #canvas.draw_line([point1], [point2], line_with,line_color)
    #canvas.draw_line([x1,y1], [x2,y2], line_width,line_color) 
    #all drawing happens here
    canvas.draw_line([75,25], [75,50], 5 ,"red") 
    canvas.draw_line([100,25], [100,50], 5 ,"red") 
    canvas.draw_line([85,60], [91,60], 5 ,"red") 
    canvas.draw_line([72,80], [80,85], 5 ,"red")
    canvas.draw_line([81,85], [90,85], 5 ,"red") 
    canvas.draw_line([91,85], [100,80], 5 ,"red")
#library.create_frame(title,width,height)
frame = simplegui.create_frame("CFU13 Happy lines",200,200)
#python colors will be the name of the frame 
frame.set_canvas_background("pink") 
frame.set_draw_handler(draw_handler) 
frame.start()
