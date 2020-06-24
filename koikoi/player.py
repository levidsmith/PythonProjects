#2020 Levi D. Smith - levidsmith.com
import pygame
import math

from card import Card
from score import Score
from drawhelper import DrawHelper
from random import randrange


class Player:
    STEP_HAND_MATCH = 0
    STEP_DRAW = 1
    STEP_DRAW_MATCH = 2
    STEP_DONE = 3
    STEP_HAND_MATCH_CONTINUE = 4
    STEP_DRAW_MATCH_CONTINUE = 5
    STEP_NAMES = ("Hand Match or Discard to table", "Draw", "Draw Match or Discard to table", "Done", "Continue to Draw", "Continue to Done")
    
    MATCH_CARDS_PER_ROW = 8
    
    
    def __init__(self, init_gamemanager):
        self.cards = []
        self.match_cards = []
        self.score = Score()
        self.iRoundScores = []
        self.isPlayerTurn = False
        self.iWaitDelay = 0
        self.gamemanager = init_gamemanager
        self.isHidden = True

        self.score.checkScore(self.match_cards)
        self.isHuman = False
        self.iStep = Player.STEP_HAND_MATCH
        self.selectedCard = None
        self.selectedOffset = (0, 0)
        self.name = "hello"
    
    def update(self):
        for card in self.cards:
            card.update()

        for card in self.match_cards:
            card.update()
              
        if (self.iWaitDelay > 0):
            self.iWaitDelay -= 1
            
        if (self.isPlayerTurn and self.iWaitDelay <= 0):
            self.playTurn()
    
    def draw(self, display, font):
        for card in self.cards:
            card.draw(display, font)



        for card in self.match_cards:
            card.draw(display, font)


        c = (255, 255, 255)
        c_bkg = (0, 0, 0)


        if (self.isPlayerTurn):
            c = (255, 255, 0)

        DrawHelper.drawTextShadow(self.name, self.position[0] + 48, self.position[1] + 128, c, display, font['normal'])
        if (self.isPlayerTurn):
            DrawHelper.drawTextShadow(Player.STEP_NAMES[self.iStep], self.position[0], self.position[1] + 128 + 32, (0, 255, 255), display, font['small'])
        
        DrawHelper.drawTextShadow(self.score.card_type_totals_text, self.position[0] + self.card_types_offset[0], self.position[1] + self.card_types_offset[1], (255, 255, 255), display, font['small'])

        DrawHelper.drawTextShadow(self.score.score_text, self.position[0] + self.score_offset[0], self.position[1] + self.score_offset[1], (255, 255, 255), display, font['small'])


        
        iMatchScore = 0
        strRoundsScore = ""
        for iScore in self.iRoundScores:
            iMatchScore += iScore
            strRoundsScore += str(iScore) + ","
            
        strMatchScore = str(iMatchScore)

        DrawHelper.drawTextShadow(strMatchScore, self.position[0], self.position[1] + 128, (255, 128, 0), display, font['normal'])

        if (self.score.isKoi):
            DrawHelper.drawTextShadow("KOI", self.position[0] + 200, self.position[1] + 128, (255, 0, 0), display, font['normal'])

            
            
            
    def playTurn(self):
        if (not self.isHuman):
            
            if (self.iStep == Player.STEP_HAND_MATCH):
                self.checkHandMatchCPU()
                self.iWaitDelay = 2 * 60
            
            elif (self.iStep == Player.STEP_HAND_MATCH_CONTINUE):
                self.checkContinueCPU()
                self.iWaitDelay = 2 * 60
            
            elif (self.iStep == Player.STEP_DRAW):
                self.drawCard()
                self.iWaitDelay = 2 * 60
            elif (self.iStep == Player.STEP_DRAW_MATCH):
                self.checkDrawMatchCPU()
                self.iWaitDelay = 2 * 60
            elif (self.iStep == Player.STEP_DRAW_MATCH_CONTINUE):
                self.checkContinueCPU()
                self.iWaitDelay = 2 * 60

        
        if (self.iStep == Player.STEP_HAND_MATCH and len(self.cards) == 0):
            self.iStep = Player.STEP_DRAW

        if (self.iStep == Player.STEP_DRAW and len(self.gamemanager.cards) == 0):
            self.iStep = Player.STEP_DONE
            self.gamemanager.doStopDraw()
            


        if (self.iStep == Player.STEP_DONE):
            self.setCardPositions()
            self.gamemanager.setCardPositions()
            self.isPlayerTurn = False
        
        
    def checkHandMatchCPU(self):
        print("checking match")
        match_card1 = None
        match_card2 = None

        for card_hand in self.cards:
            for card_table in self.gamemanager.table.cards:
                if (card_hand.iMonth == card_table.iMonth):
                    match_card1 = card_hand
                    match_card2 = card_table
                    
        if ( (match_card1 != None) and (match_card2 != None)):
            successfulMatch = self.doMatch(match_card1, match_card2)
            if (successfulMatch):
                if (self.score.hasNewScore):
                    self.iStep = Player.STEP_HAND_MATCH_CONTINUE
                    self.continuePrompt()
                else:
                    self.iStep = Player.STEP_DRAW

        else:
            if (len(self.cards) > 0):
                self.doDiscard(self.cards[0]) #Just discard the first card in the hand for now
            
            self.iStep = Player.STEP_DRAW
            

    def checkDrawMatchCPU(self):
        print("checking match")
        match_card = None
        draw_card = self.gamemanager.draw_card

        for card_table in self.gamemanager.table.cards:
            if (draw_card.iMonth == card_table.iMonth):
                match_card = card_table
                    
        if (match_card != None):
            successfulMatch = self.doMatch(draw_card, match_card)
        else:
            self.doDiscard(draw_card)
            


        if (self.score.hasNewScore):
            self.iStep = Player.STEP_DRAW_MATCH_CONTINUE
            self.continuePrompt()
        else:
            self.iStep = Player.STEP_DONE
                    

    def checkContinueCPU(self):
        #We should have fancy AI here to figure out if they should continue
        iRand = randrange(1, 100)
#        iRand = randrange(1, 49) #Always koi
        print("Random choice value is " + str(iRand))
        if (iRand < 50):
            self.gamemanager.doContinue()
        else:
            self.gamemanager.doStop()
    

    def doMatch(self, match_card1, match_card2):
        successfulMatch = False
    
        print("Match - Month " + str(match_card1.iMonth) + " - IDs " + str(match_card1.id) + ", " + str(match_card2.id))
        
        possible_matches = self.getPossibleMatches(match_card1)
        
        if (match_card2 in possible_matches):
            self.match_cards.append(match_card1)
            match_card1.isHidden = False
            if (match_card1 in self.cards):
                self.cards.remove(match_card1)


            if (len(possible_matches) == 3):  #handle the special case of three matching cards
                for card in possible_matches:
                    self.match_cards.append(card)
                    self.gamemanager.table.removeCard(card)

            else:
                self.match_cards.append(match_card2)
                self.gamemanager.table.removeCard(match_card2)


            self.score.checkScore(self.match_cards)
            self.setCardPositions()
            successfulMatch = True
            self.gamemanager.sound_effects['card_drop'].play()
            
                
        
        return successfulMatch
        
    
    def getPossibleMatches(self, match_card):
        possible_matches = []
        for card in self.gamemanager.table.cards:
            if (match_card.iMonth == card.iMonth):
                possible_matches.append(card)
        return possible_matches
                
                
    
    def drawCard(self):
        if (len(self.gamemanager.cards) > 0):
            draw_card = self.gamemanager.cards.pop()
            draw_card.isHidden = False
            draw_card.targetPosition = self.gamemanager.draw_card_position

            self.gamemanager.draw_card = draw_card
            self.iStep = Player.STEP_DRAW_MATCH
            self.gamemanager.checkHints()
        else:
            print("No more cards")
      
    def doDiscard(self, card):
        card.isHidden = False
        self.gamemanager.table.addCard(card)
        self.gamemanager.setCardPositions()
        if (card in self.cards):
            self.cards.remove(card)
        
    def setCardPositions(self):
        i = 0
        
        for card in self.cards:
            card.targetPosition = (self.position[0] + (i * 80), self.position[1])
            i += 1

        i = 0
        for card in self.match_cards:
            card.targetPosition = (self.position[0] + self.match_card_position[0] + ((i % Player.MATCH_CARDS_PER_ROW) * 32), self.position[1] + self.match_card_position[1] + (math.floor(i / Player.MATCH_CARDS_PER_ROW) * 64))
            i += 1
    
    
    def handleInput(self):
        print("Handle Input")
        
        
    def continuePrompt(self):
        self.gamemanager.continuePrompt()
        
    def doContinue(self):
        self.score.isKoi = True
        if (self.iStep == Player.STEP_HAND_MATCH_CONTINUE):
            self.score.hasNewScore = False
            self.iStep = Player.STEP_DRAW
        elif (self.iStep == Player.STEP_DRAW_MATCH_CONTINUE):
            self.score.hasNewScore = False
            self.iStep = Player.STEP_DONE
        
    def doStop(self):
        print("Ending the round")
    
    
    def nextRound(self):
        self.score = Score()
        self.isPlayerTurn = False
        self.iWaitDelay = 0
        self.score.checkScore(self.match_cards)
        self.iStep = Player.STEP_HAND_MATCH
        self.selectedCard = None




#let the game manager pass the mouse events to the player        
    def mousePressed(self, x, y):

        if (self.iStep == Player.STEP_HAND_MATCH):
            for card in self.cards:
                if (self.gamemanager.isCardAtPosition(card, x, y)):
                    self.selectCard(card, x, y)



        elif (self.iStep == Player.STEP_DRAW):
            if (len(self.gamemanager.cards) > 0 and self.gamemanager.isCardAtPosition(self.gamemanager.cards[len(self.gamemanager.cards) - 1], x, y)):
                self.drawCard()

        elif (self.iStep == Player.STEP_DRAW_MATCH):
            if (self.gamemanager.draw_card != None):
                card = self.gamemanager.draw_card
                if (self.gamemanager.isCardAtPosition(card, x, y)):
                    self.selectCard(card, x, y)
                    

    def mouseReleased(self, x, y):
        if (self.selectedCard != None):

            landedCard = None
            for card in self.gamemanager.table.cards:
                if (self.gamemanager.isCardAtPosition(card, x, y)):
                    landedCard = card
                
                
                
            if (self.iStep == Player.STEP_HAND_MATCH):
                if (landedCard != None):
                    successfulMatch = self.doMatch(self.selectedCard, landedCard)
                    if (successfulMatch):
                    
                        if (self.score.hasNewScore):
                            self.iStep = Player.STEP_HAND_MATCH_CONTINUE
                            self.continuePrompt()
                        else:
                            self.iStep = Player.STEP_DRAW
                            self.gamemanager.checkHints()
                        self.selectedCard = None
                    else:
                        self.selectedCard.targetPosition = self.selectedCard.previousPosition
                        self.selectedCard = None
                        self.gamemanager.checkHints()
                elif (self.gamemanager.table.isSelected):
                    self.doDiscard(self.selectedCard)
                    self.selectedCard = None
                    self.gamemanager.setCardPositions()
                    self.iStep = Player.STEP_DRAW
                    self.gamemanager.checkHints()
                else:
                    print("no card landed")
                    self.selectedCard.targetPosition = self.selectedCard.previousPosition
                    self.selectedCard = None
                    self.gamemanager.checkHints()

            elif (self.iStep == Player.STEP_DRAW_MATCH):
                if (landedCard != None):
                    successfulMatch = self.doMatch(self.selectedCard, landedCard)
                    if (successfulMatch):
                        self.selectedCard = None
                        if (self.score.hasNewScore):
                            self.iStep = Player.STEP_DRAW_MATCH_CONTINUE
                            self.continuePrompt()
                        else:
                            self.iStep = Player.STEP_DONE
                         
                    else:
                        self.selectedCard.targetPosition = self.selectedCard.previousPosition
                        self.selectedCard = None
                        self.gamemanager.checkHints()
                
                else:
                    if (self.gamemanager.table.isSelected):
                        self.doDiscard(self.selectedCard)
                        self.selectedCard = None
                        self.iStep = Player.STEP_DONE
                    else:
                        self.selectedCard.targetPosition = self.selectedCard.previousPosition
                        self.selectedCard = None
                        self.gamemanager.checkHints()


                
        
    def dragCard(self, x, y):
        if (not self.selectedCard == None):
            self.selectedCard.x = x - self.selectedOffset[0]
            self.selectedCard.y = y - self.selectedOffset[1]
            self.selectedCard.targetPosition = (x - self.selectedOffset[0], y - self.selectedOffset[1])

    def selectCard(self, card, xPress, yPress):
        self.selectedOffset = (xPress - card.x, yPress - card.y)
        self.selectedCard = card
        self.selectedCard.previousPosition = (self.selectedCard.x, self.selectedCard.y)
        self.gamemanager.checkHints()

