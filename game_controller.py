from data_initializer import DataInitializer
#from . duo import Duo
#from . player import Player
from models import Game
from models import Goal
from qt_core import *
import datetime

class GameController(QObject):
    timeUpdate = pyqtSignal(str)
    scoreUpdate = pyqtSignal()
 

    def __init__(self,dti:DataInitializer):
        super().__init__()
        self.dti = dti
        self.game = Game()
        self.running = False
        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
        self.timer_fast = QTimer()
        self.timer_fast.timeout.connect(self.updateDurationPrecise)
        self.timer_fast.start(1000)
        self.finishedWidget = QWidget()
        self.finished = QPushButton(self.finishedWidget)
        self.validSelection = QPushButton(self.finishedWidget)
        self.invalidSelection = QPushButton(self.finishedWidget)
        self.initPlayers()
#        self.scoreUpdate.connect(self.checkGameIsFinished)

    # def resetStates(self):
    #     self.running = False
    #     self.game.__init__()

    # GOAL ACTIONS
    # ///////////////////////////////////////////////////////////////
    def addGoal(self,player):
        goal = Goal(player,self.game.duration)
        self.game.goals.append(goal)
        self.game.scores[self.game.players.index(player)] += 1
        self.checkGameIsFinished()
        self.scoreUpdate.emit()

    def deleteLastGoal(self):
        print("deleting last goal")
        if len(self.game.goals)>0:
            self.game.scores[self.game.players.index(self.game.goals[-1].player)] -= 1
            self.game.goals.pop(-1)
        self.scoreUpdate.emit()


    def initPlayers(self):
        self.game.players = [self.dti.players[0]]*4
        self.game.duos = [self.find_duo(self.game.players[0],self.game.players[1])]*2            
    
    def togglePlayer(self,position):
        curPlayerIndex = self.dti.players.index(self.game.players[position])
        if curPlayerIndex == self.dti.numberOfPlayers-1:
            nextPlayerindex = 0
        else:
            nextPlayerindex = curPlayerIndex + 1
        self.set_player(self.dti.players[nextPlayerindex],position)



    def set_player(self,player,pos):
        self.game.players[pos] = player
        if pos < 2:
            self.game.duos[0] = self.find_duo(self.game.players[0],self.game.players[1])
        else:
            self.game.duos[1] = self.find_duo(self.game.players[2],self.game.players[3])

    def find_duo(self,def_player,off_player):
        for duo in self.dti.duos:
            if duo.def_player == def_player and duo.off_player == off_player:
                return duo


    
    def checkGameIsFinished(self):
        if (self.game.scoreRed >= 11 or self.game.scoreGre >= 11) and abs(self.game.scoreRed - self.game.scoreGre) > 1:
            self.finished.clicked.emit()

    def showTime(self):
        if self.running:
            self.game.duration += 1

        self.timeUpdate.emit(str(datetime.timedelta(seconds=self.game.duration)))

    def updateDurationPrecise(self):
        if self.running:
            self.game.duration_precise += 1.0

    def pause(self):
        self.running = False

    def start(self):
        self.running = True

    def reset(self):
        self.game.duration = 0
        self.game.duration_precise = 0.00
    def endGame(self):
        self.pause()
        self.reset()
        #self.game = Game()
