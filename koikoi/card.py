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
    isSakuraCurtain = False
    isMoon = False
    isRedRibbon = False
    isBlueRibbon = False
    isPoetryRibbon = False
    isSakeCup = False
    isSpecial = False
    isBoarDeerButterfly = False
    img = None
    img_back = None
    img_border = None
    surface_highlight = None
    surface_hint = None
    
    isHidden = True
  
    x = 0
    y = 0
    w = 64
    h = 128
    targetPosition = (0, 0)
    previousPosition = (0, 0)
	
    def __init__(self, init_id, init_x, init_y, init_application):
        self.id = init_id
        self.x = init_x
        self.y = init_y
        self.application = init_application
        self.isHovered = False
        self.isHint = False
        
    def draw(self, display, font):
        c = (128, 128, 128)
        pygame.draw.rect(display, c, (self.x, self.y, self.w, self.h))
        
        
        if (self.img != None):

            if (self.isHidden):
                display.blit(self.img_back, (self.x, self.y, self.w, self.h))
            else:
                display.blit(self.img, (self.x, self.y, self.w, self.h))
                display.blit(self.img_border, (self.x, self.y, self.w, self.h))




                c_black = (0, 0, 0)
       
#Display month
                if (self.application.options.showMonth):
                    c = (255, 255, 255)
                    text = font['normal'].render(str(self.iMonth + 1), True, c, c_black)
                    display.blit(text, (self.x, self.y))
        
                iLineSpacing = 32

#Display attribute
                if (self.application.options.showCardType):
                    if (self.isLight):
                        c = (255, 255, 0)
                        text = font['normal'].render("L", True, c, c_black)
                        display.blit(text, (self.x, self.y + iLineSpacing))

        
                    if (self.isRedRibbon):
                        c = (255, 0, 0)
                        if (self.isPoetryRibbon):
                            text = font['normal'].render("PR", True, c, c_black)
                        else:
                            text = font['normal'].render("R", True, c, c_black)
                        display.blit(text, (self.x, self.y + iLineSpacing))
        
                    if (self.isBlueRibbon):
                        c = (128, 128, 255)
                        text = font['normal'].render("BR", True, c, c_black)
                        display.blit(text, (self.x, self.y + iLineSpacing))

                    if (self.isSpecial):
                        c = (255, 128, 0)
                        text = font['normal'].render("S", True, c, c_black)
                        display.blit(text, (self.x, self.y + iLineSpacing))

                    if (self.isSakeCup):
                        c = (255, 128, 0)
                        text = font['normal'].render("SC", True, c, c_black)
                        display.blit(text, (self.x, self.y + iLineSpacing))

                    if (self.isRainMan):
                        c = (255, 128, 0)
                        text = font['normal'].render("RM", True, c, c_black)
                        display.blit(text, (self.x, self.y + iLineSpacing))

            if (self.isHovered):
                c = (128, 0, 0)
                display.blit(self.surface_highlight, (self.x, self.y))
            
            elif (self.isHint):
                c = (255, 255, 0)
                display.blit(self.surface_hint, (self.x, self.y))



#    def drawSelected(self, display, font):
#        c = (0, 128, 0)
#        pygame.draw.rect(display, c, (self.x, self.y, self.w, self.h))


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
        
    def __str__(self):
        return "Card ID: " + str(self.id) + " Month: " + str(self.iMonth)
        
        
    def checkHovered(self, x, y):
        if (x > self.x and x < self.x + self.w and y > self.y and y < self.y + self.h):
            self.isHovered = True
            return True
        else:
            self.isHovered = False
            return False

    
        