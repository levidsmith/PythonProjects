#2020 Levi D. Smith - levidsmith.com
import pygame
import random
import math
import os.path
from card import Card
from player import Player


SCREEN_SIZE = (1280, 720)
players = []
cards = []
table = []
background = []


def init():
    print("init")
    players.clear()
    cards.clear()
    table.clear()
    
    for i in range(12):
        for j in range(4):
            print(str(i) + ", " + str(j))
            card = Card((i * 4) + j,  i * 80, j * 150)
            card.iMonth = i
            strFile = 'images/hanafuda_' + str(i + 1) + '-' + str(j + 1) + '.jpg'
            if (os.path.isfile(strFile)):
                card.img = pygame.image.load(strFile)
                card.img = pygame.transform.scale(card.img, (card.w, card.h))
                
            imgBackground = pygame.image.load('images/background.jpg')
            background.append(imgBackground)
            
            
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

            if (i == 6):
                if (j == 2):
                    card.isRedRibbon = True
                if (j == 3):
                    card.isSpecial = True

            if (i == 7):
                if (j == 2):
                    card.isSpecial = True
                if (j == 3):
                    card.isLight = True

            if (i == 8):
                if (j == 2):
                    card.isBlueRibbon = True
                if (j == 3):
                    card.isSakeCup = True

            if (i == 9):
                if (j == 2):
                    card.isBlueRibbon = True
                if (j == 3):
                    card.isSpecial = True

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

                
            
            cards.append(card)
        
    random.shuffle(cards)

    #Deal to the table
    for i in range(8):
        draw_card = cards.pop()
        draw_card.x = 0
        draw_card.y = 300
        draw_card.targetPosition = (480 + ((i % 4) * 80), 200 + 160 * math.floor(i / 4))
        table.append(draw_card)

    #Create players
    p1 = Player()
    p1.name = "Player One"
    p1.position = (64, 32)
    for i in range(8):
        draw_card = cards.pop()
        draw_card.x = 0
        draw_card.y = p1.position[1]
        draw_card.targetPosition = (p1.position[0] + (i * 80), p1.position[1])
        p1.cards.append(draw_card)

    players.append(p1)
    



    p2 = Player()
    p2.name = "Player Two"
    p2.position = (640, 500)
    for i in range(8):
        draw_card = cards.pop()
        draw_card.x = 0
        draw_card.y = p2.position[1]
        draw_card.targetPosition = (p2.position[0] + (i * 80), p2.position[1])
        p2.cards.append(draw_card)

    players.append(p2)




def update():
#    print("update")
    print("update table")
    for card in table:
        card.update()
        
    for player in players:
        player.update()




def draw(display, font):

#    c = (182, 125, 56)
#    display.fill(c)
    display.blit(background[0], (0, 0))

#    c = (128, 128, 128)
#    for card in cards:
#        card.draw(display, font)
    for card in table:
        card.draw(display, font)
        
    for player in players:
        player.draw(display, font)

        
#    c = (255, 255, 255)
#    text = font.render('Hello', True, c)
#    display.blit(text, (50, 50))
    
    c = (255, 255, 255)
    text = font.render('2020 Levi D. Smith', True, c)
    display.blit(text, (1000, 680))
    
    

def main():

    pygame.init()
    display = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('Hanafuda Koi Koi')
    font = pygame.font.Font("Aerovias Brasil NF.ttf", 32)
    
    init()

    clock = pygame.time.Clock()
    
    keepLooping = True
    while (keepLooping):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                keepLooping = False
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_ESCAPE or event.key == pygame.K_q):
                    keepLooping = False
                if (event.key == pygame.K_d):
                    init()
    
        update()
        draw(display, font)
        pygame.display.update()
        clock.tick(60)
        
    
    pygame.quit()
    quit()
  



main()