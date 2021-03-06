from graphics import *
class button:
    def __init__(self, win, name,x1,x2,y1,y2):
        self.name = name
        self.xmin = x1
        self.xmax = x2
        self.ymin = y1
        self.ymax = y2
        self.wind = win
        self.red = 0
        self.green = 0
        self.blue = 0
        self.key = "placeholdthatwillnevertriger"
    def testBtn(self,p,key=None):
        if p == None:
            p = Point(-42, -42)
        if key == None:
            key = 'dont error me'
        x = p.getX()
        y = p.getY()
        if ((x>self.xmin)and(x<self.xmax)and(y>self.ymin)and(y<self.ymax)) or self.key == key:
            return 1
        else:
            return 0
    def setBtnColor(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
    def setKey(self, ky):
        self.key = ky
    def drawBtn(self):
        x1 = float(self.xmin)
        x2 = float(self.xmax)
        y1 = float(self.ymin)
        y2 = float(self.ymax)
        color = color_rgb(self.red, self.green, self.blue)
        p1 = Point(x1,y1)
        p2 = Point(x2,y2)
        rec = Rectangle(p1, p2)
        rec.setFill(color)
        self.rect = rec
        rec.draw(self.wind)
        midx = (x2+x1)/2
        midy = (y2+y1)/2
        p3 = Point(midx, midy)
        title = Text(p3, self.name)
        self.title = title
        title.draw(self.wind)
    def removeBtn(self):
        self.title.undraw()
        self.rect.undraw()
