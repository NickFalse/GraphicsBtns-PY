from graphicsbtns import *
from graphics import *
from random import *


def createWindow(title,width,height):
    win = GraphWin(title,width, height)
    win.setCoords(0.0, 0.0, float(width), float(height))
    return win

def addButton(name,x1,x2,y1,y2):
    new_button = button(name,x1,x2,y1,y2)
    return new_button
    
def main():

    win = createWindow("Test",600,600)
    
    x1 = 100
    x2 = 200
    y1 = 400
    y2 = 500
    offset = 100
    
    b1 = addButton("Quit",x1,x2,y1,y2)
    b1.setBtnColor(255,0,255)
    b1.drawBtn(win)

    
    b2 = addButton("Remove",x1,x2,y1+offset,y2+offset)
    b2.setBtnColor(0,255,0)
    b2.drawBtn(win)

    b3 = addButton("Color",x1+offset,x2+offset,y1,y2)
    b3.setBtnColor(255,255,255)
    b3.drawBtn(win)
    
    while 1:
        clicked = win.getMouse()
        if b1.testBtn(clicked) == 1:
            win.close()
        if b2.testBtn(clicked) == 1:
            b2.removeBtn()
        if b3.testBtn(clicked) == 1:
            b3.setBtnColor(randint(0,255),randint(0,255),randint(0,255))       
            b3.drawBtn(win)



main()
