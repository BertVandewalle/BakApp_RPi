from page_postGame import PostGamePage
from page_game import GamePage
from game_controller import GameController
from models.game import Game
from page_home import HomePage
from data_initializer import DataInitializer
from qt_core import *
from py_player_selection import PyPlayerSelectionWidget

class MainPages(QStackedWidget):
    def __init__(self,parent,dti:DataInitializer,gc:GameController):
        super().__init__()
        self._parent = parent
        self._dti = dti
        self.gc = gc
        self.setup()

    def setup(self):
        try:
            self.removeWidget(self.page_home)
            self.removeWidget(self.page_playerSelection)
            self.removeWidget(self.page_game)
            self.removeWidget(self.page_ranking)
            self.removeWidget(self.page_postgame)
        except: pass
        self.page_home = HomePage(self._dti)
        self.page_home.setStyleSheet("color:white")
        self.page_playerSelection = PyPlayerSelectionWidget(self._dti.players)
        self.page_game = GamePage(self.gc)
        self.page_ranking = QWidget()
        self.page_postgame = PostGamePage(self._dti)
        self.page_postgame.setStyleSheet("color:white")

        # ADD WIDGETS TO STACK
        # ///////////////////////////////////////////////////////////////
        self.addWidget(self.page_home)
        self.addWidget(self.page_playerSelection)
        self.addWidget(self.page_game)
        self.addWidget(self.page_ranking)
        self.addWidget(self.page_postgame)
        