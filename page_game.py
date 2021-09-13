
from gui.widgets.circular_picture import ScaledCircularPicture
from game_controller import GameController
from gui.core.json_themes import Themes
from gui.core.json_settings import Settings
from gui.widgets.timeline import TimeLine
import datetime
from qt_core import *

class GamePage(QWidget):
    def __init__(self,gc:GameController):
        super().__init__()
        self.gc = gc
        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # FRAMES AND LAYOUTS
        # ///////////////////////////////////////////////////////////////
        self.frame_red = QFrame()
        self.layout_red = QVBoxLayout(self.frame_red)
        
        self.frame_gre = QFrame()
        self.layout_gre = QVBoxLayout(self.frame_gre)

        self.frame_center = QFrame()
        self.layout_center = QVBoxLayout(self.frame_center)

        # CENTER FRAME
        # ///////////////////////////////////////////////////////////////
        self.label_time = QLabel(text = str(datetime.timedelta(seconds=0)))
        self.label_time.setStyleSheet(f"font: 38pt {self.settings['font']['family']};")

        self.widget_timeline = TimeLine(self.gc)
        #self.widget_timeline.setMinimumSize(150,700)
        self.layout_center.addWidget(self.label_time,0,Qt.AlignHCenter)
        self.layout_center.addWidget(self.widget_timeline,0,Qt.AlignHCenter)


        # RED FRAME
        # ///////////////////////////////////////////////////////////////
        self.label_scoreRed = QLabel(text = "0")
        self.label_scoreRed.setAlignment(Qt.AlignCenter)
        self.label_scoreRed.setMinimumWidth(350)
        self.label_scoreRed.setStyleSheet(f"""color: {self.themes['app_color']['red']};
                                                font: 240pt {self.settings['font']['family']};""")
        self.frame_playersRed = QFrame()
        self.layout_playersRed = QVBoxLayout(self.frame_playersRed)
        self.widget_redDef = PlayerScoreWidget(self.gc,0)
        self.widget_redOff = PlayerScoreWidget(self.gc,1)
        self.layout_playersRed.addWidget(self.widget_redDef,0,Qt.AlignRight)
        self.layout_playersRed.addWidget(self.widget_redOff,0,Qt.AlignRight)

        self.layout_red.addWidget(self.label_scoreRed,1,Qt.AlignCenter)
        self.layout_red.addWidget(self.frame_playersRed,0,Qt.AlignHCenter|Qt.AlignTop)


        # GREEN FRAME
        # ///////////////////////////////////////////////////////////////
        self.label_scoreGre = QLabel(text = "0")
        self.label_scoreGre.setAlignment(Qt.AlignCenter)
        self.label_scoreGre.setMinimumWidth(350)
        self.label_scoreGre.setStyleSheet(f"""color: {self.themes['app_color']['green']};
                                                font: 240pt {self.settings['font']['family']};""")
        self.frame_playersGre = QFrame()
        self.layout_playersGre = QVBoxLayout(self.frame_playersGre)
        self.widget_greDef = PlayerScoreWidget(self.gc,3)
        self.widget_greOff = PlayerScoreWidget(self.gc,2)
        self.layout_playersGre.addWidget(self.widget_greOff,0,Qt.AlignRight)
        self.layout_playersGre.addWidget(self.widget_greDef,0,Qt.AlignRight)

        self.layout_gre.addWidget(self.label_scoreGre,1,Qt.AlignCenter)
        self.layout_gre.addWidget(self.frame_playersGre,0,Qt.AlignHCenter|Qt.AlignTop)

        self._layout = QHBoxLayout()
        self._layout.addWidget(self.frame_red)
        self._layout.addWidget(self.frame_center)
        self._layout.addWidget(self.frame_gre)

        self.setLayout(self._layout)

        self.gc.timeUpdate.connect(lambda e: self.label_time.setText(e))

    def updateScores(self):
        self.label_scoreRed.setText(f"{self.gc.game.scoreRed}")
        self.label_scoreGre.setText(f"{self.gc.game.scoreGre}")

        self.widget_redDef.label_score.setText(f"{self.gc.game.scores[0]}")
        self.widget_redOff.label_score.setText(f"{self.gc.game.scores[1]}")
        self.widget_greDef.label_score.setText(f"{self.gc.game.scores[2]}")
        self.widget_greOff.label_score.setText(f"{self.gc.game.scores[3]}")

    def initWidgets(self):
        self.widget_redDef.widget_pic.setPixmap(self.gc.game.players[0].pixMap)
        self.widget_redOff.widget_pic.setPixmap(self.gc.game.players[1].pixMap)
        self.widget_greDef.widget_pic.setPixmap(self.gc.game.players[2].pixMap)
        self.widget_greOff.widget_pic.setPixmap(self.gc.game.players[3].pixMap)

        self.widget_redDef.label_name.setText(self.gc.game.players[0].name)
        self.widget_redOff.label_name.setText(self.gc.game.players[1].name)
        self.widget_greDef.label_name.setText(self.gc.game.players[2].name)
        self.widget_greOff.label_name.setText(self.gc.game.players[3].name)

class PlayerScoreWidget(QWidget):
    def __init__(self,gc:GameController,position):
        super().__init__()
        self.gc = gc
        self.position = position
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

        self.label_name = QLabel(text=f"{self.gc.game.players[self.position].name}")
        self.label_score = QLabel(text=f"{self.gc.game.scores[self.position]}")
        self.frame_stats = QFrame()
        self.layout_stats = QVBoxLayout(self.frame_stats)
        self.frame_pic_name = QFrame()
        #elf.frame_pic_name.setFixedWidth(80)
        self.layout_pic_name = QVBoxLayout(self.frame_pic_name)
        self.frame_widget = QFrame()
        self.layout_widget = QHBoxLayout(self.frame_widget)
        if self.position < 2 :
            self.widget_pic = ScaledCircularPicture(self.gc.game.players[self.position].pixMap,self.red,size=80)
            self.layout_stats.addWidget(self.label_score,0,Qt.AlignRight|Qt.AlignBottom)

            self.layout_pic_name.addWidget(self.widget_pic,0,Qt.AlignHCenter|Qt.AlignBottom)
            self.layout_pic_name.addWidget(self.label_name,0,Qt.AlignHCenter|Qt.AlignTop)

            self.layout_widget.addWidget(self.frame_stats,0,Qt.AlignRight|Qt.AlignVCenter)
            self.layout_widget.addWidget(self.frame_pic_name,0,Qt.AlignLeft|Qt.AlignVCenter)
            self.label_score.setStyleSheet(f"""color: {self.red};
                                                font: 30pt {self.settings['font']['family']};""")        

        else:
            self.widget_pic = ScaledCircularPicture(self.gc.game.players[self.position].pixMap,self.green,size=80)
            self.layout_stats.addWidget(self.label_score,0,Qt.AlignLeft|Qt.AlignBottom)

            self.layout_pic_name.addWidget(self.widget_pic,0,Qt.AlignHCenter|Qt.AlignBottom)
            self.layout_pic_name.addWidget(self.label_name,0,Qt.AlignHCenter|Qt.AlignTop)
         
            self.layout_widget.addWidget(self.frame_pic_name,0,Qt.AlignRight|Qt.AlignVCenter)
            self.layout_widget.addWidget(self.frame_stats,0,Qt.AlignLeft|Qt.AlignVCenter)

            self.label_score.setStyleSheet(f"""color: {self.green};
                                                font: 30pt {self.settings['font']['family']};""")
        

        self.setFixedSize(300,170)
        self.setLayout(self.layout_widget)
    
#     def updatePlayers(self):
#         if self.position < 2 :
# #self.widget_pic = ScaledCircularPicture(self.gc.game.players[self.position].pixMap,self.red)
#             old = self.layout_pic_name.children()
#             self.layout_pic_name.replaceWidget(old[0],ScaledCircularPicture(self.gc.game.players[self.position].pixMap,self.red))
#         else:
#  #           self.widget_pic_new = ScaledCircularPicture(self.gc.game.players[self.position].pixMap,self.green)
#             self.layout_pic_name.replaceWidget(self.widget_pic,ScaledCircularPicture(self.gc.game.players[self.position].pixMap,self.green))

        
