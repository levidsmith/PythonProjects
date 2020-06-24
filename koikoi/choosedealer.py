#2020 Levi D. Smith - levidsmith.com
import pygame


class ChooseDealer():
    def __init__(self, init_application):
        self.application = init_application
        self.cards = []
        self.restart()

    def restart(self):
        self.cards.clear()
        self.chooseCard = True
        self.chosen_card = None
        self.iDealerPlayer = -1


    def update(self):
        if (len(self.cards) < 2):
            self.application.gamemanager.createDeck()

        while (len(self.cards) < 2):
            card = self.application.gamemanager.cards.pop()
            card.targetPosition = (400 + (len(self.cards) * 200), 300)
            self.cards.append(card)


        for card in self.cards:
            card.update()

        if (self.chooseCard):
            if (not (self.chosen_card == None)):
                self.chooseCard = False

                for card in self.cards:
                    card.isHidden = False
            

        self.application.gamemanager.updateHighlight()

    def getDealerIndex(self):
        iDealer = -1
        if (self.chosen_card != None):
            iChosenMonth = self.chosen_card.iMonth
            iChosenCard = self.cards.index(self.chosen_card)
            cardOther = self.cards[(iChosenCard + 1) % 2]
            iOtherMonth = cardOther.iMonth

            if (iChosenMonth > iOtherMonth):
                iDealer = 1
            else:
                iDealer = 0

        return iDealer

    
            


