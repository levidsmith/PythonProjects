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
from screen_gamecomplete import ScreenGameComplete
from screen_options import ScreenOptions
from options import Options
from leaderboardmanager import LeaderboardManager
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
        font = {}
        font['small'] = pygame.font.Font("fonts/Seven Swordsmen BB.ttf", 20)
        font['normal'] = pygame.font.Font("fonts/Seven Swordsmen BB.ttf", 32)
        font['title'] = pygame.font.Font("fonts/Seven Swordsmen BB.ttf", 128)
#        font.append(pygame.font.Font("Aerovias Brasil NF.ttf", 20))
#        font.append(pygame.font.Font("Aerovias Brasil NF.ttf", 32))


        self.leaderboardmanager = LeaderboardManager()
#        self.leaderboardmanager.getTopScores()
#        self.leaderboardmanager.submitScore("hello", 42)
#        self.leaderboardmanager.submitScore("world", 84)


        
        #make array of screens
        self.screens = {}

        screenTitle = ScreenTitle(self)
        self.screens["title"] = screenTitle

        self.options = Options()
        screenOptions = ScreenOptions(self)
        self.screens["options"] = screenOptions

        gamemanager = GameManager(self)
        self.screens["gamemanager"] = gamemanager

        screenGameComplete = ScreenGameComplete(self)
        self.screens["gamecomplete"] = screenGameComplete

        self.currentScreen = self.screens["title"]
#        self.currentScreen = self.screens["gamecomplete"]


        if ("-nomusic" in sys.argv):
            print("Disable Music")
            gamemanager.set_audio_volume(0)


        clock = pygame.time.Clock()
    
        self.keepLooping = True
        while (self.keepLooping):
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    self.keepLooping = False
                elif event.type == pygame.KEYDOWN:
#                    if (event.key == pygame.K_ESCAPE or event.key == pygame.K_q):
#                        self.keepLooping = False
                    if (event.key >= pygame.K_a and event.key <= pygame.K_z):
                        self.currentScreen.keyInputChar(chr(event.key))
                    if (event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE):
                        self.currentScreen.keyInputDelete()

#                    if (event.key == pygame.K_m):
#                        gamemanager.set_audio_volume(0)
                    
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.currentScreen.mousePressed(pygame.mouse.get_pos())
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.currentScreen.mouseReleased(pygame.mouse.get_pos())
                elif event.type == pygame.MOUSEMOTION:
                    self.currentScreen.mouseMoved(pygame.mouse.get_pos())
    

            self.currentScreen.update()
            self.currentScreen.draw(display, font)
            pygame.display.update()
            clock.tick(60)
        
    
        pygame.quit()
        quit()
  



application = Application()