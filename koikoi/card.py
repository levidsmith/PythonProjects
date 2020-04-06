#2020 Levi D. Smith - levidsmith.com
import pygame

print("Card Class")
class Card:

    MOVE_SPEED = 10

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
    isBoarDeerButterfly = False
    img = None
    img_back = None
    img_border = None
    
    isHidden = True
    
    x = 0
    y = 0
    w = 64
    h = 128
#    w = 32
#    h = 64
    targetPosition = (0, 0)
	
    def __init__(self, init_id, init_x, init_y):
        self.id = init_id
        self.x = init_x
        self.y = init_y
        
    def draw(self, display, font):
        c = (128, 128, 128)
        pygame.draw.rect(display, c, (self.x, self.y, self.w, self.h))
        
        if (self.isHidden):
            display.blit(self.img_back, (self.x, self.y, self.w, self.h))
        
        elif (self.img != None):
            display.blit(self.img, (self.x, self.y, self.w, self.h))
            display.blit(self.img_border, (self.x, self.y, self.w, self.h))
        
            c_black = (0, 0, 0)
        
#Display month
            c = (255, 255, 255)
            text = font[0].render(str(self.iMonth), True, c, c_black)
            display.blit(text, (self.x, self.y))
        
            iLineSpacing = 32

#Display attribute
            if (self.isLight):
                c = (255, 255, 0)
                text = font[0].render("L", True, c, c_black)
                display.blit(text, (self.x, self.y + iLineSpacing))

        
            if (self.isRedRibbon):
                c = (255, 0, 0)
                if (self.isPoetryRibbon):
                    text = font[0].render("RPR", True, c, c_black)
                else:
                    text = font[0].render("RR", True, c, c_black)
                display.blit(text, (self.x, self.y + iLineSpacing))
        
            if (self.isBlueRibbon):
                c = (128, 128, 255)
                text = font[0].render("BR", True, c, c_black)
                display.blit(text, (self.x, self.y + iLineSpacing))

            if (self.isSpecial):
                c = (255, 128, 0)
                text = font[0].render("S", True, c, c_black)
                display.blit(text, (self.x, self.y + iLineSpacing))

            if (self.isSakeCup):
                c = (255, 128, 0)
                text = font[0].render("SC", True, c, c_black)
                display.blit(text, (self.x, self.y + iLineSpacing))

            if (self.isRainMan):
                c = (255, 128, 0)
                text = font[0].render("RM", True, c, c_black)
                display.blit(text, (self.x, self.y + iLineSpacing))

    def update(self):
        iSpeed = self.MOVE_SPEED
    
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
            
            

    def getIsNormal(self):
        isNormal = True
        if (self.isLight or self.isRainMan or self.isRedRibbon or self.isBlueRibbon \
            or self.isSakeCup or self.isSpecial):
            isNormal = False
        
        return isNormal