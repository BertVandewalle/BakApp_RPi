import sys
sys.path.append('../BakApp_RPi')
from gui.core.json_themes import Themes
from gui.core.json_settings import Settings
from data_controller import DataController
from data_initializer import DataInitializer
from qt_core import *
import logging

# CREATES HIGH QUALITY PIXMAP IRRESPECTIVE OF SCALE (ANTIALIASING)
class ScaledCircularPicture(QWidget):
    def __init__(self,pixMap:QPixmap,borderColor,parent=None):
        super().__init__()
        if parent != None:
            self.setParent(parent)
     
        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        if borderColor == None: self._borderColor = self.themes['app_color']['context_color']
        else: self._borderColor = borderColor
        self._pixMap = pixMap
        self.scaledPix = self._pixMap
        self.border = self.createBorder(self.scaledPix)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(sizePolicy)
        self.repaint()

    def setPixmap(self,pixMap):
        self._pixMap = pixMap
        self.repaint()

    def paintEvent(self,event):
        p = QPainter()
        p.begin(self)
        p.setRenderHint(QPainter.Antialiasing)
        self.border = self.createBorder(self.scaledPix)
        self.border = self.border.scaled(self.size(),Qt.KeepAspectRatio, transformMode = Qt.SmoothTransformation)
        self.scaledPix = self.circleImage(self._pixMap.scaled(self.border.size()*0.9, Qt.KeepAspectRatio, transformMode = Qt.SmoothTransformation))
        originPic = QPoint(int((self.width()-self.scaledPix.width())/2),
                     int((self.height()-self.scaledPix.height())/2))
        originBorder = QPoint(int((self.width()-self.border.width())/2),
                     int((self.height()-self.border.height())/2))
        
        p.drawPixmap(originBorder,self.border)
        p.drawPixmap(originPic, self.scaledPix)
        p.end()

    def sizeHint(self):
        return QSize(int(self.border.width()),int(self.border.height()))

    def heightForWidth(self, width):
        return width * int(self.border.height()/self.border.width())




    def circleImage(self,pixmap:QPixmap):
        size = min(pixmap.width(),pixmap.height())
        target = QPixmap(size,size)
        target.fill(Qt.transparent)
        p = QPainter(target)
        p.setRenderHint(QPainter.Antialiasing)
        path = QPainterPath()
        path.addEllipse(0,0,size,size)
        p.setClipPath(path)
        sourceRect = QRect(0,0,size,size)
        sourceRect.moveCenter(pixmap.rect().center())
        p.drawPixmap(target.rect(), pixmap, sourceRect)
        p.end()

        return target

    def createBorder(self,pixmap:QPixmap):
        size = int(min(pixmap.width(),pixmap.height())*1.10)
        source = QPixmap(size,size)
        source.fill(QColor(self._borderColor))
        target = self.circleImage(source)
        return target

    def setPicture(self,pixmap:QPixmap):
        self._pixMap = pixmap
        self.repaint()

        


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
        self.widget = ScaledCircularPicture(self.dti.players[1].pixMap)
        self.widget.show() 
        logging.warning("show widget")



if __name__ == '__main__':
    app = MainApp(sys.argv)
    sys.exit(app.exec_())      
                  