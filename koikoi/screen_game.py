#2020 Levi D. Smith - levidsmith.com
import pygame

from screen import Screen
from button import Button
from drawhelper import DrawHelper
from globals import Globals
from gamemanager import GameManager

class ScreenGame(Screen):

    def __init__(self, init_application):
        super().__init__()
        self.application = init_application
        self.makeButtons()

    def update(self):
        self.application.gamemanager.update()

    def draw(self, display, font):
        display.blit(self.application.gamemanager.background[0], (0, 0))
        gamemanager = self.application.gamemanager

        gamemanager.table.draw(display, font)

        for card in gamemanager.cards:
            card.draw(display, font)

        for card in gamemanager.table.cards:
            card.draw(display, font)
        
        if (gamemanager.draw_card != None):
            gamemanager.draw_card.draw(display, font)
        
        for player in gamemanager.players:
            player.draw(display, font)
            
        for button in self.buttons:
            button.draw(display, font)


        strRound = "Round " + str(gamemanager.iRound + 1)
        DrawHelper.drawTextShadow(strRound, 1280/2, 4, (255, 255, 255), display, font['normal'])

        DrawHelper.drawTextShadow(str(len(gamemanager.cards)), 20, 360, (255, 255, 255), display, font['normal'])


        strCopyright = '2020 Levi D. Smith'
        DrawHelper.drawTextShadow(strCopyright, 500, 720-32, (255, 255, 255), display, font['normal'])

    
    def makeButtons(self):
        b = Button("Arrange", 0, 0)
        b.action = self.application.gamemanager.arrangeCards
        b.show()
        self.buttons.append(b)

        b = Button("Koi", 200, 0)
        b.action = self.application.gamemanager.doContinue
        b.hide()
        self.buttons.append(b)
        
        b = Button("Stop", 400, 0)
        b.action = self.application.gamemanager.doStop
        b.hide()
        self.buttons.append(b)

        b = Button("Quit", 1100, 688)
        b.action = self.application.gamemanager.doReturnToTitle
        b.show()
        self.buttons.append(b)


    def mousePressed(self, mousePosition):
        super().mousePressed(mousePosition)
        currentPlayer = self.application.gamemanager.players[self.application.gamemanager.iCurrentPlayer]
        currentPlayer.mousePressed(mousePosition[0], mousePosition[1])
    
    def mouseReleased(self, mousePosition):
        mouseX = mousePosition[0]
        mouseY = mousePosition[1]
        currentPlayer = self.application.gamemanager.players[self.application.gamemanager.iCurrentPlayer]
        currentPlayer.mouseReleased(mouseX, mouseY)

        
    def mouseMoved(self, mousePosition):
        mouseX = mousePosition[0]
        mouseY = mousePosition[1]

        gamemanager = self.application.gamemanager

        isHovered = self.isCursorHovered
        self.isCursorHovered = False #Set cursor hovered to false, and then set it to true if any cards or buttons are hovered

        super().mouseMoved(mousePosition)

        currentPlayer = gamemanager.players[gamemanager.iCurrentPlayer]
        currentPlayer.dragCard(mouseX, mouseY)
        
        self.checkCardsHover(mouseX, mouseY)
        
        #compare the previous cursor state with the current cursor state
        #only change the cursor if the state changes, to reduce flicker
        if (isHovered != self.isCursorHovered):
            if (self.isCursorHovered):
                pygame.mouse.set_cursor(*pygame.cursors.diamond)
            else:
                pygame.mouse.set_cursor(*pygame.cursors.arrow)
            
            
    def checkCardsHover(self, x, y):
        gamemanager = self.application.gamemanager

        for card in gamemanager.table.cards:
            self.isCursorHovered = self.isCursorHovered or card.checkHovered(x, y)

        for card in gamemanager.cards:
            self.isCursorHovered = self.isCursorHovered or card.checkHovered(x, y)

        if (gamemanager.draw_card != None):
            if (gamemanager.draw_card != gamemanager.players[gamemanager.iCurrentPlayer].selectedCard):
                self.isCursorHovered = self.isCursorHovered or gamemanager.draw_card.checkHovered(x, y)

        
        for player in gamemanager.players:
            for card in player.cards:
                if (card != player.selectedCard):
                    self.isCursorHovered = self.isCursorHovered or card.checkHovered(x, y)
        
            for card in player.match_cards:
                self.isCursorHovered = self.isCursorHovered or card.checkHovered(x, y)

        #check table hovered
        gamemanager.table.isSelected = False
        if (not self.isCursorHovered):
            self.isCursorHovered = self.isCursorHovered or gamemanager.table.checkHovered(x, y)

    def showContinueButtons(self):
        self.buttons[1].show()
        self.buttons[2].show()



    def hideContinueButtons(self):
        self.buttons[1].hide()
        self.buttons[2].hide()
