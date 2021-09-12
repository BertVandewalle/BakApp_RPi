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

        self.page_home = HomePage(self._dti)
        self.page_playerSelection = PyPlayerSelectionWidget(self._dti.players)
        self.page_game = GamePage(gc)
        self.page_ranking = QWidget()

        # ADD WIDGETS TO STACK
        # ///////////////////////////////////////////////////////////////
        self.addWidget(self.page_home)
        self.addWidget(self.page_playerSelection)
        self.addWidget(self.page_game)
        self.addWidget(self.page_ranking)
        