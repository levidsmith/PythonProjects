#2020 Levi D. Smith - levidsmith.com
import pygame
import random
import math
import os.path
import sys
from card import Card
from player import Player
from gamemanager import GameManager
from globals import Globals


#SCREEN_SIZE = (1280, 720)
#players = []
#cards = []
#table = []
#background = []


#def init():
#    print("init")



#def update():
#    print("update")




#def draw(display, font):
#    print("draw")
    
    

def main():

    pygame.init()
    display = pygame.display.set_mode(Globals.SCREEN_SIZE)
    pygame.display.set_caption('Hanafuda Koi Koi')
    font = []
    font.append(pygame.font.Font("Aerovias Brasil NF.ttf", 20))
    font.append(pygame.font.Font("Aerovias Brasil NF.ttf", 32))

    gamemanager = GameManager()
    if ("-nomusic" in sys.argv):
        print("Disable Music")
        gamemanager.set_audio_volume(0)
    
#    init()

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
                    gamemanager.restart()
                if (event.key == pygame.K_m):
                    gamemanager.set_audio_volume(0)
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                gamemanager.mousePressed(pygame.mouse.get_pos())
            elif event.type == pygame.MOUSEBUTTONUP:
                gamemanager.mouseReleased(pygame.mouse.get_pos())
            elif event.type == pygame.MOUSEMOTION:
                gamemanager.mouseMoved(pygame.mouse.get_pos())
    
#        update()
#        draw(display, font)
        gamemanager.update()
        gamemanager.draw(display, font)
        pygame.display.update()
        clock.tick(60)
        
    
    pygame.quit()
    quit()
  



main()