from qt_core import *
from models import *

class PlayerSelection(QObject):
    players = []
    numberOfPlayers = 0
    gamePlayers = []
    duos = [Duo]


    def __init__(self,players: list[Player]):
        super().__init__()
        self.players = players
        self.players.sort(key=lambda s : s.name)
        self.numberOfPlayers = len(self.players)
        self.initPlayers()

    def initPlayers(self):
        self.gamePlayers = [self.players[0]]*4            
    
    def togglePlayer(self,playerNumber):
        curPlayerIndex = self.players.index(self.gamePlayers[playerNumber-1])
        if curPlayerIndex == self.numberOfPlayers-1:
            nextPlayerindex = 0
        else:
            nextPlayerindex = curPlayerIndex + 1
        self.gamePlayers[playerNumber-1] = self.players[nextPlayerindex]
