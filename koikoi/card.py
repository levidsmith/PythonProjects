#2020 Levi D. Smith - levidsmith.com
import pygame

print("Card Class")
class Card:
    id = -1
    iMonth = 0
    iPoints = 0
    isLight = False
    isRainMan = False
    isRedRibbon = False
    isBlueRibbon = False
    isPoetryRibbon = False
    isSakeCup = False
    isSpecial = False
    img = None
    
    x = 0
    y = 0
    w = 64
    h = 128
    targetPosition = (0, 0)
	
    def __init__(self, init_id, init_x, init_y):
        self.id = init_id
        self.x = init_x
        self.y = init_y
        
    def draw(self, display, font):
        c = (128, 128, 128)
        pygame.draw.rect(display, c, (self.x, self.y, self.w, self.h))
        if (self.img != None):
            display.blit(self.img, (self.x, self.y, self.w, self.h))


        c_black = (0, 0, 0)

#        c = (255, 255, 255)
#        text = font.render(str(self.id), True, (255, 255, 255), c_black)
#        display.blit(text, (self.x, self.y + 100))

        
#Display month
        c = (255, 255, 255)
        text = font.render(str(self.iMonth), True, c, c_black)
        display.blit(text, (self.x, self.y))
        
        iLineSpacing = 32

#Display attribute
        if (self.isLight):
            c = (255, 255, 0)
            text = font.render("L", True, c, c_black)
            display.blit(text, (self.x, self.y + iLineSpacing))

        
        if (self.isRedRibbon):
            c = (255, 0, 0)
            if (self.isPoetryRibbon):
                text = font.render("RPR", True, c, c_black)
            else:
                text = font.render("RR", True, c, c_black)
            display.blit(text, (self.x, self.y + iLineSpacing))
        
        if (self.isBlueRibbon):
            c = (128, 128, 255)
            text = font.render("BR", True, c, c_black)
            display.blit(text, (self.x, self.y + iLineSpacing))

        if (self.isSpecial):
            c = (255, 128, 0)
            text = font.render("S", True, c, c_black)
            display.blit(text, (self.x, self.y + iLineSpacing))

        if (self.isSakeCup):
            c = (255, 128, 0)
            text = font.render("SC", True, c, c_black)
            display.blit(text, (self.x, self.y + iLineSpacing))

        if (self.isRainMan):
            c = (255, 128, 0)
            text = font.render("RM", True, c, c_black)
            display.blit(text, (self.x, self.y + iLineSpacing))

    def update(self):
        iSpeed = 5
    
        if (self.x < self.targetPosition[0]):
            self.x += iSpeed
            if (self.x > self.targetPosition[0]):
                self.x = self.targetPosition[0]
        elif (self.x > self.targetPosition[0]):
            self.x -= iSpeed
            if (self.x < self.targetPosition[0]):
                self.x = self.targetPosition[0]

        if (self.y < self.targetPosition[1]):
            self.y += iSpeed
            if (self.y > self.targetPosition[1]):
                self.y = self.targetPosition[1]

        elif (self.y > self.targetPosition[1]):
            self.y -= iSpeed
            if (self.y < self.targetPosition[1]):
                self.y = self.targetPosition[1]
            
            