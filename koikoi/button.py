#2020 Levi D. Smith - levidsmith.com
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
        self.action_params = None
        self.bkg_color_normal = (0, 0, 0)
        self.bkg_color_highlight = (0, 0, 255)
        self.bkg_color = self.bkg_color_normal
        self.isHidden = False

        
    def draw(self, display, font):
        if (not self.isHidden):
            c = (255, 255, 255)
            pygame.draw.rect(display, self.bkg_color, [self.x, self.y, self.w, self.h])
            DrawHelper.drawTextShadow(self.strLabel, self.x, self.y, c, display, font['normal'])
        
    def isClicked(self, x, y):
        if (not self.isHidden):
            if (x > self.x and x < self.x + self.w and y > self.y and y < self.y + self.h):
                self.isSelected = True
                return True
            else:
                return False

    def checkHovered(self, x, y):        
        if (not self.isHidden):
            if (x > self.x and x < self.x + self.w and y > self.y and y < self.y + self.h):
                self.bkg_color = self.bkg_color_highlight
                return True
            else:
                self.bkg_color = self.bkg_color_normal
                return False
            
    def hide(self):
        self.isHidden = True
        
    def show(self):
        self.isHidden = False
    

    
    
    
    