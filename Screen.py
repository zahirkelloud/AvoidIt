import pygame

class Sceen:

    def __init__(self, width=800, height=600, color=(0,0,0)):
        self.width = width
        self.height = height
        self.color = color

    def get(self):
        return pygame.display.set_mode((self.width, self.height))