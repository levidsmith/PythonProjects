#2020 Levi D. Smith - levidsmith.com
import pygame
import random
import math
import os.path

from card import Card
from player import Player
from drawhelper import DrawHelper
from globals import Globals

class GameManager:

    WAIT_DELAY = 60 * 2

    players = []
    cards = []
    card_images = []
    card_back_images = []
    table = []
    background = []

    iCurrentPlayer = 0
    
    deck_position = (64, 296)
    table_position = (400, 200)
    
    def __init__(self):
        self.load_images()
        self.restart()

    def load_images(self):
        for i in range(12):
            for j in range(4):
                print(str(i) + ", " + str(j))
                strFile = 'images/hanafuda_' + str(i + 1) + '-' + str(j + 1) + '.jpg'
                if (os.path.isfile(strFile)):
                    img = pygame.image.load(strFile)
                    img = pygame.transform.scale(img, (Card.w, Card.h))
                    #self.card_images[(i * 4) + j] = img
                    self.card_images.append(img)


        img = pygame.image.load('images/hanafuda_back.jpg')
        img = pygame.transform.scale(img, (Card.w, Card.h))
        self.card_back_images.append(img)

        img = pygame.image.load('images/card_border.png')
        self.card_back_images.append(img)


        imgBackground = pygame.image.load('images/background.jpg')
        self.background.append(imgBackground)
    
    def restart(self):
        self.iCurrentPlayer = 0
        self.players.clear()
        self.cards.clear()
        self.table.clear()
    
        for i in range(12):
            for j in range(4):
#                print(str(i) + ", " + str(j))
                card = Card((i * 4) + j,  i * 80, j * 150)
                card.iMonth = i
                card.img = self.card_images[(i * 4) + j]
                card.img_back = self.card_back_images[0]
                card.img_border = self.card_back_images[1]

#                strFile = 'images/hanafuda_' + str(i + 1) + '-' + str(j + 1) + '.jpg'
#                if (os.path.isfile(strFile)):
#                    card.img = pygame.image.load(strFile)
 #                   card.img = pygame.transform.scale(card.img, (card.w, card.h))
                
            
            
                if (i == 0):
                    if (j == 2):
                        card.isRedRibbon = True
                        card.isPoetryRibbon = True
                    if (j == 3):
                        card.isLight = True

                if (i == 1):
                    if (j == 2):
                        card.isRedRibbon = True
                        card.isPoetryRibbon = True
                    if (j == 3):
                        card.isSpecial = True

                if (i == 2):
                    if (j == 2):
                        card.isRedRibbon = True
                        card.isPoetryRibbon = True
                    if (j == 3):
                        card.isLight = True

                if (i == 3):
                    if (j == 2):
                        card.isRedRibbon = True
                    if (j == 3):
                        card.isSpecial = True

                if (i == 4):
                    if (j == 2):
                        card.isRedRibbon = True
                    if (j == 3):
                        card.isSpecial = True

                if (i == 5):
                    if (j == 2):
                        card.isBlueRibbon = True
                    if (j == 3):
                        card.isSpecial = True
                        card.isBoarDeerButterfly = True

                if (i == 6):
                    if (j == 2):
                        card.isRedRibbon = True
                    if (j == 3):
                        card.isSpecial = True
                        card.isBoarDeerButterfly = True

                if (i == 7):
                    if (j == 2):
                        card.isSpecial = True
                    if (j == 3):
                        card.isLight = True

                if (i == 8):
                    if (j == 2):
                        card.isBlueRibbon = True
                    if (j == 3):
                        card.isSakeCup = True

                if (i == 9):
                    if (j == 2):
                        card.isBlueRibbon = True
                    if (j == 3):
                        card.isSpecial = True
                        card.isBoarDeerButterfly = True

                if (i == 10):
                    if (j == 1):
                        card.isSpecial = True
                    if (j == 2):
                        card.isRedRibbon = True
                    if (j == 3):
                        card.isRainMan = True

                if (i == 11):
                    if (j == 3):
                        card.isLight = True

                
            
                self.cards.append(card)
        
        random.shuffle(self.cards)
        
        i = 0
        for card in self.cards:
            card.x = self.deck_position[0] + (i * 2)
            card.y = self.deck_position[1]
            card.targetPosition = (card.x, card.y)
            i += 1


        #Deal to the table
        for i in range(8):
            draw_card = self.cards.pop()
            draw_card.x = 0
            draw_card.y = (Globals.SCREEN_SIZE[1] - Card.h) / 2
            draw_card.isHidden = False
            draw_card.targetPosition = (480 + ((i % 4) * 80), 200 + 160 * math.floor(i / 4))
            self.table.append(draw_card)

        #Create players
        p1 = Player(self)
        p1.name = "Player One"
        p1.isHidden = True
        p1.position = (64, 32)
        for i in range(8):
            draw_card = self.cards.pop()
            draw_card.x = 0
            draw_card.y = p1.position[1]
            draw_card.targetPosition = (p1.position[0] + (i * 80), p1.position[1])
            p1.cards.append(draw_card)

        self.players.append(p1)
    



        p2 = Player(self)
        p2.name = "Player Two"
        p2.isHidden = False
        p2.position = (64, 512)
        for i in range(8):
            draw_card = self.cards.pop()
            draw_card.x = 0
            draw_card.y = p2.position[1]
            draw_card.isHidden = False
            
            draw_card.targetPosition = (p2.position[0] + (i * 80), p2.position[1])
            p2.cards.append(draw_card)

        self.players.append(p2)
        
        self.players[self.iCurrentPlayer].isPlayerTurn = True
        self.players[self.iCurrentPlayer].iWaitDelay = self.WAIT_DELAY



    def update(self):
#        print ("GameManager update")
        for card in self.table:
            card.update()
        
        for player in self.players:
            player.update()

#        print ("Current Player: " + str(self.iCurrentPlayer))
        self.setCardPositions()

        if (not self.players[self.iCurrentPlayer].isPlayerTurn):
            self.doNextPlayer()
          

                
    def draw(self, display, font):
        display.blit(self.background[0], (0, 0))

        for card in self.cards:
            card.draw(display, font)

        for card in self.table:
            card.draw(display, font)
        
        for player in self.players:
            player.draw(display, font)

        strCopyright = '2020 Levi D. Smith'
#        c = (255, 255, 255)
#        text = font.render(strCopyright, True, c)
#        display.blit(text, (1000, 680))
        DrawHelper.drawTextShadow(strCopyright, 500, 720-32, (255, 255, 255), display, font[1])

    def doNextPlayer(self):
        self.iCurrentPlayer += 1
        if (self.iCurrentPlayer >= len(self.players)):
            self.iCurrentPlayer = 0
        
        self.players[self.iCurrentPlayer].isPlayerTurn = True
        self.players[self.iCurrentPlayer].iWaitDelay = self.WAIT_DELAY
        

        print("doNextPlayer " + str(self.iCurrentPlayer))
            

    def setCardPositions(self):
        i = 0
        
        for card in self.table:
            card.targetPosition = (self.table_position[0] + ((i % 4) * 80), self.table_position[1] + 160 * math.floor(i / 4))
            i += 1

