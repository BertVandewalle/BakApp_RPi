from models.rank import Rank
import sys
from models import player
sys.path.append('../BakApp_RPi')
from models.player import Player

from gui.core.json_themes import Themes
from gui.core.json_settings import Settings
from data_controller import DataController
from data_initializer import DataInitializer
from game_controller import GameController

from qt_core import *
import pyqtgraph as pg
import numpy as np

class Ranking(QWidget):
    def __init__(self,dti:DataInitializer,parent):
        super().__init__()
        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items
        self.dti= dti
        self._parent = parent
        self.players_ranked = sorted(self.dti.players, key=lambda x:x.elo,reverse=True)
        self.player_amount = len(self.players_ranked)
        # self.spacing = 10 
        self.init()
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.setSizePolicy(sizePolicy)
        self.setGeometry(0,0,1000,1000)
       
    def init(self):
        pass
    def paintEvent(self,event):
        # self.setFixedSize(self._parent.width(),self._parent.height())
        print(str(self.size())+"   "+str(self._parent.size()))

        print(self.sizeHint())
        rank_label_height = 30
        # width = (self._parent.height()-self.spacing*self.player_amount)//self.player_amount
        width = round(float(self.height()-rank_label_height)/(self.player_amount*1.2+0.2))
        spacing = round(0.2*width)
        min_length = 100
        max_length = self.width()-20
        min_elo = round(float(self.players_ranked[-1].elo))
        max_elo = round(float(self.players_ranked[0].elo))
        p = QPainter()
        p.begin(self)
        p.setRenderHint(QPainter.Antialiasing)
        # rect = QRect(0,0,self.width()//3,self.height())
        # p.setBrush(QColor("blue"))
        # p.setOpacity(0.6)
        # p.drawRect(rect)
        # p.setOpacity(1)
        pen = QPen(QColor("white"))
        p.setPen(pen)
        for rank in self.dti.ranks:
            x0 = round(min_length + float(rank.lowerbound-min_elo)/(max_elo-min_elo) * (max_length-min_length))
            x1 = round(min_length + float(rank.upperbound-min_elo)/(max_elo-min_elo) * (max_length-min_length))
            if x0 > 0 or x0 < self.width():
                p.drawLine(x0,0,x0,self.height())
                rect = QRect(x0,self.height()-rank_label_height,x1-x0,rank_label_height)
                p.drawText(rect,Qt.AlignCenter,f"{rank.division}\n{rank.subDivision}")

        for i in range(self.player_amount):
            elo = round(float(self.players_ranked[i].elo))
            atop = i*(width+spacing)
            length = round(min_length + float(elo-min_elo)/(max_elo-min_elo) * (max_length-min_length))
            rect = QRect(0,atop,length,width)
            p.setBrush(QColor(self.themes['app_color'][self.players_ranked[i].rank.division]))
            p.drawRoundedRect(rect, 2, 2)
            p.drawText(QRect(5,atop,length,width), Qt.AlignLeft|Qt.AlignVCenter, f"{self.players_ranked[i].name}")
            p.drawText(QRect(5,atop,length-10,width), Qt.AlignRight|Qt.AlignVCenter, f"{elo}")
        
        p.end()

    def sizeHint(self):
        return QSize(int(self.width()),int(self.height()))

class RankingWidget(QWidget):
    def __init__(self,dti:DataInitializer):
        super().__init__()
        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items
        self.dti= dti

        self.label_title = QLabel(text="Ranking")

        self.frame_ranking = QFrame()
        #self.frame_ranking.setStyleSheet("background: black;")
        self.layout_ranking = QHBoxLayout(self.frame_ranking)
        self.ranking = Ranking(self.dti,self.frame_ranking)
        self.layout_ranking.addWidget(self.ranking,1,Qt.AlignCenter)
        self.frame_ranking.setContentsMargins(0,0,0,0)


        self._layout = QVBoxLayout(self)
        self._layout.addWidget(self.label_title,0,Qt.AlignVCenter|Qt.AlignLeft)
        self._layout.addWidget(self.frame_ranking,1)
        #self._layout.setContentsMargins(0,0,0,0)
        
        


# APPLICATION TO TEST WIDGET
# ///////////////////////////////////////////////////////////////
class _MainApp(QApplication):
    #dti = DataInitializer
    def __init__(self, argv):
        super().__init__(argv)
        dtc = DataController()
        
        settings = Settings()
        self.settings = settings.items
        self.dti = DataInitializer(dtc,self.settings,self.initUI)

    def initUI(self):
        self.widget = RankingWidget(self.dti)
        self.widget.show()



if __name__ == '__main__':
    app = _MainApp(sys.argv)
    sys.exit(app.exec_())      
