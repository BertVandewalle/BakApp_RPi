import sys
sys.path.append('../BakApp_RPi')
from gui.core.json_themes import Themes
from gui.widgets.circular_picture import ScaledCircularPicture
from gui.core.json_settings import Settings
from data_controller import DataController
from data_initializer import DataInitializer
from qt_core import *
import logging
class WinChanceWidget(QWidget):
    def __init__(self,winchance_red):
        super().__init__()
        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items
        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        self.winchance_red = winchance_red
        self.line_width = 20

    def set_value(self,value):
        self.winchance_red = value
        self.repaint()
    
    def paintEvent(self,event):
        # parameters
        margin = self.line_width//2
        red_width = int(self.width()*self.winchance_red)
        breakline_width = 5
        line_height = self.height()//2

        p = QPainter()
        p.begin(self)
        p.setRenderHint(QPainter.Antialiasing)
        
        pen = QPen()
        pen.setWidth(self.line_width)
        pen.setColor(QColor(self.themes['app_color']['red']))
        p.setPen(pen)
        p.drawLine(margin*2,line_height,red_width,line_height)

        pen.setCapStyle(Qt.RoundCap)
        p.setPen(pen)
        p.drawLine(margin,line_height,margin*2,line_height)

        pen.setCapStyle(Qt.FlatCap)
        pen.setColor(QColor(self.themes['app_color']['green']))
        p.setPen(pen)
        p.drawLine(red_width,line_height,self.width()-margin,line_height)

        pen.setCapStyle(Qt.RoundCap)
        p.setPen(pen)
        p.drawLine(self.width()-2*margin,line_height,self.width()-margin,line_height)

        pen.setColor(QColor(self.themes['app_color']['white']))
        pen.setWidth(breakline_width)
        p.setPen(pen)
        p.drawLine(self.width()//2,line_height-2*margin,self.width()//2,line_height+2*margin)

        p.end()

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
        self.widget = WinChanceWidget(0.7)
        self.widget.show() 
        logging.warning("show widget")



if __name__ == '__main__':
    app = MainApp(sys.argv)
    sys.exit(app.exec_())      
                  