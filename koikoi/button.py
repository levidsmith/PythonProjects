import pygame

from drawhelper import DrawHelper

class Button:



    def __init__(self, str, x, y):
        self.strLabel = str
        self.x = x
        self.y = y
        self.w = 128
        self.h = 32
        self.action = None
        
        
    def draw(self, display, font):
        c_bkg = (0, 0, 0)
        pygame.draw.rect(display, c_bkg, [self.x, self.y, self.w, self.h])
        DrawHelper.drawTextShadow(self.strLabel, self.x, self.y, (255, 255, 255), display, font[1])
        
    def isClicked(self, x, y):
        if (x > self.x and x < self.x + self.w and y > self.y and y < self.y + self.h):
            return True
        else:
            return False

        

    
    
    
    