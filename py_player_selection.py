from gui.widgets.bottom_button_bar import BottomButtonBar
from gui.widgets.py_winchance import WinChanceWidget
from gui.widgets.circular_picture import ScaledCircularPicture
from gui.widgets.hq_picture import ScaledHQPicture
import logging
from models.player import Player
import sys
from gui.widgets.py_last_game.py_last_game import FootballTableWidget
from gui.core.json_settings import Settings
from gui.core.json_themes import Themes
from data_initializer import DataInitializer
from data_controller import DataController
from qt_core import *


class PyPlayerSelectionWidget(QWidget):
    PLAYER_SPACING = 50
    def __init__(self,players):
        super().__init__()
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
        self.frame_red = QFrame()
        self.layout_red = QVBoxLayout(self.frame_red)
        
        self.frame_gre = QFrame()
        self.layout_gre = QVBoxLayout(self.frame_gre)

        self.frame_center = QFrame()
        self.layout_center = QVBoxLayout(self.frame_center)

        # CENTER FRAME
        # ///////////////////////////////////////////////////////////////
        self.football_table_widget = FootballTableWidget(color=QColor(self.themes['app_color']['white']))
        self.football_table_widget.setMinimumSize(300,300)
        self.winchance_widget = WinChanceWidget(0.5)
        self.winchance_widget.setMinimumSize(300,60)
        self.frame_winchance = QFrame()
        self.layout_winchance = QHBoxLayout(self.frame_winchance)
        self.label_winchance_red = QLabel(text="50%")
        self.label_winchance_gre = QLabel(text="50%")
        self.label_winchance_red.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_winchance_red.setStyleSheet(f"""color:{self.themes['app_color']['red']};
                                                    font:20pt {self.settings['font']['family']}
                                                """)
        self.label_winchance_gre.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_winchance_gre.setStyleSheet(f"""color:{self.themes['app_color']['green']};
                                                    font:20pt {self.settings['font']['family']}
                                                """)

        self.layout_winchance.addWidget(self.label_winchance_red,0,Qt.AlignCenter)
        self.layout_winchance.addWidget(self.label_winchance_gre,0,Qt.AlignCenter)

        # RED FRAME
        # ///////////////////////////////////////////////////////////////
        self.redDef_widget = PlayerPicNameWidget(players[0],"red")
        self.redOff_widget = PlayerPicNameWidget(players[0],"red")

        # GREEN FRAME
        # ///////////////////////////////////////////////////////////////
        self.greDef_widget = PlayerPicNameWidget(players[0],"green")
        self.greOff_widget = PlayerPicNameWidget(players[0],"green")
        

        # ADD WIDGETS TO LAYOUT
        # ///////////////////////////////////////////////////////////////
        self.layout_red.addWidget(self.redDef_widget,0,Qt.AlignRight|Qt.AlignBottom)
        self.layout_red.addSpacing(self.PLAYER_SPACING)
        self.layout_red.addWidget(self.redOff_widget,0,Qt.AlignRight|Qt.AlignTop)

        self.layout_center.addSpacing(100)
        self.layout_center.addWidget(self.football_table_widget,1,Qt.AlignCenter)
        self.layout_center.addSpacing(20)
        self.layout_center.addWidget(self.winchance_widget,0,Qt.AlignCenter)
        self.layout_center.addWidget(self.frame_winchance,Qt.AlignHCenter|Qt.AlignTop)

        self.layout_gre.addWidget(self.greOff_widget,0,Qt.AlignLeft|Qt.AlignBottom)
        self.layout_gre.addSpacing(self.PLAYER_SPACING)
        self.layout_gre.addWidget(self.greDef_widget,0,Qt.AlignLeft|Qt.AlignTop)

        # ADD FRAME BOTTOM MENU
        # Add here the custom bottom menu bar
        # ///////////////////////////////////////////////////////////////
        self.bottom_button_bar_frame = QFrame()

        # BOTTOM MENU LAYOUT
        self.bottom_button_bar_layout = QHBoxLayout(self.bottom_button_bar_frame)

        # ADD BOTTOM MENU BAR
        # ///////////////////////////////////////////////////////////////
        self.bottom_button_bar = BottomButtonBar()
        self.bottom_button_bar_layout.addWidget(self.bottom_button_bar)
        self.bottom_button_bar.add_button('icon_home.svg',"Start Game","right")
        #self.bottom_button_bar_layout.addWidget(self.bottom_button_bar)



        # ADD ALL TO WIDGET LAYOUT
        self.layout_content = QHBoxLayout()
        self.layout_content.addWidget(self.frame_red,1,Qt.AlignRight)
        self.layout_content.addWidget(self.frame_center,0,Qt.AlignCenter)
        self.layout_content.addWidget(self.frame_gre,1,Qt.AlignLeft)

        self.layout_widget = QVBoxLayout()
        self.layout_widget.addLayout(self.layout_content)
        self.layout_widget.addWidget(self.bottom_button_bar_frame)
        self.setLayout(self.layout_widget)
        self.bottom_button_bar_frame.hide()
    # def paintEvent(self,event):
    #     self.redDef_widget.widget_pic.repaint()
    #     self.redOff_widget.widget_pic.repaint()
    #     self.greDef_widget.widget_pic.repaint()
    #     self.greOff_widget.widget_pic.repaint()

class PlayerPicNameWidget(QWidget):
    def __init__(self,player:Player,team:str="red"):
        super().__init__()
        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        if team == "red": self.text_color = self.themes['app_color']['red']
        else: self.text_color = self.themes['app_color']['green']

        self.layout_widget = QVBoxLayout()
        # LABELS
        # ///////////////////////////////////////////////////////////////
        #self.widget_pic = ScaledHQPicture(player.pixMap)
        self.widget_pic = ScaledCircularPicture(player.pixMap,self.text_color)
        #self.widget_pic.setMinimumSize(200,500)
        self.label_name = QLabel(text=f"{player.name}")
        self.label_name.setStyleSheet(f"""color: {self.text_color};
                                                font: 20pt {self.settings['font']['family']};
                                                """)
        # ADD ALL TO WIDGET LAYOUT
        # ///////////////////////////////////////////////////////////////
        self.layout_widget.addWidget(self.widget_pic,0,Qt.AlignHCenter|Qt.AlignBottom)
        self.layout_widget.addWidget(self.label_name,0,Qt.AlignHCenter|Qt.AlignTop)
        self.setLayout(self.layout_widget)

 



# APPLICATION TO TEST WIDGET
# ///////////////////////////////////////////////////////////////
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
        self.widget = PyPlayerSelectionWidget(self.dti.players)
        #self.widget = PlayerPicNameWidget(self.dti.players[0])
        self.widget.show() 
        logging.warning("show widget")



if __name__ == '__main__':
    app = MainApp(sys.argv)
    sys.exit(app.exec_())      
           