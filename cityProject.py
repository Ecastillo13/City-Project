from graphics import *


class Building(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def building(self, win):
        block = Rectangle(Point(self.x, self.y), Point(self.x + 125, self.y + 175))
        block.setFill("gray")
        block.draw(win)

        window1 = Rectangle(Point(self.x + 25, self.y + 25), Point(self.x + 50, self.y + 50))
        window1.setFill("yellow")
        window1.draw(win)
        window2 = Rectangle(Point(self.x + 100, self.y + 25), Point(self.x + 75, self.y + 50))
        window2.setFill("yellow")
        window2.draw(win)
        window3 = Rectangle(Point(self.x + 50, self.y + 75 ), Point(self.x + 25 , self.y + 100 ))
        window3.setFill("yellow")
        window3.draw(win)
        window4 = Rectangle(Point(self.x + 75 , self.y + 75 ), Point(self.x + 100, self.y + 100))
        window4.setFill("yellow")
        window4.draw(win)


class House(Building):
    def __init__(self, x:int, y:int, win):
        super().__init__(x, y, win)

    def roof(self, win):
        houseroof = Polygon(Point(self.x, self.y), Point(self.x + 125, self.y), Point(self.x + 63.5, self.y - 62.5))
        houseroof.setFill("brown")
        houseroof.draw(win)

    def door(self, win):
        door = Rectangle(Point(self.x + 50 , self.y + 175 ), Point(self.x + 50, self.y + 175))
        door.setFill("brown")
        door.draw(win)

#class Skyscraper(Building):
    #def __init__(self, x:int, y:int, color, win):
        #super().__init__(x , y)



    

    ##def skytop(self, win):
    ##   topper = Arc


class CityStreet(object):
    def __init__(self, x:int, y:int, color):
        self.x = x
        self.y = y
        self.color = color

    def drawCityStreet(self, win):
        street = Rectangle(Point(self.x, self.y), Point(self.x + 1000, self.y + 75))
        street.setFill(self.color)
        street.draw(win)

    def drawSideWalk(self, win):
        sideWalk1 = Rectangle(Point(self.x, self.y), Point(self.x + 1000, self.y + 49 ))
        sideWalk1.setFill(self.color)
        sideWalk1.draw(win)
        sideWalk2 = Rectangle(Point(self.x, self.y), Point(self.x + 1000, self.y + 49))
        sideWalk2.setFill(self.color)
        sideWalk2.draw(win)

    def details(self, win):
        yellowLine = Rectangle(Point(self.x, self.y), Point(self.x + 125, self.y + 25))
        yellowLine.setFill(self.color)
        yellowLine.draw(win)

def main():
    win = GraphWin("cityProject", 999, 649)
    street = CityStreet(0, 525, color_rgb(52, 55, 61))
    street.drawCityStreet(win)

    yellowLine = CityStreet(125, 550, color_rgb(255, 241, 56))
    yellowLine.details(win)

    sideWalk = CityStreet(0, 475, color_rgb(196, 199, 206))
    sideWalk.drawSideWalk(win)
    sideWalk2 = CityStreet(0, 600, color_rgb(196, 199, 206))
    sideWalk2.drawSideWalk(win)

    house = House(0,250,win)
    house.building(win)
    win.getMouse()
    win.close()


main()
