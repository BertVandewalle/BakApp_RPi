import sys
sys.path.append('../BakApp_RPi')
from gui.widgets.circular_picture import ScaledCircularPicture
from gui.widgets.py_circular_progress.py_circular_progress import PyCircularProgress
from gui.core.json_settings import Settings
from gui.core.json_themes import Themes
from data_initializer import DataInitializer
from data_controller import DataController

from qt_core import *
from models import *

class GamesTodayWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.games = []
        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(0,0,0,0)
        self._layout.setSpacing(0)
        self.label_title = QLabel(text="Games Today")
        self.label_title.setStyleSheet("font-weight: bold;")
        self._layout.addWidget(self.label_title,0,Qt.AlignVCenter|Qt.AlignLeft)
        self.setMinimumSize(300,300)
        self._layout.addStretch(2)
    


    def addGame(self,game:Game):
        widget = GameToday(game)
        self._layout.insertWidget(1,widget,1,Qt.AlignTop)
        self.games.insert(0,widget)


class GameToday(QWidget):
    def __init__(self,game:Game):
        super().__init__()
        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items
        self.game = game

        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.setSizePolicy(sizePolicy)
        self.setGeometry(0,0,1000,1000)

        self._layout = QHBoxLayout(self)
        self._layout.setContentsMargins(0,0,0,0)

        startDateTime = QDateTime.fromString(self.game.startDateTime,"yyyy-MM-ddThh:mm:ss")
        startDateTime = startDateTime.toLocalTime()
        self.label_time = QLabel(text=startDateTime.time().toString("hh:mm"))
        
        self.frame_red_names = QFrame()
        self.frame_red_names.setContentsMargins(0,0,0,0)
        self.frame_red_names.setStyleSheet(f"""color: {self.themes['app_color']['red']};
                                                font-weight: {self.setFontWeight('red')};""")
        self.layout_red_names = QVBoxLayout(self.frame_red_names)
        self.label_redDef_name = QLabel(text=self.game.players[0].name)
        self.label_redDef_name.setContentsMargins(0,0,0,0)
        self.label_redOff_name = QLabel(text=self.game.players[1].name)
        self.label_redOff_name.setContentsMargins(0,0,0,0)

        self.layout_red_names.addWidget(self.label_redDef_name,0,Qt.AlignRight|Qt.AlignBottom)
        self.layout_red_names.addWidget(self.label_redOff_name,0,Qt.AlignRight|Qt.AlignTop)

        self.frame_score = QFrame()
        self.layout_score = QHBoxLayout(self.frame_score)
        self.label_red_score = QLabel(text=str(self.game.scoreRed))
        self.label_red_score.setAlignment(Qt.AlignCenter)
        self.label_red_score.setStyleSheet(f"""color: {self.themes['app_color']['red']};
                                                font-weight: {self.setFontWeight('red')};""")

        self.label_dash = QLabel(text="-")
        self.label_dash.setAlignment(Qt.AlignCenter)
        self.label_gre_score = QLabel(text=str(self.game.scoreGre))
        self.label_gre_score.setStyleSheet(f"""color: {self.themes['app_color']['green']};
                                                font-weight: {self.setFontWeight('green')};""")
        self.label_gre_score.setAlignment(Qt.AlignCenter)
        self.layout_score.addWidget(self.label_red_score)
        self.layout_score.addWidget(self.label_dash)
        self.layout_score.addWidget(self.label_gre_score)
        
        self.frame_gre_names = QFrame()
        self.layout_gre_names = QVBoxLayout(self.frame_gre_names)
        self.frame_gre_names.setStyleSheet(f"""color: {self.themes['app_color']['green']};
                                                font-weight: {self.setFontWeight('green')};""")

        self.label_greDef_name = QLabel(text=self.game.players[2].name)
        self.label_greOff_name = QLabel(text=self.game.players[3].name)
        self.layout_gre_names.addWidget(self.label_greOff_name,0,Qt.AlignLeft|Qt.AlignBottom)
        self.layout_gre_names.addWidget(self.label_greDef_name,0,Qt.AlignLeft|Qt.AlignTop)

        self._layout.addWidget(self.label_time,0,Qt.AlignRight)
        self._layout.addWidget(self.frame_red_names,0,Qt.AlignRight)
        self._layout.addWidget(self.frame_score)
        self._layout.addWidget(self.frame_gre_names,0,Qt.AlignLeft)

      
        #self.setMinimumSize(50,50)
    def sizeHint(self):
        return QSize(int(self.width()),int(self.height()))

    def setFontWeight(self,team:str):
        if self.game.scoreRed > self.game.scoreGre: winner = "red"
        else: winner = "green"
        if team == winner: return "bold"
        else: return "normal"


class _MainApp(QApplication):
    dti = DataInitializer
    def __init__(self, argv):
        super().__init__(argv)
        dtc = DataController()
        settings = Settings()
        self.settings = settings.items
        self.dti = DataInitializer(dtc,self.settings,self.initUI)

    def initUI(self):
        self.widget = GamesTodayWidget()
        self.widget.addGame(self.dti.lastGame)
        self.widget.addGame(self.dti.lastGame)
        
        self.widget.show() 
        self.widget.addGame(self.dti.lastGame)
        self.widget.addGame(self.dti.lastGame)
        


if __name__ == '__main__':
    app = _MainApp(sys.argv)
    sys.exit(app.exec_())      
                 