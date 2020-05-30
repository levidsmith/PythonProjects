#2020 Levi D. Smith - levidsmith.com
import pygame
import random
import math
import os.path
import sys
from card import Card
from player import Player
from gamemanager import GameManager
from screen_title import ScreenTitle
from screen_gameover import ScreenGameOver
from globals import Globals

class Application:
    def __init__(self):

        self.main()

    def loadScreen(self, strScreen):
        self.currentScreen = self.screens[strScreen]
        self.currentScreen.restart()

    def doQuit(self):
        self.keepLooping = False


    def main(self):

        pygame.init()
        display = pygame.display.set_mode(Globals.SCREEN_SIZE)
        pygame.display.set_caption('Hanafuda Koi Koi')
        font = []
        font.append(pygame.font.Font("Aerovias Brasil NF.ttf", 20))
        font.append(pygame.font.Font("Aerovias Brasil NF.ttf", 32))



        if ("-nomusic" in sys.argv):
            print("Disable Music")
            gamemanager.set_audio_volume(0)

    

        #make array of screens
        self.screens = {}

        screenTitle = ScreenTitle(self)
        self.screens["title"] = screenTitle

        gamemanager = GameManager(self)
        self.screens["gamemanager"] = gamemanager

        screenGameOver = ScreenGameOver(self)
        self.screens["gameover"] = screenGameOver

        self.currentScreen = self.screens["title"]


        clock = pygame.time.Clock()
    
        self.keepLooping = True
        while (self.keepLooping):
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    self.keepLooping = False
                elif event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_ESCAPE or event.key == pygame.K_q):
                        self.keepLooping = False
#                    if (event.key == pygame.K_d):
#                        gamemanager.restart()
                    if (event.key == pygame.K_m):
                        gamemanager.set_audio_volume(0)
                    
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    #gamemanager.mousePressed(pygame.mouse.get_pos())
                    self.currentScreen.mousePressed(pygame.mouse.get_pos())
                elif event.type == pygame.MOUSEBUTTONUP:
                    #gamemanager.mouseReleased(pygame.mouse.get_pos())
                    self.currentScreen.mouseReleased(pygame.mouse.get_pos())
                elif event.type == pygame.MOUSEMOTION:
                    #gamemanager.mouseMoved(pygame.mouse.get_pos())
                    self.currentScreen.mouseMoved(pygame.mouse.get_pos())
    

            self.currentScreen.update()
            self.currentScreen.draw(display, font)
            pygame.display.update()
            clock.tick(60)
        
    
        pygame.quit()
        quit()
  



#main()
application = Application()