from . player import Player
from . duo import Duo
from .goal import Goal 
from PyQt5.QtCore import QDateTime, QObject

class Game(QObject):
    id = int
    duration = int
    #duration_precise = float
    players = [Player]
    duos = [Duo]
    goals = [Goal]
    scores = [int]
    startDateTime = QDateTime
    deltaElo = []
    def __init__(self):
        super().__init__()
        self.id = 0
        self.duration = 0
        self.duration_precise = 0.00
        self.players = []*4
        self.duos = []*2
        self.goals = []
        self.scores = [0]*4
        self.deltaElo = [0]*4
        self.startDateTime = QDateTime.currentDateTimeUtc()

    @property
    def scoreRed(self):
        return self.scores[0] + self.scores[1]    

    @property
    def scoreGre(self):
        return self.scores[2] + self.scores[3]

