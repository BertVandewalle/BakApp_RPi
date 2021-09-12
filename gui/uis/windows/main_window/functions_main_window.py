import sys
from qt_core import *
from . ui_main import *

# FUNCTIONS
class MainFunctions():
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    # SET MAIN WINDOW PAGES 
    # ///////////////////////////////////////////////////////////////
    def set_page(self, page):
        self.ui.load_pages.setCurrentWidget(page)

    