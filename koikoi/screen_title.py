#2020 Levi D. Smith - levidsmith.com
import pygame

from screen import Screen
from button import Button
from drawhelper import DrawHelper
from globals import Globals

class ScreenTitle(Screen):

    def __init__(self, init_application):
        print("init")
        self.application = init_application
        self.makeButtons()
        self.isCursorHovered = False


    def makeButtons(self):
        self.buttons = []
        b = Button("Start", 0, 500)
        b.action = self.doStart
        b.show()
        self.buttons.append(b)

        b = Button("Quit", 200, 500)
        b.action = self.doQuit
        b.show()
        self.buttons.append(b)


    def update(self):
#        print("update")
        None


    def draw(self, display, font):
        #print("draw")

        c = (64, 32, 0)
        pygame.draw.rect(display, c, (0, 0, Globals.SCREEN_SIZE[0], Globals.SCREEN_SIZE[1]))

        strTitle = "PyKoiKoi"
        DrawHelper.drawTextShadow(strTitle, 1280/2, 300, (255, 255, 255), display, font[1])

        strCopyright = "2020 - Levi D. Smith"
        DrawHelper.drawTextShadow(strCopyright, 1280/2, 600, (255, 255, 255), display, font[1])

        for button in self.buttons:
            button.draw(display, font)



    def mousePressed(self, mousePosition):
        mouseX = mousePosition[0]
        mouseY = mousePosition[1]

        self.checkButtonsPress(mouseX, mouseY)
    
    def mouseReleased(self, mousePosition):
        mouseX = mousePosition[0]
        mouseY = mousePosition[1]
        
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

        
    def checkButtonsPress(self, x, y):
        for button in self.buttons:
            if (button.isClicked(x, y)):
                print(button.strLabel + " button clicked")
                button.action()
    
    def checkButtonsHover(self, x, y):
        for button in self.buttons:
            self.isCursorHovered = self.isCursorHovered or button.isHovered(x, y)

    
    def doStart(self):
        self.application.loadScreen("gamemanager")


    def doQuit(self):
        self.application.doQuit()
