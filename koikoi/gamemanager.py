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

    deck_position = (64, 296)
    draw_card_position = (256, 296)

        
    def __init__(self, init_application):
        super().__init__()

        self.application = init_application
        self.players = []
        self.cards = []
        self.table = Table()
        self.draw_card = None
        self.load_images()
        self.load_audio()
        self.isCursorHovered = False

        self.iRound = 0
        self.iCurrentPlayer = -1

        #Highlight value used by all cards
        self.fHighlightValue = 0
        self.fHighlightIncrement = 0.03

    
    def load_images(self):
        self.card_images = []
        self.card_back_images = []
        for i in range(12):
            for j in range(4):
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

        self.surface_card_hint = pygame.Surface((64, 128))
        self.surface_card_hint.set_alpha(128)
        self.surface_card_hint.fill((255, 255, 0))

        self.surface_card_selected = pygame.Surface((64, 128))
        self.surface_card_selected.set_alpha(128)
        self.surface_card_selected.fill((0, 255, 0))


        imgBackground = pygame.image.load('images/background_game.jpg')
        self.background.append(imgBackground)

    def load_audio(self):
        pygame.mixer.music.load('audio/PyKoiKoi_game.mp3')
        pygame.mixer.music.set_volume(0.5)
        if (self.application.options.soundEffectsEnabled):
            self.sound_effects['card_drop'] = pygame.mixer.Sound('audio/card_drop.wav')
            self.sound_effects['next_player'] = pygame.mixer.Sound('audio/next_player.wav')

    def set_audio_volume(self, vol):
        pygame.mixer.music.set_volume(0)
    
    def restart(self):
        self.players.clear()
        self.table.restart()
        self.draw_card = None
        self.iRound = 0

        self.createDeck()
    

        #Create players
        p1 = Player(self)
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
        
        self.getCurrentPlayer().isPlayerTurn = True
        if (not self.getCurrentPlayer().isHuman):
            self.getCurrentPlayer().iWaitDelay = self.WAIT_DELAY

        self.checkHints()


        if (self.application.options.musicEnabled):
            pygame.mixer.music.play(-1)


    def createDeck(self):
        self.cards.clear()

        for i in range(12):
            for j in range(4):
                card = Card((i * 4) + j,  i * 80, j * 150, self.application)
                card.iMonth = i
                card.img = self.card_images[(i * 4) + j]
                card.img_back = self.card_back_images[0]
                card.img_border = self.card_back_images[1]
                card.surface_highlight = self.surface_card_highlight
                card.surface_hint = self.surface_card_hint
                card.surface_selected = self.surface_card_selected

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


    def dealCards(self):
        #Deal to the table
        for i in range(8):
            draw_card = self.cards.pop()
            draw_card.x = 0
            draw_card.y = (Globals.SCREEN_SIZE[1] - Card.h) / 2
            draw_card.isHidden = False
            self.table.addCard(draw_card)

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

        if (self.iRound >= self.application.options.iTotalRounds):
            if (self.application.options.musicEnabled):
                pygame.mixer.music.stop()

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

        self.table.restart()


        for card in self.cards:
            card.isHidden = True

        random.shuffle(self.cards)
        
        self.setCardPositions()
        self.dealCards()

    def update(self):
        for card in self.cards:
            card.update()


        for card in self.table.cards:
            card.update()
            
        if (self.draw_card != None):
            self.draw_card.update()
        
        for player in self.players:
            player.update()

        if ( (self.iCurrentPlayer >= 0) and (self.iCurrentPlayer < len(self.players)) and (not self.getCurrentPlayer().isPlayerTurn)):
            self.doNextPlayer()


        self.updateHighlight()


    def updateHighlight(self):

        self.fHighlightValue += self.fHighlightIncrement
        if (self.fHighlightValue > 1.0):
            self.fHighlightValue = 1.0
            self.fHighlightIncrement = -abs(self.fHighlightIncrement)
        elif (self.fHighlightValue < 0.0):
            self.fHighlightValue = 0.0
            self.fHighlightIncrement = abs(self.fHighlightIncrement)



    def doNextPlayer(self):
        self.iCurrentPlayer += 1
        if (self.iCurrentPlayer >= len(self.players)):
            self.iCurrentPlayer = 0
        
        self.players[self.iCurrentPlayer].isPlayerTurn = True
        self.players[self.iCurrentPlayer].iStep = Player.STEP_HAND_MATCH
        self.players[self.iCurrentPlayer].iWaitDelay = self.WAIT_DELAY

        self.checkHints()
        

        print("doNextPlayer " + str(self.iCurrentPlayer))
        if (self.application.options.soundEffectsEnabled):
            self.sound_effects['next_player'].play()
        
            

    def setCardPositions(self):
        i = 0
            
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
        self.table.setCardPositions()

        self.setCardPositions()
        
        for player in self.players:
            player.cards.sort(key=attrgetter('iMonth'))
            player.setCardPositions()
        
        
        
    def doContinue(self):
        print("Koi (Continue)")
        self.application.screens["game"].hideContinueButtons()

        currentPlayer = self.players[self.iCurrentPlayer]
        currentPlayer.doContinue()


        
        
    def doStop(self):
        print("Stop - End Round")
        self.application.screens["game"].hideContinueButtons()

# Use the lines below to stop the round, and make up a winning score for one of the players
#        self.iCurrentPlayer = randrange(0, 2)
#        self.players[self.iCurrentPlayer].score.iTotalPoints = randrange(10, 20)

        for player in self.players:
            if (player == self.getCurrentPlayer()):
                iPoints = player.score.iTotalPoints
                if (self.getIdlePlayer().score.isKoi):
                    iPoints *= 2
                if (player.score.iTotalPoints >= 7):
                    iPoints *= 2

                player.iRoundScores.append(iPoints)
                if (player.isHuman):
                    self.application.leaderboardmanager.submitScore(player.name, iPoints)

            else:
                player.iRoundScores.append(0)

            print("player " + player.name + ": " + str(player.iRoundScores))

        self.nextRound()
    

    def doStopDraw(self):
        print("Stop - Draw")
        for player in self.players:
            player.iRoundScores.append(0)

        self.nextRound()

    def continuePrompt(self):
        self.application.screens["game"].showContinueButtons()
        
    def doReturnToTitle(self):
        if (self.application.options.musicEnabled):
            pygame.mixer.music.stop()

        self.application.loadScreen("title")

    def checkHints(self):
        if (not self.application.options.showHints):
            return

        self.resetHints()
        print("gamemanager.checkHints()")

        if (self.getCurrentPlayer().iStep == Player.STEP_HAND_MATCH):

            if (self.getCurrentPlayer().selectedCard == None):
                print("selectedCard is None")
                for card_hand in self.getCurrentPlayer().cards:
                    #card_hand.isHint = False
                    for card_table in self.table.cards:
                        if (card_hand.iMonth == card_table.iMonth):
                            print("Found match card")
                            card_hand.isHint = True
            else:
                cardMatches = self.getCurrentPlayer().getPossibleMatches(self.getCurrentPlayer().selectedCard)
                for card in cardMatches:
                    card.isHint = True

        elif (self.getCurrentPlayer().iStep == Player.STEP_DRAW):
            for card in self.cards:
                if (card == self.cards[len(self.cards) - 1]):
                    card.isHint = True

        elif (self.getCurrentPlayer().iStep == Player.STEP_DRAW_MATCH):
            if (self.getCurrentPlayer().selectedCard == None and self.draw_card != None):
                self.draw_card.isHint = True
            else:
                cardMatches = self.getCurrentPlayer().getPossibleMatches(self.draw_card)
                for card in cardMatches:
                    card.isHint = True

    def resetHints(self):
        print("resetHints()")
        for player in self.players:
            for card in player.cards:
                card.isHint = False

            for card in player.match_cards:
                card.isHint = False

            if (player.selectedCard != None):
                player.selectedCard.isHint = False

            for card in self.table.cards:
                card.isHint = False
        
        for card in self.table.cards:
            card.isHint = False

        for card in self.cards:
            card.isHint = False

        

    def getCurrentPlayer(self):
        currentplayer = None
        if ( (self.iCurrentPlayer >= 0) and (self.iCurrentPlayer < len(self.players))):
            currentplayer = self.players[self.iCurrentPlayer]

        return currentplayer

    def getIdlePlayer(self):
        idleplayer = None
        iIdle = (self.iCurrentPlayer + 1) % 2
        if ((iIdle >= 0) and (iIdle < len(self.players))):
            idleplayer =  self.players[(self.iCurrentPlayer + 1) % 2]        
       
        return idleplayer
