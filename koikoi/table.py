#2020 Levi D. Smith - levidsmith.com
import pygame

from card import Card

class Table:

    def __init__(self):
        self.position = (400, 200)
        self.size = (512, (Card.h * 2 + 32))
        self.cards = []
        self.isSelected = False
        self.surfaceBackground = None
        self.makeBackground()

    def makeBackground(self):
        self.surfaceBackground = pygame.Surface(self.size)
        self.surfaceBackground.set_alpha(64)
        self.surfaceBackground.fill((0, 0, 255))
        
    
    def update(self):
        None

    def draw(self, display, font):
        self.surfaceBackground.set_alpha(32)

        if (self.isSelected):
            self.surfaceBackground.set_alpha(64)
        display.blit(self.surfaceBackground, (self.position[0], self.position[1], self.size[0], self.size[1]))



    def checkHovered(self, x, y):
        if (x > self.position[0] and x < self.position[0] + self.size[0] and y > self.position[1] and y < self.position[1] + self.size[1]):
            self.isSelected = True
            return True
        else:
            self.isSelected = False
            return False
