#2020 Levi D. Smith - levidsmith.com
import pygame
import math

from card import Card
from score import Score
from drawhelper import DrawHelper


class Player:
#    name = None
#    position = (0, 0)

    STEP_HAND_MATCH = 0
    STEP_DRAW = 1
    STEP_DRAW_MATCH = 2
    STEP_DONE = 3
    STEP_NAMES = ("Hand Match or Discard", "Draw", "Draw Match or Discard", "Done")
    
    MATCH_CARDS_PER_ROW = 8
    
    
    def __init__(self, init_gamemanager):
        name = "hello"
        self.cards = []
        self.match_cards = []
        self.score = Score()
        self.iRoundScores = []
        self.isPlayerTurn = False
        self.iWaitDelay = 0
        self.gamemanager = init_gamemanager
        self.isHidden = True
#        self.score_text = "None, 0 points"

#        self.score_offset = (960, -20)
#        self.card_types_offset = (1080, -20)

        self.score.checkScore(self.match_cards)
        self.isHuman = False
        self.iStep = Player.STEP_HAND_MATCH
        self.selectedCard = None
        self.waitContinueDecision = False
    
    def update(self):
        for card in self.cards:
            card.update()

        for card in self.match_cards:
            card.update()
              
        if (self.iWaitDelay > 0):
            self.iWaitDelay -= 1
            
        if (not self.waitContinueDecision):
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
            pygame.draw.rect(display, c_bkg, (self.position[0], self.position[1] + 128 + 4, 128, 32))
            
#        text = font.render(self.name, True, c, c_bkg)
#        display.blit(text, self.position)
        DrawHelper.drawTextShadow(self.name, self.position[0], self.position[1] + 128, (255, 255, 255), display, font[1])
#        if (self.isPlayerTurn):
        DrawHelper.drawTextShadow(str(self.iStep) + ": " + Player.STEP_NAMES[self.iStep], self.position[0], self.position[1] + 128 + 32, (0, 255, 255), display, font[1])
        DrawHelper.drawTextShadow(self.score.card_type_totals_text, self.position[0] + self.card_types_offset[0], self.position[1] + self.card_types_offset[1], (255, 255, 255), display, font[0])

        DrawHelper.drawTextShadow(self.score.score_text, self.position[0] + self.score_offset[0], self.position[1] + self.score_offset[1], (255, 255, 255), display, font[0])


        
        iMatchScore = 0
        strRoundsScore = ""
        for iScore in self.iRoundScores:
            iMatchScore += iScore
            strRoundsScore += str(iScore) + ","
            
        strRoundsScore += " Total = " + str(iMatchScore)

        DrawHelper.drawTextShadow(strRoundsScore, self.position[0] + 140, self.position[1] + 140, (255, 255, 255), display, font[0])
            
            
            
    def playTurn(self):
#        print(self.name + " playTurn " + " STEP " + str(self.iStep))
        
        if (not self.isHuman):
            
            if (self.iStep == Player.STEP_HAND_MATCH):
                self.checkHandMatch()
                self.iWaitDelay = 2 * 60
 #               self.setCardPositions()
            
            elif (self.iStep == Player.STEP_DRAW):
                self.drawCard()
                self.iWaitDelay = 2 * 60
#                self.setCardPositions()
            elif (self.iStep == Player.STEP_DRAW_MATCH):
                self.checkDrawMatch()
                self.iWaitDelay = 2 * 60

        
        if (self.iStep == Player.STEP_DONE):
            self.setCardPositions()
            self.gamemanager.setCardPositions()
            self.isPlayerTurn = False
        
        
    def checkHandMatch(self):
        print("checking match")
        match_card1 = None
        match_card2 = None

        for card_hand in self.cards:
            for card_table in self.gamemanager.table:
                if (card_hand.iMonth == card_table.iMonth):
                    match_card1 = card_hand
                    match_card2 = card_table
                    
        if ( (match_card1 != None) and (match_card2 != None)):
            successfulMatch = self.doMatch(match_card1, match_card2)
            if (successfulMatch):
#                self.cards.remove(match_card1)
                self.iStep = Player.STEP_DRAW

        else:
            if (len(self.cards) > 0):
                self.doDiscard(self.cards[0]) #Just discard the first card in the hand for now
            
            self.iStep = Player.STEP_DRAW
            

    def checkDrawMatch(self):
        print("checking match")
        match_card = None
        draw_card = self.gamemanager.draw_card

        for card_table in self.gamemanager.table:
            if (draw_card.iMonth == card_table.iMonth):
                match_card = card_table
                    
        if (match_card != None):
            self.doMatch(draw_card, match_card)
        else:
            self.doDiscard(draw_card)
            


#        self.setCardPositions()
        self.iStep = Player.STEP_DONE
                    

    def doMatch(self, match_card1, match_card2):
        successfulMatch = False
    
        print("Match - Month " + str(match_card1.iMonth) + " - IDs " + str(match_card1.id) + ", " + str(match_card2.id))
        if (match_card1.iMonth == match_card2.iMonth):
            self.match_cards.append(match_card1)
            match_card1.isHidden = False
            if (match_card1 in self.cards):
                self.cards.remove(match_card1)
#            self.cards.remove(match_card1)

            self.match_cards.append(match_card2)
            self.gamemanager.table.remove(match_card2)
            self.score.checkScore(self.match_cards)
            self.setCardPositions()
#            self.iStep = Player.STEP_DRAW
            successfulMatch = True
            self.gamemanager.sound_effects['card_drop'].play()
            
            if (self.score.hasNewScore):
                self.continuePrompt()
        
        return successfulMatch
        
    
    def drawCard(self):
        if (len(self.gamemanager.cards) > 0):
            draw_card = self.gamemanager.cards.pop()
            draw_card.isHidden = False
            draw_card.targetPosition = self.gamemanager.draw_card_position

            self.gamemanager.draw_card = draw_card
            self.iStep = Player.STEP_DRAW_MATCH
        else:
            print("No more cards")
        
        
            
#            match_card = None
#            for card_table in self.gamemanager.table:
#                if (draw_card.iMonth == card_table.iMonth):
#                    match_card = card_table
                
#            if (match_card != None):
#                print("Match - Month " + str(match_card.iMonth) + " - IDs " + str(draw_card.id) + ", " + str(match_card.id))
#                self.match_cards.append(match_card)
#                match_card.isHidden = False
#                self.gamemanager.table.remove(match_card)
                
#                draw_card.isHidden = False
#                self.match_cards.append(draw_card)
#                self.checkScore()
#            else:
#                draw_card.isHidden = False
#                self.gamemanager.table.append(draw_card)
                
#            self.setCardPositions()
        
#        self.iStep = Player.STEP_DONE
      
    def doDiscard(self, card):
        card.isHidden = False
        self.gamemanager.table.append(card)
        self.gamemanager.setCardPositions()
        if (card in self.cards):
            self.cards.remove(card)


        
        
        
        


        
    def setCardPositions(self):
        i = 0
        
        for card in self.cards:
#            card.targetPosition = (self.position[0] + 800 + (i * 32), + self.position[1])
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
        self.waitContinueDecision = True
        
    def doContinue(self):
        self.waitContinueDecision = False
        
    def doStop(self):
        self.waitContinueDecision = False
    
    
    def nextRound(self):
        self.score = Score()
        self.isPlayerTurn = False
        self.iWaitDelay = 0
        self.score.checkScore(self.match_cards)
        self.iStep = Player.STEP_HAND_MATCH
        self.selectedCard = None
        self.waitContinueDecision = False
