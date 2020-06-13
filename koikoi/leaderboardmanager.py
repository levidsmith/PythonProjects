#2020 Levi D. Smith - levidsmith.com
import urllib.request
import hashlib

class LeaderboardManager:

    def __init__(self):
        self.iGameID = 6751
        f = open("leaderboard.key", "r")
        self.strKey = f.readline()
        f.close()

    def submitScore(self, strName, iScore):
        strToHash = strName + str(iScore) + str(self.iGameID) + self.strKey
        print("strToHash: " + strToHash)
        hash = hashlib.md5(strToHash.encode())
        print("MD5 sum of has string " + hash.hexdigest())
        urllib.request.urlopen("https://levidsmith.com/scores/AddScore.php?name=" + strName + "&game=" + str(self.iGameID) + "&score=" + str(iScore) + "&hash=" + hash.hexdigest())
        
    def getTopScores(self):
        print(urllib.request.urlopen("https://levidsmith.com/scores/TopScores.php?game=" + str(self.iGameID)).read())