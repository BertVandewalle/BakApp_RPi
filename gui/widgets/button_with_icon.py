import sys
sys.path.append('../BakApp_RPi')

from qt_core import *
from . svg_widget import SVGWidget

class ButtonWithIcon(QWidget):
    def __init__(self,icon_name,text="",color_text="white",color_bg="blue"):
        super().__init__()
        self.icon_name = icon_name
        self.text = text
        self.color_text = color_text
        self.color_bg = color_bg
        self.setMaximumHeight(50)
        self.setMinimumHeight(50)
        self.init_widget()

    def init_widget(self):
        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0,0,0,0)
        
        self.bg = QFrame()
        self.layout_bg = QHBoxLayout(self.bg)
        self.layout_bg.setContentsMargins(-10,0,-10,0)
        
        self.icon = SVGWidget(None,self.icon_name,self.color_text)

        self.icon.setMinimumSize(20,20)
        
        self.label_text = QLabel(text=self.text)
        self.label_text.setStyleSheet(f"""color: {self.color_text};
                                    """)
        self.label_text.setAlignment(Qt.AlignCenter)
        
        self.layout_bg.addWidget(self.icon,0,Qt.AlignVCenter)
        self.layout_bg.addWidget(self.label_text,0,Qt.AlignVCenter)
        self.bg.setStyleSheet(f"""background-color: {self.color_bg};
                                border-radius: 8
                            """)
        self.opacity_effect = QGraphicsOpacityEffect()                    
        self.opacity_effect.setOpacity(0.3)
        self.setGraphicsEffect(self.opacity_effect)
        
        self._layout.addWidget(self.bg)
        self.setLayout(self._layout)

# APPLICATION TO TEST WIDGET
# ///////////////////////////////////////////////////////////////
class MainApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.initUI()
        

    def initUI(self):
        self.button = ButtonWithIcon("icon_home.svg",text="test")
        self.button.show()
        



if __name__ == '__main__':
    app = MainApp(sys.argv)
    sys.exit(app.exec_())      
           