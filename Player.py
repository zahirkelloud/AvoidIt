import pygame

class Player:
    color = (255,0,0)
    size = 50
    xpos = 0
    ypos = 0
    
    def __init__(self, screen, color=(255,0,0), size=50):
        self.color = color
        self.size = size
        self.setPosition((screen.width-self.size)/2, screen.height-2*self.size)

    def setPosition(self, x, y):
        self.xpos = x
        self.ypos = y
    
    def get(self, screen):
        return pygame.draw.rect(screen, self.color, (self.xpos, self.ypos, self.size, self.size))
        