#2020 Levi D. Smith - levidsmith.com
import pygame

class DrawHelper:

    def drawTextShadow(str, x, y, c, display, font):
        text = font.render(str, True, (0, 0, 0))
        display.blit(text, (x + 2, y + 2))

        text = font.render(str, True, c)
        display.blit(text, (x, y))

        
    