import logging
import sys
sys.path.append('../BakApp_RPi')
from gui.widgets.circular_picture import ScaledCircularPicture
from gui.widgets.py_circular_progress.py_circular_progress import PyCircularProgress
from gui.core.json_settings import Settings
from gui.core.json_themes import Themes
from data_initializer import DataInitializer
from data_controller import DataController

from PyQt5.QtSvg import QSvgWidget
from gui.core.functions import Functions
from models import *
from models.player import Player
#from models.game import Game
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import * 

class PyLastGameWidget(QWidget):
    SCORE_LABEL_SIZE = 30
    def __init__(
        self,
        red="red",
        green="green",
        game:Game = None,
    ):
        super().__init__()
        self._game = game
        if self._game != None:
            self._red = red
            self._green = green

            # LOAD SETTINGS
            # ///////////////////////////////////////////////////////////////
            settings = Settings()
            self.settings = settings.items

            # LOAD THEME COLOR
            # ///////////////////////////////////////////////////////////////
            themes = Themes()
            self.themes = themes.items
            self._red = self.themes['app_color']['red']
            self._green = self.themes['app_color']['green']

            self.setStyleSheet(f"""background: {self.themes['app_color']['bg_three']} ; 
                                border-radius: 8;
                                font = {self.settings['font']['text_size']}
                                """)


            # TITLE LABEL
            # ///////////////////////////////////////////////////////////////
            self.label_title = QLabel(text="Last Game")

            # STATS FRAME
            # ///////////////////////////////////////////////////////////////
            self.layout_stats = QHBoxLayout()
            self.frame_red_players = QFrame()
            self.layout_red_players = QVBoxLayout(self.frame_red_players)
            self.frame_gre_players = QFrame()
            self.layout_gre_players = QVBoxLayout(self.frame_gre_players)
            self.frame_central = QFrame()
            self.layout_central = QVBoxLayout(self.frame_central)


            # TOTAL SCORE LABEL
            # ///////////////////////////////////////////////////////////////
            self.frame_score = QFrame()
            self.layout_score = QHBoxLayout(self.frame_score)
            self.layout_score.setSpacing(5)
            self.label_scoreRed = QLabel(parent=self.frame_score,text=f"{self._game.scoreRed}")
            sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
            sizePolicy1.setHorizontalStretch(1)
            sizePolicy1.setVerticalStretch(0)
            sizePolicy1.setHeightForWidth(self.label_scoreRed.sizePolicy().hasHeightForWidth())
            self.label_scoreRed.setSizePolicy(sizePolicy1)
            self.label_scoreRed.setAlignment(Qt.AlignRight)
            self.label_scoreRed.setStyleSheet(f"""color: {self._red};
                                                font: {self.SCORE_LABEL_SIZE}pt Arial;
                                                """)

            self.label_scoreGre = QLabel(text=f"{self._game.scoreGre}")
            self.label_scoreGre.setStyleSheet(f"""color: {self._green};
                                                font: {self.SCORE_LABEL_SIZE}pt Arial; 
                                                """)
            sizePolicy1.setHeightForWidth(self.label_scoreGre.sizePolicy().hasHeightForWidth())
            self.label_scoreGre.setSizePolicy(sizePolicy1)
            self.label_dash = QLabel(text="-")
            self.label_dash.setStyleSheet(f""" font: {self.SCORE_LABEL_SIZE}pt Arial;
                                            """)

            #maxWidth = self.FindMaxWidth(self.label_scoreRed,self.label_scoreGre)
            self.label_scoreRed.setFixedWidth(60)
            self.label_scoreGre.setFixedWidth(60)
            self.layout_score.addWidget(self.label_scoreRed,0,Qt.AlignRight|Qt.AlignVCenter)
            self.layout_score.addWidget(self.label_dash,0,Qt.AlignCenter)
            self.layout_score.addWidget(self.label_scoreGre,0,Qt.AlignLeft|Qt.AlignVCenter)

            # CENTRAL SVG WIDGET
            # ///////////////////////////////////////////////////////////////
            self.football_table_widget = FootballTableWidget()
            self.football_table_widget.setMinimumSize(150,150) 

            # DURATION LABEL
            # ///////////////////////////////////////////////////////////////
            self.label_duration = QLabel(text=f"{self._game.duration}")
            
            # ADD WIDGETS TO CENTRAL LAYOUT
            # ///////////////////////////////////////////////////////////////
            self.layout_central.addWidget(self.frame_score,0,Qt.AlignHCenter|Qt.AlignBottom)
            self.layout_central.addWidget(self.football_table_widget,0,Qt.AlignCenter)
            self.layout_central.addWidget(self.label_duration,0,Qt.AlignHCenter|Qt.AlignTop)

            # ADD WIDGETS TO RED AND GREEN LAYOUT
            # ///////////////////////////////////////////////////////////////
            self.layout_red_players.addSpacing(40)
            self.redDefWidget = PlayerStatWidget(self._game,0)
            self.layout_red_players.addWidget(self.redDefWidget,0,Qt.AlignRight|Qt.AlignBottom)
            self.layout_red_players.addSpacing(20)
            self.redOffWidget = PlayerStatWidget(self._game,1)
            self.layout_red_players.addWidget(self.redOffWidget,0,Qt.AlignRight|Qt.AlignTop)

            self.layout_gre_players.addSpacing(40)
            self.greOffWidget = PlayerStatWidget(self._game,3)
            self.layout_gre_players.addWidget(self.greOffWidget,0,Qt.AlignLeft|Qt.AlignBottom)
            self.layout_gre_players.addSpacing(20)
            self.greDefWidget = PlayerStatWidget(self._game,2)
            self.layout_gre_players.addWidget(self.greDefWidget,0,Qt.AlignLeft|Qt.AlignTop)

            # ADD WIDGETS TO STAT LAYOUT            
            self.layout_stats.addWidget(self.frame_red_players,1,Qt.AlignRight)
            self.layout_stats.addWidget(self.frame_central,0,Qt.AlignHCenter)
            self.layout_stats.addWidget(self.frame_gre_players,1,Qt.AlignLeft)
            self.layout_stats.setContentsMargins(0,0,0,0)

            # ADD ALL TO WIDGET LAYOUT
            self.widget_layout = QVBoxLayout()
            self.widget_layout.addWidget(self.label_title)
            self.widget_layout.addLayout(self.layout_stats)
            self.widget_layout.setContentsMargins(0,0,0,0)
            self.setLayout(self.widget_layout)

    def FindMaxWidth(self,label1:QLabel,label2:QLabel):
        if label1.width()>label2.width(): return label1.width()
        else: return label2.width()

class PlayerStatWidget(QWidget):
    def __init__(self,game:Game,position):
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
        # LABELS
        self.label_name = QLabel(text=f"{game.players[position].name}")
        # self.label_pic =  QLabel()
        # pixmap = game.players[position].pixMap
        # scaledPixmap = pixmap.scaled(30,50,Qt.KeepAspectRatio)
        # self.label_pic.setPixmap(scaledPixmap)
        self.label_score = QLabel(text=f"{game.scores[position]} goals")
        self.label_dElo = QLabel(text=f"{int(game.deltaEloTotal[position])} elo")
        self.frame_stats = QFrame()
        self.layout_stats = QVBoxLayout(self.frame_stats)
        self.frame_pic_name = QFrame()
        self.frame_pic_name.setFixedWidth(80)
        self.layout_pic_name = QVBoxLayout(self.frame_pic_name)
        self.frame_widget = QFrame()
        self.layout_widget = QHBoxLayout(self.frame_widget)
        if position < 2 :
            self.widget_pic = ScaledCircularPicture(game.players[position].pixMap,self.red,size=40)
            self.layout_stats.addWidget(self.label_score,0,Qt.AlignRight|Qt.AlignBottom)
            self.layout_stats.addWidget(self.label_dElo,0,Qt.AlignRight|Qt.AlignTop)

            self.layout_pic_name.addWidget(self.widget_pic,0,Qt.AlignHCenter|Qt.AlignBottom)
            self.layout_pic_name.addWidget(self.label_name,0,Qt.AlignHCenter|Qt.AlignTop)

            self.layout_widget.addWidget(self.frame_stats,0,Qt.AlignRight|Qt.AlignVCenter)
            self.layout_widget.addWidget(self.frame_pic_name,0,Qt.AlignLeft|Qt.AlignVCenter)
        else:
            self.widget_pic = ScaledCircularPicture(game.players[position].pixMap,self.green,size=40)
            self.layout_stats.addWidget(self.label_score,0,Qt.AlignLeft|Qt.AlignBottom)
            self.layout_stats.addWidget(self.label_dElo,0,Qt.AlignLeft|Qt.AlignTop)

            self.layout_pic_name.addWidget(self.widget_pic,0,Qt.AlignHCenter|Qt.AlignBottom)
            self.layout_pic_name.addWidget(self.label_name,0,Qt.AlignHCenter|Qt.AlignTop)
         
            self.layout_widget.addWidget(self.frame_pic_name,0,Qt.AlignRight|Qt.AlignVCenter)
            self.layout_widget.addWidget(self.frame_stats,0,Qt.AlignLeft|Qt.AlignVCenter)
        

        
        self.setLayout(self.layout_widget)
        

class FootballTableWidget(QWidget):
    def __init__(self,color:QColor=QColor("white")):
        QWidget.__init__(self)
        self._image_path = Functions.set_svg_image("table-football.svg")
        self.image = QPixmap(self._image_path)
        self.scaledPix = self.image.scaled(self.size(), Qt.KeepAspectRatio, transformMode = Qt.SmoothTransformation)
        self._color = color
        #self.show()

    def paintEvent(self,event):
        p = QPainter()
        p.begin(self)
        p.setRenderHint(QPainter.Antialiasing)
        rect = QRect(0,0,self.width(),self.height())
        #image= image.scaled(300,800,Qt.KeepAspectRatio)
        painter = QPainter(self.image)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(self.image.rect(),self._color)

        self.scaledPix = self.image.scaled(self.size(), Qt.KeepAspectRatio, transformMode = Qt.SmoothTransformation)
        p.drawPixmap(
                    int((self.width()-self.scaledPix.width())/2),
                    int((self.height()-self.scaledPix.height())/2),
                    self.scaledPix)
        painter.end() 
        p.end()
        


class MainApp(QApplication):
    dti = DataInitializer
    def __init__(self, argv):
        super().__init__(argv)
        dtc = DataController()
        settings = Settings()
        self.settings = settings.items
        self.dti = DataInitializer(dtc,self.settings,self.initUI)

    def initUI(self):
        logging.warning("init UI")
        self.widget = PyLastGameWidget("red", "green",game=self.dti.lastGame)
        #self.widget = PlayerStatWidget(game=self.dti.lastGame,position=0)
        self.widget.show() 
        logging.warning("show widget")



if __name__ == '__main__':
    app = MainApp(sys.argv)
    sys.exit(app.exec_())      
           