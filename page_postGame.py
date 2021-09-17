from models.player import Player
from models.game import Game
from gui.widgets.svg_widget import SVGWidget
import sys
sys.path.append('../BakApp_RPi')
from gui.widgets.circular_picture import ScaledCircularPicture
from gui.widgets.py_circular_progress.py_circular_progress import PyCircularProgress
from gui.core.json_settings import Settings
from gui.core.json_themes import Themes
from data_initializer import DataInitializer
from data_controller import DataController
from qt_core import *

class TotalDeltaEloWidget(QWidget):
    def __init__(self,deltaElo):
        super().__init__()
        self.deltaElo = deltaElo
        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items
        self.width_elo = 20
        self.setFixedSize(self.width_elo*3.5,350)
        self.setStyleSheet("background: grey;")

    def paintEvent(self,event):
        height_elo = abs(self.deltaElo)*1.5
        if self.deltaElo >= 0: pos = True
        else: pos = False 
        width_line = 2
        length_line = 3*self.width_elo

        text_width = 30
        text_height = 30
        p = QPainter()
        p.begin(self)
        p.setRenderHint(QPainter.Antialiasing)
        pen = QPen(QColor("white"))
        p.setPen(pen)

        aleft = round(self.width()/2 - self.width_elo/2)
        
        if pos: atop = round(self.height()/2 - height_elo)
        else: atop = round(self.height()/2)

        rect_deltaElo = QRect(aleft,atop,self.width_elo,round(height_elo))
        p.setBrush(QColor(self.themes['app_color']['context_color']))
        p.drawRoundedRect(rect_deltaElo,2,2)
        x1 = round(self.width()/2-length_line/2)
        x2 = round(self.width()/2+length_line/2)
        y = round(self.height()/2)
        pen.setWidth(width_line)
        p.setPen(pen)
        p.drawLine(x1,y,x2,y)

        aleft = round(aleft-text_width)
        if pos: atop = round(atop-text_height)
        else: atop = round(atop + height_elo)
        rect_text = QRect(aleft,atop,text_width,text_height)
        if pos: p.drawText(rect_text,Qt.AlignRight|Qt.AlignBottom,f"+{round(self.deltaElo)}")
        else: p.drawText(rect_text,Qt.AlignRight|Qt.AlignTop,f"-{abs(round(self.deltaElo))}")
        p.end()

class DeltaEloDivsionWidget(QWidget):
    def __init__(self,deltaElo_base,deltaElo_ind_bonus,deltaElo_team_bonus):
        super().__init__()
        self.deltaElo_base = deltaElo_base
        self.deltaElo_ind_bonus = deltaElo_ind_bonus
        self.deltaElo_team_bonus = deltaElo_team_bonus
        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items
        self.width_elo = 20
        self.width_line = 2
        self.text_width = 30
        self.text_height = 30
        self.setStyleSheet("background: grey;")
        self.width_icon = self.width_elo - 5
        self.color_icon = "white"
        self.icon_win = SVGWidget(self,"icon_trophy2.svg",self.color_icon,self.width_icon,self.width_icon)
        self.icon_individual = SVGWidget(self,"icon_individual.svg",self.color_icon,self.width_icon,self.width_icon)
        self.icon_team = SVGWidget(self,"icon_team.svg",self.color_icon,self.width_icon,self.width_icon)
        self.setFixedSize(self.width_elo*9,350)

    def paintEvent(self,event):
        x2 = round(self.width()/2)
        x1 = x2 -self.width_elo - self.text_width
        x3 = x2 + self.width_elo + self.text_width

        self.length_line = x3-x2+6*self.width_elo
        self.paintElo(self.deltaElo_base,x1,self.icon_win)
        self.paintElo(self.deltaElo_ind_bonus,x2,self.icon_individual)
        self.paintElo(self.deltaElo_team_bonus,x3,self.icon_team)

        p = QPainter()
        p.begin(self)
        p.setRenderHint(QPainter.Antialiasing)
        pen = QPen(QColor("white"))
        pen.setWidth(self.width_line)
        p.setPen(pen)
        x1 = round(self.width()/2-self.length_line/2)
        x2 = round(self.width()/2+self.length_line/2)
        y = round(self.height()/2)
        
        p.drawLine(x1,y,x2,y)
        

    def paintElo(self,elo,x,icon:SVGWidget):
        height_elo = abs(elo)*1.5
        if elo >= 0: pos = True
        else: pos = False 

        p = QPainter()
        p.begin(self)
        p.setRenderHint(QPainter.Antialiasing)
        pen = QPen(QColor("white"))
        p.setPen(pen)

        aleft = round(x - self.width_elo/2)
        if pos: atop = round(self.height()/2 - height_elo)
        else: atop = round(self.height()/2)
        rect_deltaElo = QRect(aleft,atop,self.width_elo,round(height_elo))
        p.setBrush(QColor(self.themes['app_color']['context_color']))
        p.drawRoundedRect(rect_deltaElo,2,2)

        if pos: top_icon = round(atop - self.width_icon - 5)
        else: top_icon = round(atop + height_elo + 5)
        icon.move(round(x-self.width_icon/2),top_icon)


        aleft = round(aleft-self.text_width)
        if pos: atop = round(atop-self.text_height)
        else: atop = round(atop + height_elo)
        rect_text = QRect(aleft,atop,self.text_width,self.text_height)
        if pos: p.drawText(rect_text,Qt.AlignRight|Qt.AlignBottom,f"+{round(elo)}")
        else: p.drawText(rect_text,Qt.AlignRight|Qt.AlignTop,f"-{abs(round(elo))}")

        p.end()

class PlayerStatsWidget(QWidget):
    def __init__(self,player:Player,pos:int,game:Game):
        super().__init__()
        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        if pos < 2: self.color = self.themes['app_color']['red']
        else: self.color = self.themes['app_color']['green']

        self._layout = QHBoxLayout(self)
        
        self.frame_pic_name = QFrame()
        self.layout_pic_name = QVBoxLayout(self.frame_pic_name)
        self.widget_pic = ScaledCircularPicture(player.pixMap,self.color,size=60)
        self.label_name = QLabel(text=player.name)
        self.layout_pic_name.addWidget(self.widget_pic,0,Qt.AlignHCenter|Qt.AlignBottom)
        self.layout_pic_name.addWidget(self.label_name,0,Qt.AlignHCenter|Qt.AlignTop)

        self.label_goals = QLabel(text=f"{game.scores[pos]} goals")

        self.widget_total_elo = TotalDeltaEloWidget(game.deltaEloTotal[pos])
        self.widget_division_elo = DeltaEloDivsionWidget(game.deltaEloBase[pos],game.deltaEloIndividualBonus[pos],game.deltaEloTeamBonus[pos])

        if pos > 1:
            self._layout.addWidget(self.frame_pic_name)
            self._layout.addWidget(self.label_goals)
            self._layout.addWidget(self.widget_total_elo)
            self._layout.addWidget(self.widget_division_elo)

        else:
            self._layout.addWidget(self.widget_division_elo)
            self._layout.addWidget(self.widget_total_elo)
            self._layout.addWidget(self.label_goals)
            self._layout.addWidget(self.frame_pic_name)

class PostGamePage(QWidget):
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

        self._layout = QHBoxLayout(self)

        self.frame_red = QFrame()
        self.layout_red = QVBoxLayout(self.frame_red)

        self.frame_gre = QFrame()
        self.layout_gre = QVBoxLayout(self.frame_gre)

        self.widget_redDef = PlayerStatsWidget(dti.lastGame.players[0],0,dti.lastGame)
        self.widget_redOff = PlayerStatsWidget(dti.lastGame.players[1],1,dti.lastGame)
        self.widget_greDef = PlayerStatsWidget(dti.lastGame.players[2],2,dti.lastGame)
        self.widget_greOff = PlayerStatsWidget(dti.lastGame.players[3],3,dti.lastGame)

        self.layout_red.addWidget(self.widget_redDef)
        self.layout_red.addWidget(self.widget_redOff)
        self.layout_gre.addWidget(self.widget_greOff)
        self.layout_gre.addWidget(self.widget_greDef)

        self._layout.addWidget(self.frame_red)
        self._layout.addWidget(self.frame_gre)

class _MainApp(QApplication):
    dti = DataInitializer
    def __init__(self, argv):
        super().__init__(argv)
        dtc = DataController()
        settings = Settings()
        self.settings = settings.items
        self.dti = DataInitializer(dtc,self.settings,self.initUI)

    def initUI(self):
        #self.widget = TotalDeltaEloWidget(100)
        #self.widget = DeltaEloDivsionWidget(-100,+10,-5)
        # self.widget = PlayerStatsWidget(self.dti.lastGame.players[0],0,self.dti.lastGame)
        self.widget = PostGamePage(self.dti)
        self.widget.show() 



if __name__ == '__main__':
    app = _MainApp(sys.argv)
    sys.exit(app.exec_())      
           

        