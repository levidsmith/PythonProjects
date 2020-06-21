#2020 Levi D. Smith - levidsmith.com
import pygame

class Screen:
    def __init__(self):
        self.isCursorHovered = False
        self.buttons = []
        pass

    def update(self):
        pass
    
    def draw(self, display, font):
        for button in self.buttons:
            button.draw(display, font)
    
    def restart(self):
        pass


    def mousePressed(self, mousePosition):
        
        for button in self.buttons:
            if (button.isClicked(mousePosition[0], mousePosition[1])):
                print(button.strLabel + " button clicked")
                if (button.action_params != None):
                    button.action(button.action_params)
                else:
                    button.action()


    def mouseReleased(self, mousePosition):
        pass


    def mouseMoved(self, mousePosition):
        mouseX = mousePosition[0]
        mouseY = mousePosition[1]
        
        isHovered = self.isCursorHovered
        self.isCursorHovered = False #Set cursor hovered to false, and then set it to true if any cards or buttons are hovered

        self.checkButtonsHover(mouseX, mouseY)
        if (isHovered != self.isCursorHovered):
            if (self.isCursorHovered):
                pygame.mouse.set_cursor(*pygame.cursors.diamond)
            else:
                pygame.mouse.set_cursor(*pygame.cursors.arrow)


    def checkButtonsHover(self, x, y):
        for button in self.buttons:
            self.isCursorHovered = self.isCursorHovered or button.checkHovered(x, y)


    def keyInputChar(self, inputChar):
        pass

    def keyInputDelete(self):
        pass


