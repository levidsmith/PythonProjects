#2020 Levi D. Smith - levidsmith.com

class Player:
    name = None
    position = (0, 0)
    
    def __init__(self):
        name = "hello"
        self.cards = []
    
    def update(self):
#        print("update player " + self.name + " card count: " + str(len(self.cards)) )
        
        for card in self.cards:
#            print("update player card " + str(card.id))
            card.update()
    
    def draw(self, display, font):
        for card in self.cards:
            card.draw(display, font)
    