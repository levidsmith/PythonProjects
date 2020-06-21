#2020 Levi D. Smith - levidsmith.com
import pygame

from screen import Screen
from button import Button
from drawhelper import DrawHelper
from globals import Globals
from gamemanager import GameManager
from choosedealer import ChooseDealer

class ScreenChooseDealer(Screen):

    def __init__(self, init_application):
        super().__init__()
        self.application = init_application
        self.makeButtons()

    def restart(self):
        for button in self.buttons:
            button.hide()
            
    def makeButtons(self):
        iOffset = ((Globals.SCREEN_SIZE[0] - (128 * 3)) / 2) + (128 * 0)
        b = Button("Continue", iOffset, 500)
        b.action = self.doContinue
        b.hide()
        self.buttons.append(b)
        self.buttonBegin = b


    def update(self):
        self.application.choosedealer.update()


    def draw(self, display, font):
        gamemanager = self.application.gamemanager
        display.blit(self.application.gamemanager.background[0], (0, 0))

        super().draw(display, font)


        strText = "Choose Dealer"
        DrawHelper.drawTextShadow(strText, 1280/2, 4, (255, 255, 255), display, font['normal'])

        for card in self.application.choosedealer.cards:
            card.draw(display, font)

    def mouseMoved(self, mousePosition):
        gamemanager = self.application.gamemanager

        isHovered = self.isCursorHovered
        self.isCursorHovered = False #Set cursor hovered to false, and then set it to true if any cards or buttons are hovered

        super().mouseMoved(mousePosition)
      
        self.checkCardsHover(mousePosition[0], mousePosition[1])
        
        #compare the previous cursor state with the current cursor state
        #only change the cursor if the state changes, to reduce flicker
        if (isHovered != self.isCursorHovered):
            if (self.isCursorHovered):
                pygame.mouse.set_cursor(*pygame.cursors.diamond)
            else:
                pygame.mouse.set_cursor(*pygame.cursors.arrow)

    def checkCardsHover(self, x, y):
        choosedealer = self.application.choosedealer

        for card in choosedealer.cards:
            self.isCursorHovered = self.isCursorHovered or card.checkHovered(x, y)

    def mouseReleased(self, mousePosition):
        mouseX = mousePosition[0]
        mouseY = mousePosition[1]

        choosedealer = self.application.choosedealer

        for card in choosedealer.cards:
            if (self.application.gamemanager.isCardAtPosition(card, mouseX, mouseY)):
                self.chooseCard(card)

    def chooseCard(self, card):
        print("choose card: " + str(card))
        choosedealer = self.application.choosedealer

        choosedealer.chosen_card = card
        self.buttons[0].show()
            
    def doContinue(self):
        self.application.gamemanager.iCurrentPlayer = self.application.choosedealer.getDealerIndex()
        print ("Dealer is " + str(self.application.gamemanager.iCurrentPlayer))
        self.application.gamemanager.restart()
        self.application.loadScreen("game")            

