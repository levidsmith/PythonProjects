#2020 Levi D. Smith - levidsmith.com
import pygame

from button import Button
from screen import Screen
from globals import Globals
from drawhelper import DrawHelper


class ScreenGameComplete(Screen):
    ROW_SPACING = 40

    def __init__(self, init_application):
        print("init")
        super().__init__()
        self.application = init_application
        self.imgBackground = None
        self.load_images()
        self.makeButtons()

    def load_images(self):
        self.imgBackground = pygame.image.load('images/background_gamecomplete.jpg')
        self.surfaceBackground = pygame.Surface((600, 700))
        self.surfaceBackground.set_alpha(64)
        self.surfaceBackground.fill((0, 0, 0))



    def makeButtons(self):
        iOffset = (Globals.SCREEN_SIZE[0] - 128) / 2
        b = Button("Finished", iOffset, 680)
        b.action = self.doFinished
        b.show()
        self.buttons.append(b)



    def update(self):
        pass

    def draw(self, display, font):
        display.blit(self.imgBackground, (0, 0))

        display.blit(self.surfaceBackground.subsurface(0, 0, 600, ((2 + self.application.options.iTotalRounds) * ScreenGameComplete.ROW_SPACING)), (400, 100))
        self.buttons[0].y = 200 + (self.application.options.iTotalRounds * ScreenGameComplete.ROW_SPACING)


        super().draw(display, font)


        strText = "Game Complete"
        iOffsetX = (Globals.SCREEN_SIZE[0] -  DrawHelper.getTextSize(strText, font['normal'])[0]) / 2
        DrawHelper.drawTextShadow(strText, iOffsetX, 50, (255, 255, 255), display, font['normal'])

        DEFAULT_OFFSET_X = 400
        iOffsetY = 100
        iOffsetX = DEFAULT_OFFSET_X
        DrawHelper.drawTextShadow("Round", iOffsetX, iOffsetY, (255, 255, 255), display, font['normal'])

        iOffsetX += 200
        for player in self.application.gamemanager.players:
            DrawHelper.drawTextShadow(player.name, iOffsetX, iOffsetY, (255, 255, 255), display, font['normal'])
            iOffsetX += 200

        iOffsetY += 40

        for i in range(self.application.options.iTotalRounds):
            iOffsetX = DEFAULT_OFFSET_X
            DrawHelper.drawTextShadow(str(i + 1), iOffsetX, iOffsetY, (255, 255, 255), display, font['normal'])

            iOffsetX += 200
            for idx, player in enumerate(self.application.gamemanager.players):
                c = (255, 255, 255)
                if (len(player.iRoundScores) > i):
                    if (len(self.application.gamemanager.players[(idx + 1) % 2].iRoundScores) > i):
                        if (player.iRoundScores[i] > self.application.gamemanager.players[(idx + 1) % 2].iRoundScores[i]):
                            c = (255, 255, 0)
                    DrawHelper.drawTextShadow(str(player.iRoundScores[i]), iOffsetX, iOffsetY, c, display, font['normal'])

                iOffsetX += 200
            iOffsetY += 40


        iOffsetX = DEFAULT_OFFSET_X
        DrawHelper.drawTextShadow("Total", iOffsetX, iOffsetY, (255, 255, 255), display, font['normal'])
        iOffsetX += 200
        iSums = []
        for idx, player in enumerate(self.application.gamemanager.players):
            iSums.append(sum(player.iRoundScores))

        for idx, iSum in enumerate(iSums):
            c = (255, 255, 255)
            if (iSum > iSums[(idx + 1) % 2]):
                c = (255, 255, 0)
            DrawHelper.drawTextShadow(str(iSum), iOffsetX, iOffsetY, c, display, font['normal'])

            iOffsetX += 200
        iOffsetY += 40



    def doFinished(self):
        self.application.loadScreen("title")

