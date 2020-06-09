#2020 Levi D. Smith - levidsmith.com
import pygame

from card import Card

class Table:

    def __init__(self):
        self.position = (400, 200)
        self.size = (512, (Card.h * 2 + 32))
        self.cards = []
        self.isSelected = False
        
    
    def update(self):
        None

    def draw(self, display, font):
        c = (0, 0, 128)
        if (self.isSelected):
            c = (64, 64, 128)
        pygame.draw.rect(display, c, (self.position[0], self.position[1], self.size[0], self.size[1]))



    def checkHovered(self, x, y):
        if (x > self.position[0] and x < self.position[0] + self.size[0] and y > self.position[1] and y < self.position[1] + self.size[1]):
            self.isSelected = True
            return True
        else:
            self.isSelected = False
            return False
