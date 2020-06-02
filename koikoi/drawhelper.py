#2020 Levi D. Smith - levidsmith.com
import pygame

class DrawHelper:

    def drawTextShadow(str, x, y, c, display, font):
        iVerticalOffset = 0
        dimensions = []
        

        for strLine in str.splitlines():
            text = font.render(strLine, True, (0, 0, 0))
            display.blit(text, (x + 2, y + 2 + iVerticalOffset))
            
            text = font.render(strLine, True, c)
            display.blit(text, (x, y + iVerticalOffset))
            iVerticalOffset += font.size(strLine)[1]

    def getTextSize(str, font):
        return font.size(str)
        


        
    