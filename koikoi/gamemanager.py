#2020 Levi D. Smith - levidsmith.com
import pygame
import random
import math
import os.path

from screen import Screen
from card import Card
from player import Player
from table import Table
from button import Button
from drawhelper import DrawHelper
from globals import Globals
from random import randrange

from operator import itemgetter, attrgetter

class GameManager():

    WAIT_DELAY = 60 * 2

    sound_effects = {}
    
    background = []

    iCurrentPlayer = 0
    
    deck_position = (64, 296)
    draw_card_position = (256, 296)
    
    
    def __init__(self, init_application):
        super().__init__()

#        self.iTotalRounds = 6
        self.application = init_application
        self.players = []
        self.cards = []
        self.table = Table()
        self.load_images()
        self.load_audio()
#        self.restart()

#        self.makeButtons()
        self.isCursorHovered = False
        
        



    
    def load_images(self):
        self.card_images = []
        self.card_back_images = []
        for i in range(12):
            for j in range(4):
#                print(str(i) + ", " + str(j))
                strFile = 'images/hanafuda_' + str(i + 1) + '-' + str(j + 1) + '.jpg'
                if (os.path.isfile(strFile)):
                    img = pygame.image.load(strFile)
                    img = pygame.transform.scale(img, (Card.w, Card.h))
                    self.card_images.append(img)


        img = pygame.image.load('images/hanafuda_back.jpg')
        img = pygame.transform.scale(img, (Card.w, Card.h))
        self.card_back_images.append(img)

        img = pygame.image.load('images/card_border.png')
        self.card_back_images.append(img)

        self.surface_card_highlight = pygame.Surface((64, 128))
        self.surface_card_highlight.set_alpha(128)
        self.surface_card_highlight.fill((255, 0, 0))


        imgBackground = pygame.image.load('images/background_game.jpg')
        self.background.append(imgBackground)

    def load_audio(self):
        pygame.mixer.music.load('audio/PyKoiKoi_game.mp3')
        pygame.mixer.music.set_volume(0.5)
        self.sound_effects['card_drop'] = pygame.mixer.Sound('audio/card_drop.wav')
        self.sound_effects['next_player'] = pygame.mixer.Sound('audio/next_player.wav')

    def set_audio_volume(self, vol):
        pygame.mixer.music.set_volume(0)
    
    def restart(self):
        self.iCurrentPlayer = 0
        self.players.clear()
        self.cards.clear()
        self.table.cards.clear()
        self.draw_card = None
        self.iRound = 0
    
        for i in range(12):
            for j in range(4):
                card = Card((i * 4) + j,  i * 80, j * 150, self.application)
                card.iMonth = i
                card.img = self.card_images[(i * 4) + j]
                card.img_back = self.card_back_images[0]
                card.img_border = self.card_back_images[1]
                card.surface_highlight = self.surface_card_highlight

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
                        card.isSakuraCurtain = True

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
                        card.isMoon = True

                if (i == 8):
                    if (j == 2):
                        card.isBlueRibbon = True
                    if (j == 3):
                        card.isSakeCup = True
                        card.isNormal = True

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
        


        

        #Create players
        p1 = Player(self)
#        p1.name = "CPU"
        p1.isHidden = True
        p1.position = (64, 32)
        p1.score_offset = (1000, 200)
        p1.card_types_offset = (1000, -20)
        p1.match_card_position = (660, 0)
        if (p1.isHuman):
            p1.name = self.application.options.strName
        else:
            p1.name = "CPU"
        self.players.append(p1)
    



        p2 = Player(self)
#        p2.name = "Player"

        print("Name is " + self.application.options.strName)
        p2.name = self.application.options.strName
        p2.isHidden = False
        p2.isHuman = True
        if (p2.isHuman):
            p2.name = self.application.options.strName
        else:
            p2.name = "CPU"

        p2.position = (64, 512)
        p2.score_offset = (1000, 60)
        p2.card_types_offset = (1000, -140)
        p2.match_card_position = (660, 0)
        

        self.players.append(p2)
        
        self.dealCards()
        
        self.players[self.iCurrentPlayer].isPlayerTurn = True
        self.players[self.iCurrentPlayer].iWaitDelay = self.WAIT_DELAY
        
        pygame.mixer.music.play(-1)

    def dealCards(self):
        #Deal to the table
        for i in range(8):
            draw_card = self.cards.pop()
            draw_card.x = 0
            draw_card.y = (Globals.SCREEN_SIZE[1] - Card.h) / 2
            draw_card.isHidden = False
            self.table.cards.append(draw_card)

        self.setCardPositions()

        for player in self.players:

            for i in range(8):
                draw_card = self.cards.pop()
                draw_card.x = 0
                draw_card.y = player.position[1]
                if (player.isHuman):
                    draw_card.isHidden = False
                else:
                    draw_card.isHidden = True
            
                draw_card.targetPosition = (player.position[0] + (i * 80), player.position[1])
                player.cards.append(draw_card)

    
    
    def nextRound(self):
        self.iRound += 1

#        if (self.iRound >= self.iTotalRounds):
        if (self.iRound >= self.application.options.iTotalRounds):
            self.application.loadScreen("gamecomplete")

            

        for player in self.players:
            while (len(player.cards) > 0):
                card = player.cards.pop()
                self.cards.append(card)

            while (len(player.match_cards) > 0):
                card = player.match_cards.pop()
                self.cards.append(card)

        
            player.setCardPositions()
            player.nextRound()


        while (len(self.table.cards) > 0):
            card = self.table.cards.pop()
            self.cards.append(card)

            
        for card in self.cards:
            card.isHidden = True

        random.shuffle(self.cards)
        
        self.setCardPositions()
        self.dealCards()


    def update(self):
#        print ("GameManager update")
        for card in self.table.cards:
            card.update()
            
        if (self.draw_card != None):
            self.draw_card.update()
        
        for player in self.players:
            player.update()


        if (not self.players[self.iCurrentPlayer].isPlayerTurn):
            self.doNextPlayer()
          

                

    def doNextPlayer(self):
        self.iCurrentPlayer += 1
        if (self.iCurrentPlayer >= len(self.players)):
            self.iCurrentPlayer = 0
        
        self.players[self.iCurrentPlayer].isPlayerTurn = True
        self.players[self.iCurrentPlayer].iStep = Player.STEP_HAND_MATCH
        self.players[self.iCurrentPlayer].iWaitDelay = self.WAIT_DELAY
        

        print("doNextPlayer " + str(self.iCurrentPlayer))
        self.sound_effects['next_player'].play()
        
            

    def setCardPositions(self):
        i = 0
        iCardsPerRow = math.ceil(len(self.table.cards) / 2)
        
        for card in self.table.cards:
            card.targetPosition = (self.table.position[0] + ((i % iCardsPerRow) * 80), self.table.position[1] + 160 * math.floor(i / iCardsPerRow))
            i += 1
            
        for card in self.cards:
            card.x = self.deck_position[0] + (i * 2)
            card.y = self.deck_position[1]
            card.targetPosition = (card.x, card.y)
            i += 1




    
        
            
    def isCardAtPosition(self, card, x, y):
        isCardAtPosition = False
        if (x > card.x and x < card.x + card.w and y > card.y and y < card.y + card.h):
            isCardAtPosition = True
            
        return isCardAtPosition
        
        
    def arrangeCards(self):
        print("arrangeCards")
        self.table.cards.sort(key=attrgetter('iMonth'))
        self.setCardPositions()
        
        for player in self.players:
            player.cards.sort(key=attrgetter('iMonth'))
            player.setCardPositions()
        
        
        
    def doContinue(self):
        print("Koi (Continue)")
#        super().buttons[1].hide()
#        super().buttons[2].hide()
        self.application.screens["game"].hideContinueButtons()

        currentPlayer = self.players[self.iCurrentPlayer]
        currentPlayer.doContinue()


        
        
    def doStop(self):
        print("Stop - End Round")
        self.application.screens["game"].hideContinueButtons()
#        super().buttons[1].hide()
#        super().buttons[2].hide()

# Use the lines below to stop the round, and make up a winning score for one of the players
#        self.iCurrentPlayer = randrange(0, 2)
#        self.players[self.iCurrentPlayer].score.iTotalPoints = randrange(10, 20)

        for player in self.players:
            if (player == self.players[self.iCurrentPlayer]):
                iPoints = player.score.iTotalPoints
                if (self.players[(self.iCurrentPlayer + 1) % 2].score.isKoi):
                    iPoints *= 2
                player.iRoundScores.append(iPoints)
                if (player.isHuman):
                    self.application.leaderboardmanager.submitScore(player.name, iPoints)

            else:
                player.iRoundScores.append(0)

            print("player " + player.name + ": " + str(player.iRoundScores))


        
        self.nextRound()
        
    
    
    def continuePrompt(self):
        #show the "Koi" and "Stop" buttons
        self.application.screens["game"].showContinueButtons()
#        super().buttons[1].show()
#        super().buttons[2].show()
        
    def doReturnToTitle(self):
        self.application.loadScreen("title")
