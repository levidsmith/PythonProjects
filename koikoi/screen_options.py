#2020 Levi D. Smith - levidsmith.com
import pygame

from button import Button
from screen import Screen
from drawhelper import DrawHelper
from globals import Globals

class ScreenOptions(Screen):

    def __init__(self, init_application):
        super().__init__()
        print("init")
        self.application = init_application
        self.buttonBegin = None
        self.makeButtons()
        self.imgBackground = None
        self.load_images()

    def load_images(self):
        self.imgBackground = pygame.image.load('images/background_options.jpg')


    def makeButtons(self):
        iOffset = ((Globals.SCREEN_SIZE[0] - (128 * 3)) / 2) + (128 * 0)
        b = Button("Begin", iOffset, 500)
        b.action = self.doBegin
        b.hide()
        self.buttons.append(b)
        self.buttonBegin = b

        iOffset = ((Globals.SCREEN_SIZE[0] - (128 * 3)) / 2) + (128 * 2)
        b = Button("Back", iOffset, 500)
        b.action = self.doBack
        b.show()
        self.buttons.append(b)


        iOffsetX = 64
        iOffsetValueX = 512
        iOffsetY = 200
        iSpacing = 40


        iRoundOptions = [1, 3, 6, 12]
        for idx, iRoundOption in enumerate(iRoundOptions):
            b = Button(str(iRoundOption), iOffsetValueX + 256 + (idx * (128 + 8)), iOffsetY + (iSpacing * 1))
            b.action = self.doSetRounds
            b.action_params = iRoundOption
            b.show()
            self.buttons.append(b)

        self.yesnoOptions = [True, False]
        self.yesnoMap = {}
        self.yesnoMap[True] = "Yes"
        self.yesnoMap[False] = "No"

        self.onoffOptions = [True, False]
        self.onoffMap = {}
        self.onoffMap[True] = "On"
        self.onoffMap[False] = "Off"



        for idx, hintEnabled in enumerate(self.yesnoOptions):
            b = Button(self.yesnoMap[hintEnabled], iOffsetValueX + 256 + (idx * (128 + 8)), iOffsetY + (iSpacing * 2))
            b.action = self.doSetHint
            b.action_params = hintEnabled
            b.show()
            self.buttons.append(b)

        for idx, showMonthEnabled in enumerate(self.yesnoOptions):
            b = Button(self.yesnoMap[showMonthEnabled], iOffsetValueX + 256 + (idx * (128 + 8)), iOffsetY + (iSpacing * 3))
            b.action = self.doSetShowMonth
            b.action_params = showMonthEnabled
            b.show()
            self.buttons.append(b)

        for idx, showCardTypeEnabled in enumerate(self.yesnoOptions):
            b = Button(self.yesnoMap[showCardTypeEnabled], iOffsetValueX + 256 + (idx * (128 + 8)), iOffsetY + (iSpacing * 4))
            b.action = self.doSetShowCardType
            b.action_params = showCardTypeEnabled
            b.show()
            self.buttons.append(b)

        for idx, musicEnabled in enumerate(self.onoffOptions):
            b = Button(self.onoffMap[musicEnabled], iOffsetValueX + 256 + (idx * (128 + 8)), iOffsetY + (iSpacing * 5))
            b.action = self.doSetMusicEnabled
            b.action_params = musicEnabled
            b.show()
            self.buttons.append(b)


    def update(self):
        pass


    def draw(self, display, font):
        iOffsetX = 64
        iOffsetValueX = 512
        iOffsetY = 200
        iSpacing = 40

        display.blit(self.imgBackground, (0, 0))

        super().draw(display, font)


        DrawHelper.drawTextShadow("Name", iOffsetX, iOffsetY + (iSpacing * 0), (255, 255, 255), display, font['normal'])
        DrawHelper.drawTextShadow(self.application.options.strName + "|", iOffsetValueX, iOffsetY + (iSpacing * 0), (255, 255, 0), display, font['normal'])

        DrawHelper.drawTextShadow("Rounds", iOffsetX, iOffsetY + (iSpacing * 1), (255, 255, 255), display, font['normal'])
        DrawHelper.drawTextShadow(str(self.application.options.iTotalRounds), iOffsetValueX, iOffsetY + (iSpacing * 1), (255, 255, 0), display, font['normal'])



        DrawHelper.drawTextShadow("Show Hints", iOffsetX, iOffsetY + (iSpacing * 2), (255, 255, 255), display, font['normal'])
        strValue = ""
        DrawHelper.drawTextShadow(self.yesnoMap[self.application.options.showHints], iOffsetValueX, iOffsetY + (iSpacing * 2), (255, 255, 0), display, font['normal'])

        DrawHelper.drawTextShadow("Show Month Number", iOffsetX, iOffsetY + (iSpacing * 3), (255, 255, 255), display, font['normal'])
        DrawHelper.drawTextShadow(self.yesnoMap[self.application.options.showMonth], iOffsetValueX, iOffsetY + (iSpacing * 3), (255, 255, 0), display, font['normal'])

        DrawHelper.drawTextShadow("Show Card Type", iOffsetX, iOffsetY + (iSpacing * 4), (255, 255, 255), display, font['normal'])
        DrawHelper.drawTextShadow(self.yesnoMap[self.application.options.showCardType], iOffsetValueX, iOffsetY + (iSpacing * 4), (255, 255, 0), display, font['normal'])

        DrawHelper.drawTextShadow("Music", iOffsetX, iOffsetY + (iSpacing * 5), (255, 255, 255), display, font['normal'])
        DrawHelper.drawTextShadow(self.onoffMap[self.application.options.musicEnabled], iOffsetValueX, iOffsetY + (iSpacing * 5), (255, 255, 0), display, font['normal'])


    def doBegin(self):
        if (len(self.application.options.strName) >= 3):
            print("options name: " + self.application.options.strName)
            self.application.choosedealer.restart()
            self.application.loadScreen("choosedealer")            

    def doBack(self):
        self.application.loadScreen("title")

    def keyInputChar(self, inputChar):
        self.application.options.strName += inputChar
        self.checkComplete()

    def keyInputDelete(self):
        self.application.options.strName = self.application.options.strName[:-1]
        self.checkComplete()

    def checkComplete(self):
        if (len(self.application.options.strName) >= 3):
            self.buttonBegin.isHidden = False
        else:
            self.buttonBegin.isHidden = True


    def doSetRounds(self, iRounds):
        print("set rounds " + str(iRounds))
        self.application.options.iTotalRounds = iRounds

    def doSetHint(self, hintEnabled):
        print("set hint " + str(hintEnabled))
        self.application.options.showHints = hintEnabled

    def doSetShowMonth(self, showMonthEnabled):
        print("show month " + str(showMonthEnabled))
        self.application.options.showMonth = showMonthEnabled

    def doSetShowCardType(self, showCardTypeEnabled):
        print("show card type " + str(showCardTypeEnabled))
        self.application.options.showCardType = showCardTypeEnabled

    def doSetMusicEnabled(self, musicEnabled):
        print("music enabled " + str(musicEnabled))
        self.application.options.musicEnabled = musicEnabled