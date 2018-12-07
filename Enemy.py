import random

class Enemy:
    color = (255,0,0)
    size = 50
    xpos = 0
    ypos = 0
    
    def __init__(self, screen, color=(0,0,255), size=50):
        self.color = color
        self.size = size
        self.setPosition(random.randint(0, screen.width-self.size), 0)

    def setPosition(self, x, y):
        self.xpos = x
        self.ypos = y