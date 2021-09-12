from game_controller import GameController
from gui.widgets.bottom_button_bar import BottomButtonBar
from data_initializer import DataInitializer
from main_pages import MainPages
from gui.uis.dashboard_widgets.ui_last_game import Ui_lastGame
from qt_core import *
from gui.core.json_settings import Settings
from gui.core.json_themes import Themes
from gui.widgets import *
from gui.uis.pages.ui_main_pages_new import Ui_MainPages
from gui.uis.pages.ui_main_pages import Ui_main_pages



# MAIN WINDOW OBJECT
# ///////////////////////////////////////////////////////////////
class UI_MainWindow(object):
    def setup_ui(self, parent, dti:DataInitializer,gc:GameController):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # SET INITIAL PARAMETERS
        parent.resize(self.settings["startup_size"][0], self.settings["startup_size"][1])
        parent.setMinimumSize(self.settings["minimum_size"][0], self.settings["minimum_size"][1])

        # SET CENTRAL WIDGET
        # Add central widget to app
        # ///////////////////////////////////////////////////////////////
        self.central_widget = QWidget()
        self.central_widget.setStyleSheet(f'''
            font: {self.settings["font"]["text_size"]}pt "{self.settings["font"]["family"]}";
            color: {self.themes["app_color"]["text_foreground"]};
        ''')
        self.central_widget_layout = QVBoxLayout(self.central_widget)
        self.central_widget_layout.setContentsMargins(0,0,0,0)
        
        # LOAD PY WINDOW CUSTOM WIDGET
        # Add inside PyWindow "layout" all Widgets
        # ///////////////////////////////////////////////////////////////
        self.window = PyWindow(
            parent,
            bg_color = self.themes["app_color"]["bg_one"],
            border_color = self.themes["app_color"]["bg_two"],
            text_color = self.themes["app_color"]["white"]
        )
     
        # ADD PY WINDOW TO CENTRAL WIDGET
        self.central_widget_layout.addWidget(self.window)

        # ADD FRAME BOTTOM MENU
        # Add here the custom bottom menu bar
        # ///////////////////////////////////////////////////////////////
        self.bottom_menu_frame = QFrame()

        # BOTTOM MENU LAYOUT
        self.bottom_menu_layout = QHBoxLayout(self.bottom_menu_frame)

        # ADD BOTTOM MENU
        # Add custom bottom menu here
        # ///////////////////////////////////////////////////////////////
        self.bottom_menu = PyBottomMenu(
            parent = self.bottom_menu_frame,
            dark_one = self.themes["app_color"]["dark_one"],
            dark_three = self.themes["app_color"]["dark_three"],
            dark_four = self.themes["app_color"]["dark_four"],
            bg_one = self.themes["app_color"]["bg_one"],
            icon_color = self.themes["app_color"]["icon_color"],
            icon_color_hover = self.themes["app_color"]["icon_hover"],
            icon_color_pressed = self.themes["app_color"]["icon_pressed"],
            icon_color_active = self.themes["app_color"]["icon_active"],
            context_color = self.themes["app_color"]["context_color"],
            text_foreground = self.themes["app_color"]["text_foreground"],
            text_active = self.themes["app_color"]["text_active"]
        )
        self.bottom_menu_layout.addWidget(self.bottom_menu)


        # # ADD FRAME BOTTOM MENU
        # # Add here the custom bottom menu bar
        # # ///////////////////////////////////////////////////////////////
        # self.bottom_button_bar_frame = QFrame()

        # # BOTTOM MENU LAYOUT
        # self.bottom_button_bar_layout = QHBoxLayout(self.bottom_button_bar_frame)

        # # ADD BOTTOM MENU BAR
        # # ///////////////////////////////////////////////////////////////
        # self.bottom_button_bar = BottomButtonBar()
        # self.bottom_button_bar_layout.addWidget(self.bottom_button_bar)
        
        # ADD CONTENT AREA
        # ///////////////////////////////////////////////////////////////
        self.content_area_frame = QFrame()
        self.content_area_layout = QHBoxLayout(self.content_area_frame)

        # IMPORT MAIN PAGES TO CONTENT AREA
        #self.load_pages = Ui_main_pages()
        #self.load_pages.setupUi(self.content_area_frame)
        self.load_pages = MainPages(parent,dti,gc)
        self.content_area_layout.addWidget(self.load_pages)
        # self.last_game_widget = Ui_lastGame()
        # self.last_game_widget.setupUi(self.load_pages.frame_welcome)
       
        # ADD WIDGETS TO "PyWindow"
        # Add here your custom widgets or default widgets
        # ///////////////////////////////////////////////////////////////
        self.window.layout.addWidget(self.content_area_frame)
        #self.window.layout.addWidget(self.bottom_button_bar_frame)
        self.window.layout.addWidget(self.bottom_menu_frame )
        #self.bottom_button_bar_frame.hide()

        # ADD CENTRAL WIDGET AND SET CONTENT MARGINS
        # ///////////////////////////////////////////////////////////////
        parent.setCentralWidget(self.central_widget)