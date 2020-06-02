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
        self.imgBackground = None
        self.load_images()
        self.iBackgroundScale = 1


    def load_images(self):
        self.imgBackground = pygame.image.load('images/background_title.jpg')
#        self.imgBackground = pygame.transform.scale(self.imgBackground, (, 480))


    def makeButtons(self):
        self.buttons = []
        iOffset = ((Globals.SCREEN_SIZE[0] - (128 * 3)) / 2) + (128 * 0)
        b = Button("Start", iOffset, 500)
        b.action = self.doStart
        b.show()
        self.buttons.append(b)

        iOffset = ((Globals.SCREEN_SIZE[0] - (128 * 3)) / 2) + (128 * 2)
        b = Button("Quit", iOffset, 500)
        b.action = self.doQuit
        b.show()
        self.buttons.append(b)


    def update(self):
#        print("update")
        None
        self.iBackgroundScale += 0.1 * (1/60)
#        self.imgBackground = pygame.transform.scale(self.imgBackground, (int(Globals.SCREEN_SIZE[0] * self.iBackgroundScale), int(Globals.SCREEN_SIZE[1] * self.iBackgroundScale)))



    def draw(self, display, font):
        #print("draw")

        display.blit(self.imgBackground, (0, 0))


#        c = (64, 32, 0)
#        pygame.draw.rect(display, c, (0, 0, Globals.SCREEN_SIZE[0], Globals.SCREEN_SIZE[1]))

        strTitle = "PyKoiKoi"
        iOffset = (Globals.SCREEN_SIZE[0] -  DrawHelper.getTextSize(strTitle, font['title'])[0]) / 2
        DrawHelper.drawTextShadow(strTitle, iOffset, 200, (255, 255, 255), display, font['title'])

        strCopyright = "2020 - Levi D. Smith"
        iOffset = (Globals.SCREEN_SIZE[0] -  DrawHelper.getTextSize(strCopyright, font['normal'])[0]) / 2
        DrawHelper.drawTextShadow(strCopyright, iOffset, 600, (255, 255, 255), display, font['normal'])

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
