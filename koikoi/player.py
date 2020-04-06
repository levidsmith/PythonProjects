#2020 Levi D. Smith - levidsmith.com
from card import Card


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
    
    def update(self):
#        print("update player " + self.name + " card count: " + str(len(self.cards)) )
        
        for card in self.cards:
#            print("update player card " + str(card.id))
            card.update()

              
        if (self.iWaitDelay > 0):
            self.iWaitDelay -= 1
            
        if (self.isPlayerTurn and self.iWaitDelay <= 0):
            self.playTurn()
    
    def draw(self, display, font):
        for card in self.cards:
            card.draw(display, font)

        c = (255, 255, 255)
        c_bkg = (0, 0, 0)
        if (self.isPlayerTurn):
            c = (0, 0, 0)
            c_bkg = (255, 255, 255)
            
        text = font.render(self.name, True, c, c_bkg)
        display.blit(text, self.position)

            
            
            
    def playTurn(self):
        print(self.name + " playTurn")
        self.checkMatch()
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
            self.cards.remove(match_card1)

            self.match_cards.append(match_card2)
            self.gamemanager.table.remove(match_card2)
                    
        
        
    def setCardPositions(self):
        i = 0
        for card in self.match_cards:
            card.targetPosition = (self.position[0] + 800 + (i * Card.w), + self.position[1])
            i += 1
    