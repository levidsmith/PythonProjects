#2020 Levi D. Smith - levidsmith.com
import pygame

from button import Button
from screen import Screen
from globals import Globals
from drawhelper import DrawHelper

class ScreenGameComplete(Screen):

    def __init__(self, init_application):
        print("init")
        super().__init__()
        self.application = init_application
        self.imgBackground = None
        self.load_images()
        self.makeButtons()

    def load_images(self):
        self.imgBackground = pygame.image.load('images/background_gamecomplete.jpg')


    def makeButtons(self):
#        self.buttons = []

        iOffset = (Globals.SCREEN_SIZE[0] - 128) / 2
        b = Button("Finished", iOffset, 500)
        b.action = self.doFinished
        b.show()
        self.buttons.append(b)



    def update(self):
#        print("update")
        pass

    def draw(self, display, font):
#        print("draw")
        display.blit(self.imgBackground, (0, 0))

        for button in self.buttons:
            button.draw(display, font)


        DrawHelper.drawTextShadow("Game Complete", 600, 300, (255, 255, 255), display, font['normal'])



    def doFinished(self):
        self.application.loadScreen("title")

