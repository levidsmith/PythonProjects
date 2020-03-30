#2020 Levi D. Smith - levidsmith.com
import pygame
from card import Card
from player import Player

SCREEN_SIZE = (1280, 720)
players = []
cards = []

def init():
#    print("init")
    
    for i in range(12):
        for j in range(4):
            print(str(i) + ", " + str(j))
            cards.append(Card(i, (i * 12) + j, j * 72, i * 136))
#            card = Card(i, j)


def update():
    print("update")


def draw(display):
    c = (0, 0, 0)
    display.fill(c)

    c = (128, 128, 128)
    for card in cards:
        card.draw(display)

def main():

    pygame.init()
    display = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('Hanafuda Koi Koi')
    
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
    
        update()
        draw(display)
        pygame.display.update()
        clock.tick(60)
        
    
    pygame.quit()
    quit()
  



main()