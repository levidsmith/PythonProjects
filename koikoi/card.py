#2020 Levi D. Smith - levidsmith.com
import pygame

print("Card Class")
class Card:
    iSuit = -1
    id = -1
    
    x = 0
    y = 0
    w = 64
    h = 128
	
    def __init__(self, init_suit, init_id, init_x, init_y):
        self.iSuit = init_suit
        self.id = init_id
        self.x = init_x
        self.y = init_y
        
    def draw(self, display):
        c = (128, 128, 128)
        pygame.draw.rect(display, c, (self.x, self.y, self.w, self.h))
