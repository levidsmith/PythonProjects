#2020 Levi D. Smith - levidsmith.com
class Score:

#    hasSankou = False
#    hasShikou = False
#    hasAmeShikou = False
#    hasGokou = False
#    hasInoshikachou = False
#    hasTane = False
#    hasAkaTan = False
#    hasAoTan = False
#    hasAkaAoNoChoufuku = False
#    hasTanzaku = False
#    hasTsukimiZake = False
#    hasHanamiZake = False
#    hasKasu = False
#    iKasuCount = 0
 
    def __init__(self):
        self.scoreDict = { }
        self.score_text = "Scores"
        self.card_type_totals_text = ""
        self.hasNewScore = False
    
    
    def checkScore(self, cards):
        iLights = 0
        iRainMan = 0
        iSakuraCurtain = 0
        iMoon = 0
        iPoetryRibbons = 0
        iRedRibbons = 0
        iBlueRibbons = 0
        iRibbons = 0
        iSpecials = 0
        iSakeCup = 0
        iBoarDeerButterfly = 0
        iNormals = 0

           
        
        for card in cards:
            if (card.isLight):
                iLights += 1

            if (card.isRainMan):
                iRainMan += 1
            
            if (card.isSakuraCurtain):
                iSakuraCurtain += 1
                
            if (card.isMoon):
                iMoon += 1
            
            if (card.isRedRibbon):
                iRedRibbons += 1

            if (card.isBlueRibbon):
                iBlueRibbons += 1

            if (card.isPoetryRibbon):
                iPoetryRibbons += 1

            if (card.isSakeCup):
                iSakeCup += 1
                iSpecials += 1

            if (card.isSpecial):
                iSpecials += 1
            
            if (card.isBoarDeerButterfly):
                iBoarDeerButterfly += 1

            if (card.getIsNormal()):
                iNormals += 1
                
                
            iRibbons = iRedRibbons + iBlueRibbons
            
            
        self.card_type_totals_text = "Card Totals\n"
        if (iLights > 0):
            self.card_type_totals_text += "Lights " + str(iLights) + "\n"

        if (iRainMan > 0):
            self.card_type_totals_text += "Rain Man " + str(iRainMan) + "\n"

        if (iSakeCup > 0):
            self.card_type_totals_text += "Sake Cup " + str(iSakeCup) + "\n"

        if (iRibbons > 0): 
            self.card_type_totals_text += "Ribbons " + str(iRibbons) + "\n"

        if (iRedRibbons > 0): 
            self.card_type_totals_text += "Red Ribbons " + str(iRedRibbons) + "\n"

        if (iBlueRibbons > 0): 
            self.card_type_totals_text += "Blue Ribbons " + str(iBlueRibbons) + "\n"

        if (iPoetryRibbons > 0): 
            self.card_type_totals_text += "Poetry Ribbons " + str(iPoetryRibbons) + "\n"

        if (iSpecials > 0): 
            self.card_type_totals_text += "Specials " + str(iSpecials) + "\n"

        if (iBoarDeerButterfly > 0): 
            self.card_type_totals_text += "B,D,BF " + str(iBoarDeerButterfly) + "\n"


        if (iNormals > 0): 
            self.card_type_totals_text += "Normals " + str(iNormals) + "\n"
            
        
        self.hasNewScore = False
        
        #Check Yaku matches
        strKey = 'kasu'
        if (not strKey in self.scoreDict):
            if (iNormals >= 10):
                iPoints = 1 + (iNormals - 10)
                self.scoreDict[strKey] = iPoints
                self.hasNewScore = True

        else:
            iPoints = 1 + (iNormals - 10)
            if (self.scoreDict[strKey] < iPoints):
                self.scoreDict[strKey] = iPoints
                self.hasNewScore = True
                
        #Hanamizake matches
        strKey = 'hanamizake'
        if (not strKey in self.scoreDict):
            if (iSakuraCurtain >= 1 and iSakeCup >= 1):
                self.scoreDict[strKey] = 5
                self.hasNewScore = True

        #Tsukimizake matches
        strKey = 'tsukimizake'
        if (not strKey in self.scoreDict):
            if (iMoon >= 1 and iSakeCup >= 1):
                self.scoreDict[strKey] = 5
                self.hasNewScore = True
                
        #Tanzaku matches
        strKey = 'tanzaku'
        if (not strKey in self.scoreDict):
            print("tanzaku does not exist - Ribbons: " + str(iRibbons))
            if (iRibbons >= 5):
                iPoints = 1 + (iRibbons - 5)
                self.scoreDict[strKey] = iPoints
                self.hasNewScore = True
        else:
            print("tanzaku exists - Ribbons: " + str(iRibbons))
            iPoints = 1 + (iRibbons - 5)
            if (self.scoreDict[strKey] < iPoints):
                self.scoreDict[strKey] = iPoints
                self.hasNewScore = True
                
        #Akatan, Aotan no Choufuku
        strKey = 'akaaonochoufuku'
        if (not strKey in self.scoreDict):
            if (iBlueRibbons >= 3 and iPoetryRibbons >= 3):
                self.scoreDict[strKey] = 10
                self.hasNewScore = True
                
        #Aotan matches
        strKey = 'aotan'
        if (not strKey in self.scoreDict):
            if (iBlueRibbons >= 3):
                self.scoreDict[strKey] = 5
                self.hasNewScore = True
        
        #Akatan matches
        strKey = 'akatan'
        if (not strKey in self.scoreDict):
            if (iPoetryRibbons >= 3):
                self.scoreDict[strKey] = 5
                self.hasNewScore = True
                
        #Tane
        strKey = 'tane'
        if (not strKey in self.scoreDict):
            if (iSpecials >= 5):
                iPoints = 1 + (iSpecials - 5)
                self.scoreDict[strKey] = iPoints
                self.hasNewScore = True
        else:
            iPoints = 1 + (iSpecials - 5)
            if (self.scoreDict[strKey] < iPoints):
                self.scoreDict[strKey] = iPoints
                self.hasNewScore = True
            
        #Inoshikachou
        strKey = 'inoshikachou'
        if (not strKey in self.scoreDict):
            if (iBoarDeerButterfly >= 3):
                self.scoreDict[strKey] = 5
                self.hasNewScore = True
                
        #Sankou
        strKey = 'sankou'
        if (not strKey in self.scoreDict and not 'shikou' in self.scoreDict and not 'ameshikou' in self.scoreDict and not 'gokou' in self.scoreDict):
            if (iLights == 3):
                self.scoreDict[strKey] = 6
                self.hasNewScore = True
                
        #Shikou
        strKey = 'shikou'
        if (not strKey in self.scoreDict and not 'ameshikou' in self.scoreDict and not 'gokou' in self.scoreDict):
            if (iLights == 4):
                self.scoreDict[strKey] = 8
                self.hasNewScore = True
                
                strKey = 'sankou'
                if (strKey in self.scoreDict):
                    del self.scoreDict[strKey]
                    
        #Ame Shikou
        strKey = 'ameshikou'
        if (not strKey in self.scoreDict and not 'gokou' in self.scoreDict):
            if (iRainMan == 1 and iLights == 3):
                self.scoreDict[strKey] = 7
                self.hasNewScore = True

                strKey = 'sankou'
                if (strKey in self.scoreDict):
                    del self.scoreDict[strKey]

                strKey = 'shikou'
                if (strKey in self.scoreDict):
                    del self.scoreDict[strKey]

        #Gokou
        strKey = 'gokou'
        if (not strKey in self.scoreDict):
            if (iRainMan == 1 and iLights == 4):
                self.scoreDict[strKey] = 15
                self.hasNewScore = True

                strKey = 'sankou'
                if (strKey in self.scoreDict):
                    del self.scoreDict[strKey]

                strKey = 'shikou'
                if (strKey in self.scoreDict):
                    del self.scoreDict[strKey]
                
                strKey = 'ameshikou'
                if (strKey in self.scoreDict):
                    del self.scoreDict[strKey]


        #Build total score and score text
        self.iTotalPoints = 0
        self.score_text = "Score\n"
        for key in self.scoreDict:
            self.score_text += key + " " + str(self.scoreDict[key]) + "\n"
            self.iTotalPoints += self.scoreDict[key]
        
        self.score_text += "Points " + str(self.iTotalPoints)
                
            
            
        
    
    