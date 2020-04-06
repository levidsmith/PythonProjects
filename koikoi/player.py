#2020 Levi D. Smith - levidsmith.com
import pygame
import math

from card import Card
from drawhelper import DrawHelper


class Player:
#    name = None
#    position = (0, 0)
    
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
        DrawHelper.drawTextShadow(self.score_text, self.position[0] + 1080, self.position[1] - 20, (255, 255, 255), display, font[0])


            
            
            
    def playTurn(self):
        print(self.name + " playTurn")
        self.checkMatch()
        self.drawCard()
        self.setCardPositions()

        self.isPlayerTurn = False
        
        
    def checkMatch(self):
        print("checking match")
        match_card1 = None
        match_card2 = None

        for card_hand in self.cards:
            for card_table in self.gamemanager.table:
                if (card_hand.iMonth == card_table.iMonth):
                    match_card1 = card_hand
                    match_card2 = card_table
                    
        if ( (match_card1 != None) and (match_card2 != None)):
            print("Match - Month " + str(match_card1.iMonth) + " - IDs " + str(match_card1.id) + ", " + str(match_card2.id))
            self.match_cards.append(match_card1)
            match_card1.isHidden = False
            self.cards.remove(match_card1)

            self.match_cards.append(match_card2)
            self.gamemanager.table.remove(match_card2)
            self.checkScore()
                    

    def drawCard(self):
        if (len(self.gamemanager.cards) > 0):
            draw_card = self.gamemanager.cards.pop()
#            draw_card.isHidden = self.isHidden
        
            match_card = None
            for card_table in self.gamemanager.table:
                if (draw_card.iMonth == card_table.iMonth):
                    match_card = card_table
                
            if (match_card != None):
                print("Match - Month " + str(match_card.iMonth) + " - IDs " + str(draw_card.id) + ", " + str(match_card.id))
                self.match_cards.append(match_card)
                match_card.isHidden = False
                self.gamemanager.table.remove(match_card)
                
                draw_card.isHidden = False
                self.match_cards.append(draw_card)
                self.checkScore()
            else:
                draw_card.isHidden = False
                self.gamemanager.table.append(draw_card)
                
        
        
        
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
    