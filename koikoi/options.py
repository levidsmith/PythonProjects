#2020 Levi D. Smith - levidsmith.com
import pygame
import os



class Options:

    def __init__(self):
        self.strName = ""
        self.iTotalRounds = 3
        self.showHints = True
        self.showMonth = True
        self.showCardType = True
        self.musicEnabled = True
        
        strOS = ""
        if ('OS' in os.environ):
            strOS = os.environ['OS']
        print("OS is " + strOS)
        
        self.soundEffectsEnabled = True
        if (strOS != "Windows_NT"):
            self.soundEffectsEnabled = False
