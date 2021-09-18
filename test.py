
import sys
from gui.widgets.timeline import TimeLineGoal
from game_controller import GameController
from gui.core.json_settings import Settings
from data_controller import DataController
from data_initializer import DataInitializer
from qt_core import *


class testWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._layout = QHBoxLayout(self)
        self.label_test=QLabel("test")
        self._layout.addWidget(self.label_test)

# APPLICATION TO TEST WIDGET
# ///////////////////////////////////////////////////////////////
class _MainApp(QApplication):
    dti = DataInitializer
    def __init__(self, argv):
        super().__init__(argv)
        self.initUI()

    def initUI(self):
        self.widget= testWidget()
        self.widget.show()       

if __name__ == '__main__':
    app = _MainApp(sys.argv)
    sys.exit(app.exec_())      
                  