#2020 Levi D. Smith - levidsmith.com
import pygame

from screen import Screen
from button import Button
from drawhelper import DrawHelper
from globals import Globals

class ScreenTitle(Screen):


    def __init__(self, init_application):
        super().__init__()

        print("init")
        self.application = init_application
        self.makeButtons()
        self.isCursorHovered = False
        self.imgBackground = None
        self.load_images()
        self.iBackgroundScale = 1


    def load_images(self):
        self.imgBackground = pygame.image.load('images/background_title.jpg')


    def makeButtons(self):
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
        None
        self.iBackgroundScale += 0.1 * (1/60)



    def draw(self, display, font):

        display.blit(self.imgBackground, (0, 0))



        strTitle = "PyKoiKoi"
        iOffset = (Globals.SCREEN_SIZE[0] -  DrawHelper.getTextSize(strTitle, font['title'])[0]) / 2
        DrawHelper.drawTextShadow(strTitle, iOffset, 200, (255, 255, 255), display, font['title'])

        strCopyright = "2020 - Levi D. Smith"
        iOffset = (Globals.SCREEN_SIZE[0] -  DrawHelper.getTextSize(strCopyright, font['normal'])[0]) / 2
        DrawHelper.drawTextShadow(strCopyright, iOffset, 600, (255, 255, 255), display, font['normal'])

        super().draw(display, font)

    
    def doStart(self):
        self.application.loadScreen("options")


    def doQuit(self):
        self.application.doQuit()
