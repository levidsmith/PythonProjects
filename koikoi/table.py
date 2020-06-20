#2020 Levi D. Smith - levidsmith.com
import pygame
import math

from card import Card

class Table:

    def __init__(self):
        self.position = (400, 200)
        self.size = (512, (Card.h * 2 + 32))
        self.cards = []
        self.card_slots = {}
        self.iNextCardSlot = 0
        self.isSelected = False
        self.surfaceBackground = None
        self.makeBackground()


    def makeBackground(self):
        self.surfaceBackground = pygame.Surface(self.size)
        self.surfaceBackground.set_alpha(64)
        self.surfaceBackground.fill((0, 0, 255))
        
    
    def restart(self):
        print("restart table")
        self.cards.clear()
        self.card_slots.clear()
        self.iNextCardSlot = 0
        

    def update(self):
        None

    def draw(self, display, font):
        self.surfaceBackground.set_alpha(32)

        if (self.isSelected):
            self.surfaceBackground.set_alpha(64)
        display.blit(self.surfaceBackground, (self.position[0], self.position[1], self.size[0], self.size[1]))



    def checkHovered(self, x, y):
        if (x > self.position[0] and x < self.position[0] + self.size[0] and y > self.position[1] and y < self.position[1] + self.size[1]):
            self.isSelected = True
            return True
        else:
            self.isSelected = False
            return False


    def addCard(self, card):
        self.cards.append(card)


        foundSlot = False
        iSlot = -1
#        for idx, cardSlot in enumerate(self.card_slots):
#            if (not (cardSlot in self.cards)):
#                iSlot = idx
#                foundSlot = True
                #self.card_slots[card] = idx

        i = 0
#        for i in range(0, self.iNextCardSlot):
        while (i < self.iNextCardSlot):
            if (not foundSlot):
                if (not (i in self.card_slots.values())):
                    print("foundSlot " + str(i))
                    iSlot = i
                    foundSlot = True
                    
            i += 1

        if (foundSlot):
            self.card_slots[card] = iSlot

        else:
            self.card_slots[card] = self.iNextCardSlot
            self.iNextCardSlot += 1

        self.setCardPositions()

    def removeCard(self, card):
        self.cards.remove(card)
        self.card_slots.pop(card, None)

    def setCardPositions(self):
#        i = 0
#        iCardsPerRow = math.ceil(len(self.cards) / 2)
#        iCardsPerRow = math.ceil(self.iNextCardSlot / 2)
        
        
        for card in self.cards:
            card.targetPosition = (self.position[0] + (math.floor(self.card_slots[card] / 2) * 80), self.position[1] + 160 * (self.card_slots[card] % 2))
#            card.targetPosition = (self.position[0] + ((self.card_slots[card] % iCardsPerRow) * 80), self.position[1] + 160 * math.floor(self.card_slots[card] / iCardsPerRow))

#            card.targetPosition = (self.position[0] + ((i % iCardsPerRow) * 80), self.position[1] + 160 * math.floor(i / iCardsPerRow))
#            i += 1

