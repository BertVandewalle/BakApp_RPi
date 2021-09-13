import time
from logging import exception
import sys
sys.path.append('../BakApp_RPi')
from models.player import Player

from gui.core.json_themes import Themes
from gui.widgets.circular_picture import ScaledCircularPicture
from gui.core.json_settings import Settings
from data_controller import DataController
from data_initializer import DataInitializer
from game_controller import GameController
from qt_core import *


class TimeLineGoal(QWidget):
    def __init__(self,time_seconds:float,player:Player,team:str,size=40,parent=None):
        super().__init__()
        if parent != None:
            self.setParent(parent)
        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items
        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items
        self.red = self.themes['app_color']['red']
        self.green = self.themes['app_color']['green']
        
        self.player = player
        self.team = team
        self.time_seconds = time_seconds
        self.time_minute = int(time_seconds/60+1)
        self._layout = QHBoxLayout(self)
        self.label_time = QLabel(text=f"{self.time_minute}'")
        if self.team == "red":
            self.widget_pic = ScaledCircularPicture(self.player.pixMap,self.red,size=size)
            self.label_time.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
            self._layout.addWidget(self.label_time)
            self._layout.addWidget(self.widget_pic,0,Qt.AlignRight|Qt.AlignVCenter)
        else:
            self.widget_pic = ScaledCircularPicture(self.player.pixMap,self.green,size=size)
            self.label_time.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)
            self._layout.addWidget(self.widget_pic,0,Qt.AlignLeft|Qt.AlignVCenter)
            self._layout.addWidget(self.label_time)
#        self.widget_pic.setFixedSize(size,size)

class TimeLine(QWidget):
    goals = [TimeLineGoal]
    def __init__(self,gc:GameController):
        super().__init__()
        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items
        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        self.red = self.themes['app_color']['red']
        self.green = self.themes['app_color']['green']

        self.gc = gc
        #self.start()

        self.goals = []
        self._layout = QVBoxLayout(self)
        self.setFixedSize(150,600)
        #self._layout.addWidget(self.redDefPlayer)
        #self.redDefPlayer.move(self.width()//2-self.redDefPlayer.width()-10,self.height()-40-self.redDefPlayer.height())
        

    def paintEvent(self,event):
        p = QPainter()
        p.begin(self)
        p.setRenderHint(QPainter.Antialiasing)

        pen = QPen()
        pen.setWidth(10)
        pen.setColor(QColor(Qt.white))
        pen.setCapStyle(Qt.RoundCap)

        p.setPen(pen)
        p.drawLine(self.width()//2,10,self.width()//2,self.height()-10)
        #self.redDefPlayer.move(self.width()//2-self.redDefPlayer.width()-10,self.height()-40-self.redDefPlayer.height())
        
        #self.redDefPlayer2.move(self.width()//2-self.redDefPlayer.width()-10,self.height()-50-self.redDefPlayer.height())
        #print(self.goals)
        # for goal in self.goals:
        #     try:
        #         self.setPosition(goal,self.gc.game.duration_precise)
        #     except Exception as e: print(e)
        p.end()

    def moveGoalWidgets(self):
        for goal in self.goals:
            try:
                self.setPosition(goal,self.gc.game.duration_precise)
            except Exception as e: print(e)

        # if len(self.goals)>0:
        #     try:
        #         self.goals[0].move(self.width()//2-self.goals[0].width(),self.height()-10)
        #     except Exception as e: print(f"{e} len(goals) = {len(self.goals)}")
        #self.repaint()

    def calculateHeight(self,goal:TimeLineGoal,time_current):
        if time_current > 0:
            return round(self.height()-goal.height()+goal/time_current*(goal.height()-self.height()))
        else: pass
    
    def setPosition(self,goal:TimeLineGoal,time_current:float):
        if time_current > 0:
            y = round(self.height()-goal.height()+float(goal.time_seconds)/time_current*(goal.height()-self.height()))
            if goal.team == "red": x = round(self.width()/2.0-goal.width())
            else: x = round(self.width()/2.0)
            goal.move(x,y)
            #print(f"move to ({x},{y})")
        else: pass

    def addGoal(self,player:Player,team,time:float):
        self.hide()
        goal = TimeLineGoal(time,player,team,parent=self)
        #goal = QLabel(text="Goal")
        goal.setFixedSize(100,60)
        self.goals.append(goal)
        #self._layout.addWidget(self.goals[-1])
        #self.goals[-1].hide()
        self.setPosition(goal,time)
        #self.moveGoalWidgets()
        self.show()
        #self.goals[-1].show()
        #self.repaint()

    def deleteLastGoal(self):
        if len(self.goals)>0:
            #self._layout.removeWidget(self.goals[-1])
            self.hide()
            self.goals[-1].deleteLater()
            self.goals.pop()
            self.show()
            #self.moveGoalWidgets()
            #self.repaint()

    def endGame(self):
        k = len(self.goals)
        for i in range(k):
            self.deleteLastGoal()

    def pause(self):
        try:
            self.gc.timer_fast.timeout.disconnect(self.moveGoalWidgets)
        except: pass

    def start(self):
        self.gc.timer_fast.timeout.connect(self.moveGoalWidgets)



        
# APPLICATION TO TEST WIDGET
# ///////////////////////////////////////////////////////////////
class _MainApp(QApplication):
    dti = DataInitializer
    def __init__(self, argv):
        super().__init__(argv)
        dtc = DataController()
        settings = Settings()
        self.settings = settings.items
        self.dti = DataInitializer(dtc,self.settings,self.initUI)
        

    def initUI(self):
        self.gc = GameController(self.dti)
        self.gc.game.players = self.dti.players[0:3]
        self.gc.reset()
        self.gc.start()        
        self.widget = TimeLine(self.gc)
        #self.widget = QWidget()
        #self.goal = TimeLineGoal(30,self.dti.players[0],"red",parent=self.widget)
        self.widget.show()
        self.widget.addGoal(self.gc.game.players[0],"red",10)
        #self.goal = TimeLineGoal(20,self.gc.game.players[0],team="red",parent=self.widget)
        # self.goal.setFixedSize(100,60)
        # self.goal.move(50,0)
        # self.goal.repaint()
        # time.sleep(1)
        # self.goal.move(50,100)
        # self.goal.repaint()
        # time.sleep(1)
        # self.goal.move(50,200)
        # self.goal.repaint()
        # time.sleep(1)
        # self.goal.move(50,300)



if __name__ == '__main__':
    app = _MainApp(sys.argv)
    sys.exit(app.exec_())      
                  