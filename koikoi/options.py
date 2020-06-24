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
        
        print(os.environ['OS'])
        self.soundEffectsEnabled = True
        if (os.environ['OS'] != "Windows_NT"):
            self.soundEffectsEnabled = False
