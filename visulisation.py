from graphics import *
import random
text_file = open("data.txt", "r")
dataNumbers = text_file.read().split('\n')
text_file.close()

for word in dataNumbers: print(">>" + word)
window = GraphWin("Data", 600, 600)

for word in dataNumbers:
    posx = random.randrange(0,600)
    posy = random.randrange(0,600)
    line = Line(Point(posx,posy),Point(0,600))
    line.setWidth(10)
    line.draw(window)
    
window.getMouse()
