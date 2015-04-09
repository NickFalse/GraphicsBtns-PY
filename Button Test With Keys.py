from graphicsbtns import *
from graphics import *
from random import *


def createWindow(title,width,height):
    win = GraphWin(title,width, height)
    win.setCoords(0.0, 0.0, float(width), float(height))
    return win

def addButton(win,name,x1,x2,y1,y2):
    new_button = button(win,name,x1,x2,y1,y2)
    return new_button
    
def main():

    win = createWindow("Test",600,600)
    
    x1 = 100
    x2 = 200
    y1 = 400
    y2 = 500
    offset = 100
    
    b1 = addButton(win,"Quit",x1,x2,y1,y2)
    b1.setBtnColor(255,0,255)
    b1.setKey('Escape')
    b1.drawBtn()

    
    b2 = addButton(win,"Remove",x1,x2,y1+offset,y2+offset)
    b2.setBtnColor(0,255,0)
    b2.setKey('Delete')
    b2.drawBtn()

    b3 = addButton(win,"Color",x1+offset,x2+offset,y1,y2)
    b3.setBtnColor(255,255,255)
    b3.setKey('c')
    b3.drawBtn()
    
    while 1:
        clicked = win.checkMouse()
        key = win.checkKey()
        if b1.testBtn(clicked,key) == 1:
            win.close()
        if b2.testBtn(clicked,key) == 1:
            b2.removeBtn()
        if b3.testBtn(clicked,key) == 1:
            b3.setBtnColor(randint(0,255),randint(0,255),randint(0,255))       
            b3.drawBtn()



main()
