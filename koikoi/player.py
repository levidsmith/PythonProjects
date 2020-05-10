#2020 Levi D. Smith - levidsmith.com
import pygame
import math

from card import Card
from drawhelper import DrawHelper


class Player:
#    name = None
#    position = (0, 0)

    STEP_HAND_MATCH = 0
    STEP_DRAW = 1
    STEP_DRAW_MATCH = 2
    STEP_DONE = 3
    STEP_NAMES = ("Hand Match", "Draw", "Draw Match", "Done")
    
    def __init__(self, init_gamemanager):
        name = "hello"
        self.cards = []
        self.match_cards = []
        self.isPlayerTurn = False
        self.iWaitDelay = 0
        self.gamemanager = init_gamemanager
        self.isHidden = True
#        self.score_text = "None, 0 points"
        self.checkScore()
        self.isHuman = False
        self.iStep = Player.STEP_HAND_MATCH
        
        self.selectedCard = None
    
    def update(self):
#        print("update player " + self.name + " card count: " + str(len(self.cards)) )
        
        for card in self.cards:
#            print("update player card " + str(card.id))
            card.update()

        for card in self.match_cards:
#            print("update player card " + str(card.id))
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
            pygame.draw.rect(display, c_bkg, (self.position[0], self.position[1] + 128 + 4, 128, 32))
            
#        text = font.render(self.name, True, c, c_bkg)
#        display.blit(text, self.position)
        DrawHelper.drawTextShadow(self.name, self.position[0], self.position[1] + 128, (255, 255, 255), display, font[1])
#        if (self.isPlayerTurn):
        DrawHelper.drawTextShadow(str(self.iStep) + ": " + Player.STEP_NAMES[self.iStep], self.position[0], self.position[1] + 128 + 32, (0, 255, 255), display, font[1])
        DrawHelper.drawTextShadow(self.score_text, self.position[0] + 1080, self.position[1] - 20, (255, 255, 255), display, font[0])


            
            
            
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
            self.checkScore()
            self.setCardPositions()
#            self.iStep = Player.STEP_DRAW
            successfulMatch = True
            self.gamemanager.sound_effects['card_drop'].play()
        
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


        
        
        
        
    def checkScore(self):
        iLights = 0
        iRainMan = 0
        iPoetryRibbons = 0
        iRedRibbons = 0
        iBlueRibbons = 0
        iRibbons = 0
        iSpecials = 0
        iSakeCup = 0
        iBoarDeerButterfly = 0
        iNormals = 0
        
        for card in self.match_cards:
            if (card.isLight):
                iLights += 1

            if (card.isRainMan):
                iRainMan += 1
            
            if (card.isRedRibbon):
                iRedRibbons += 1

            if (card.isBlueRibbon):
                iBlueRibbons += 1

            if (card.isPoetryRibbon):
                iPoetryRibbons += 1

            if (card.isSakeCup):
                iSakeCup += 1
                iSpecials += 1

            if (card.isSpecial):
                iSpecials += 1
            
            if (card.isBoarDeerButterfly):
                iBoarDeerButterfly += 1

            if (card.getIsNormal()):
                iNormals += 1
                
                
            iRibbons = iRedRibbons + iBlueRibbons
            
            
        self.score_text = ""
        if (iLights > 0):
            self.score_text += "Lights " + str(iLights) + "\n"

        if (iRainMan > 0):
            self.score_text += "Rain Man " + str(iRainMan) + "\n"

        if (iSakeCup > 0):
            self.score_text += "Sake Cup " + str(iSakeCup) + "\n"

        if (iRibbons > 0): 
            self.score_text += "Ribbons " + str(iRibbons) + "\n"

        if (iRedRibbons > 0): 
            self.score_text += "Red Ribbons " + str(iRedRibbons) + "\n"

        if (iBlueRibbons > 0): 
            self.score_text += "Blue Ribbons " + str(iBlueRibbons) + "\n"

        if (iPoetryRibbons > 0): 
            self.score_text += "Poetry Ribbons " + str(iPoetryRibbons) + "\n"

        if (iSpecials > 0): 
            self.score_text += "Specials " + str(iSpecials) + "\n"

        if (iBoarDeerButterfly > 0): 
            self.score_text += "B,D,BF " + str(iBoarDeerButterfly) + "\n"


        if (iNormals > 0): 
            self.score_text += "Normals " + str(iNormals) + "\n"
#            + "\nRed Ribbons " + str(iRedRibbons)
 #           + "\nNormals " + str(iNormals)


        
    def setCardPositions(self):
        i = 0
        
        for card in self.cards:
#            card.targetPosition = (self.position[0] + 800 + (i * 32), + self.position[1])
            card.targetPosition = (self.position[0] + (i * 80), self.position[1])
            i += 1

        i = 0
        for card in self.match_cards:
            card.targetPosition = (self.position[0] + 700 + ((i % 10) * 32), self.position[1] + (math.floor(i / 10) * 64))
            i += 1
    
    
    def handleInput(self):
        print("Handle Input")