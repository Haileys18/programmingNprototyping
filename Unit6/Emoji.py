import simplegui
import math
# Global Variables

width = int(input("Enter a width value: "))
height = int(input("Enter a Height value: "))
face1 = False
face2 = False
face3 = False
face4 = False
face5 = False
scale= 0.4
# Event Handlers

def all_false():
    global face1
    global face2
    global face3
    global face4
    global face5
    face1 = False
    face2 = False
    face3 = False
    face4 = False
    face5 = False
    
def toggle_face1():
    all_false()
    global face1
    face1 = not face1
    
def toggle_face2():
    all_false()
    global face2
    face2 = not face2
      
def toggle_face3():
    all_false()
    global face3
    face3 = not face3
    
def toggle_face4():
    all_false()
    global face4
    face4 = not face4

def toggle_face5():
    all_false()
    global face5
    face5 = not face5

def draw(canvas):
    if face1:
        canvas.draw_circle(((width/2)/2, (height/2)/2), (width/2 - 50)*scale, 10, "Yellow", "Yellow")
        
        # Right eye (winking)
        canvas.draw_circle([width/3, height/6], 60*scale, 2, "Black", "yellow")
        canvas.draw_circle([width/3, height/5.5], 62.5*scale, 2, "yellow", "yellow")
        
        # Left eye (open)
        canvas.draw_circle([width/6, height/6], 60*scale, 2, "black", "white")
        canvas.draw_circle([width/6, height/6], 15*scale, 2, "black", "black")
        
        # Big smiling mouth
        canvas.draw_circle([width/4, height/3.5 + 30], 75*scale, 2, "black","black")
        canvas.draw_circle([width/4, height/3.5 + 30], 75*scale, 2, "yellow", "white")
     

        
    if face2:
        canvas.draw_circle((width/2, height/2), width/2 - 50, 10, "yellow", "yellow")
        canvas.draw_line([100,200],[width/3,height/3],5,"black")
        canvas.draw_line([400,200],[500,height/3],5,"black")
    #Mouth
        canvas.draw_circle([width/2,height/2+70],90,2,"black")
        canvas.draw_polygon([(width/1,height/1),(width/2,height/1),
        (width/4,5*height/3),(width/4,5*height/3)],2,"yellow","yellow")
        
    if face3:
        canvas.draw_circle((width/2, height/2), width/2 - 50, 10, "#FA8072", "#FA8072")
        canvas.draw_circle([width/2.75, height/2 - 100], 10 , 10, "Black", "White")
        canvas.draw_circle([width - width/2.75, height/2 - 100], 10 , 10, "Black", "White")
        canvas.draw_line((width/3, height/2 - 150),(width/3 + 50, height/2 - 125), 5, "Black")
        canvas.draw_line((width - width/3, height/2 - 150),(width - width/3 - 50, height/2 - 125), 5, "Black")
        canvas.draw_polygon([(width/2, height - height/4), (width/2 - 50, height - height/4 + 25), (width/2 - 10, height - height/4 - 30), (width/2 + 10, height - height/4 - 30), (width/2 + 50, height - height/4 + 25)],10, "Black", "White")
        canvas.draw_line((width/2 - 30, height - height/4 - 10), (width/2 + 30, height - height/4 - 10), 5, "Black")

    if face4:
        canvas.draw_circle((300, 300), 250, 10, "#FCF4A3", "#FCF4A3")
        canvas.draw_circle((200, 200), 30, 2, "Black", "White")
        canvas.draw_circle((400, 200), 30, 2, "Black", "White")
        canvas.draw_circle((200, 215), 15, 2, "Black", "Black")
        canvas.draw_circle((400, 215), 15, 2, "Black", "Black")
        canvas.draw_circle((200, 215), 4, 2, "White", "White")
        canvas.draw_circle((400, 215), 4, 2, "White", "White")
        canvas.draw_line((160, 180),(200, 150), 3, "Black")
        canvas.draw_line((200, 150),(240, 180), 3, "Black")
        canvas.draw_line((360, 180),(400, 150), 3, "Black")
        canvas.draw_line((400, 150),(440, 180), 3, "Black")
        canvas.draw_circle((300, 400), 30, 2, "Black", "Black")

    if face5:
        canvas.draw_circle((300, 300), 250, 10, "#FCF4A3", "#FCF4A3")
frame = simplegui.create_frame("Pictures", width, height) 

frame.set_draw_handler(draw)
frame.add_button("Hailey", toggle_face1, 100)
frame.add_button("Marisa", toggle_face2, 100)
frame.add_button("Farhan", toggle_face3, 100)
frame.add_button("Surprised", toggle_face4, 100)
frame.add_button("Everything", toggle_face5, 100)

frame.start()
