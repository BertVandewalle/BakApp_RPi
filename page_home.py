import logging
import sys
from data_controller import DataController
from gui.core.json_themes import Themes
from gui.core.json_settings import Settings
from gui.widgets.py_last_game.py_last_game import PyLastGameWidget
from qt_core import *
from data_initializer import DataInitializer

class HomePage(QWidget):
    def __init__(self,dti:DataInitializer):
        super().__init__()
        self._dti = dti

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        self.resize(self.settings["startup_size"][0], self.settings["startup_size"][1])


        # FRAMES AND LAYOUTS
        # ///////////////////////////////////////////////////////////////
        self.frame_lastGame = QFrame()
        self.layout_lastGame = QHBoxLayout(self.frame_lastGame)
        self.frame_lastGame.setLayout(self.layout_lastGame)
        
        self.frame_bottom = QFrame() 
        self.layout_bottom = QHBoxLayout(self.frame_bottom)
        self.frame_ranking = QFrame()
        self.layout_ranking = QVBoxLayout(self.frame_ranking)
        self.frame_gamesToday = QFrame()
        self.layout_gamesToday = QVBoxLayout(self.frame_gamesToday)
        self.layout_bottom.addWidget(self.frame_ranking)
        self.layout_bottom.addWidget(self.frame_gamesToday)

        # TITLE WIDGET
        # ///////////////////////////////////////////////////////////////
        self.label_homeTitle = QLabel()
        self.label_homeTitle.setText("Welcome Back!")

        # LAST GAME WIDGET
        # ///////////////////////////////////////////////////////////////
        self.widget_lastGame = PyLastGameWidget(game=self._dti.lastGame)
        #self.widget_lastGame = QLabel(text="TEST")
        #self.widget_lastGame.setMinimumSize(400,400)
        # sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(1)
        # sizePolicy.setHeightForWidth(self.frame_lastGame.sizePolicy().hasHeightForWidth())
        # self.frame_lastGame.setSizePolicy(sizePolicy)
        self.frame_lastGame.setStyleSheet(f"background: {self.themes['app_color']['bg_three']} ; border-radius: 8")
        #self.frame_lastGame.setMaximumHeight(parent.height()//2)
        self.layout_lastGame.addWidget(self.widget_lastGame)

        # ADD ALL TO PAGE LAYOUT
        self.layout_page = QVBoxLayout()
        self.layout_page.addWidget(self.label_homeTitle,0,Qt.AlignHCenter)
        self.layout_page.addWidget(self.frame_lastGame,1)
        self.layout_page.addWidget(self.frame_bottom,2)

        self.setLayout(self.layout_page)




        
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
        logging.warning("init UI")
        self.widget = HomePage(self.dti)
        self.widget.show() 
        logging.warning("show widget")



if __name__ == '__main__':
    app = _MainApp(sys.argv)
    sys.exit(app.exec_())      
           

   