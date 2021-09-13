
import sys
from gui.widgets.timeline import TimeLineGoal
from game_controller import GameController
from gui.core.json_settings import Settings
from data_controller import DataController
from data_initializer import DataInitializer
from qt_core import *


class testWidget(QWidget):
    def __init__(self,dti):
        super().__init__()
        self.dti = dti
        #self.anotherwidget = QWidget(self)
        #self.anotherwidget.setMinimumSize(500,500)
        # self.goal = TimeLineGoal(30,self.dti.players[0],"red",parent=self.anotherwidget)
        # self.goal.move(50,100)
        
        # self.addGoal(self)


    def addGoal(self,parent=None):
        self.goal = TimeLineGoal(30,self.dti.players[0],"red")
        self.goal.move(50,100)

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
        self.widget= testWidget(self.dti)       
        #self.widget = TimeLine(self.gc)
        #self.widget = QWidget()
        self.widget.show()
        self.widget.addGoal(parent=self.widget)
        # self.widget.addGoal(self.widget.anotherwidget)
        #self.widget.addGoal(self.gc.game.players[0],"red",10)
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
                  