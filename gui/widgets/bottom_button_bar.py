
import sys
sys.path.append('../BakApp_RPi')
from gui.core.json_themes import Themes
from gui.core.json_settings import Settings
from gui.widgets.button_with_icon import ButtonWithIcon

from gui.widgets.py_icon_button import PyIconButton
from qt_core import *

class BottomButtonBar(QWidget):
    def __init__(self):
        super().__init__()
        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items
        self.text_color = self.themes['app_color']['white']
        self.bg_color = self.themes['app_color']['context_color']

        self.setup_ui()

    def setup_ui(self):
        self.bottom_bar_layout = QHBoxLayout(self)
        self.bottom_bar_layout.setContentsMargins(0,0,0,0)
        # ADD BG
        self.bg = QFrame()
        # ADD LAYOUTS
        self._layout = QHBoxLayout(self.bg)
        self._layout.setContentsMargins(0,0,0,0)
        # ADD BG TO LAYOUT
        self.bottom_bar_layout.addWidget(self.bg)

    
    def add_button(self,icon_name,text,position):
        if position == "left": 
            self.button_left = ButtonWithIcon(icon_name,text,self.text_color,self.bg_color)
            self._layout.addWidget(self.button_left,0,Qt.AlignLeft)
        elif position == "center":
            self.button_center = ButtonWithIcon(icon_name,text,self.text_color,self.bg_color)
            self._layout.addWidget(self.button_center,0,Qt.AlignCenter)
        elif position == "right":
            self.button_right = ButtonWithIcon(icon_name,text,self.text_color,self.bg_color)
            self._layout.addWidget(self.button_right,0,Qt.AlignRight)

    

# APPLICATION TO TEST WIDGET
# ///////////////////////////////////////////////////////////////
class _MainApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.initUI()
        

    def initUI(self):
        buttons = [
        {
            "btn_icon" : "icon_home.svg",
            "btn_id" : "btn_search",
            "btn_text" : "Start",
        }]
        self.BottomButtonBar = BottomButtonBar()
        self.BottomButtonBar.add_button("icon_home.svg","Start Game","right")
        self.BottomButtonBar.show()
        



if __name__ == '__main__':
    app = _MainApp(sys.argv)
    sys.exit(app.exec_())      
           