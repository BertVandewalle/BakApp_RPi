# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from key_functions import keyPressEventHandler
from stat_calculations import calculate_winchance_red
import sys
import os
from gui import widgets
#from player_selection import PlayerSelection
from data_controller import DataController
from button_controller import ButtonController
from game_controller import GameController
from gui.core.functions import Functions
from gui.uis.windows.main_window.functions_main_window import *


# IMPORT QT MODULES
from qt_core import *

# IMPORT DATA MODELS
from models import *

# IMPORT DATA SETUP
from data_initializer import *

# IMPORT SETTINGS
from gui.core.json_settings import Settings

# IMPORT WINDOWS
from gui.uis.windows.main_window import *
from gui.uis.windows.dialogues import *

# IMPORT CUSTOM WIDGETS
from gui.widgets import *

# ADJUST QT FONT DPI FOR HIGHT SCALE
# ///////////////////////////////////////////////////////////////


# MAIN APPLICATION 
# ///////////////////////////////////////////////////////////////
class MainApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.setAttribute(Qt.AA_DisableHighDpiScaling)
        try: 
            if str(argv[1]) == "f":
                os.environ["QT_FONT_DPI"] = "64"
                self.fullscreen = 1
            else:
                os.environ["QT_FONT_DPI"] = "96"
                self.fullscreen = 0
        except: 
            self.fullscreen = 0
            os.environ["QT_FONT_DPI"] = "96"
 

        self.main_window = None

        # Initialize settings
        settings = Settings()
        self.settings = settings.items

        # Initialize data controller
        self.dataController = DataController()

        # Initialize buttoncontroller
        self.btc = ButtonController()

        # Initialize data
        self.dataInitializer = DataInitializer(self.dataController,self.settings,self.setupUI)

  
       
    def setupUI(self):
        # Initialize gameobject
        if self.main_window != None:
            self.main_window.hide()
            self.main_window.ui.load_pages.setup()
            self.main_window.show()
        else:
            self.gc = GameController(self.dataInitializer)
            # create main window
            self.main_window = MainWindow(self.btc,self,self.dataInitializer)
            if self.fullscreen: self.main_window.showFullScreen()
            else: self.main_window.show()

            # create game paused dialog
            self.game_pause_dialog = GamePauseDialog(self.btc)
            # create game cancel dialog
            self.game_cancel_dialog = GameCancelDialog(self.btc)
            # create game finish dialog
            self.game_finish_dialog = GameFinishDialog(self.btc)

        self.initStateMachine()



    def initStateMachine(self):
        self.stateMachine = QStateMachine()

        # Definitions of objects used by stateMachine
        # Define States
        self.state_View_Home = QState()
        
        self.state_View_PlayerSelection = QState()
        
        self.state_Enter_PlayerSelection = QState()
        self.state_Enter_PlayerSelection_Invalid = QState(self.state_Enter_PlayerSelection)
        self.state_Enter_PlayerSelection_Valid = QState(self.state_Enter_PlayerSelection)
        self.state_Enter_PlayerSelection.setInitialState(self.state_Enter_PlayerSelection_Invalid)

        self.state_Game = QState()
        self.state_Game_Running = QState(self.state_Game)
        self.state_Game_Paused = QState(self.state_Game)
        self.state_Game.setInitialState(self.state_Game_Running)

        self.state_Game_Paused_UnPauseSelected = QState(self.state_Game_Paused)
        self.state_Game_Paused_CancelSelected = QState(self.state_Game_Paused)
        self.state_Game_Paused_CancelDialog = QState(self.state_Game_Paused)
        self.state_Game_Paused.setInitialState(self.state_Game_Paused_UnPauseSelected)

        self.state_Game_Paused_CancelDialog_yesSelected = QState(self.state_Game_Paused_CancelDialog)
        self.state_Game_Paused_CancelDialog_noSelected = QState(self.state_Game_Paused_CancelDialog)
        self.state_Game_Paused_CancelDialog.setInitialState(self.state_Game_Paused_CancelDialog_noSelected)

        self.state_Game_FinishDialog = QState(self.state_Game)
        self.state_Game_FinishDialog_yesSelected = QState(self.state_Game_FinishDialog)
        self.state_Game_FinishDialog_noSelected = QState(self.state_Game_FinishDialog)
        self.state_Game_FinishDialog_cancelling = QState(self.state_Game_FinishDialog)
        self.state_Game_Saving = QState(self.state_Game)
        self.state_Game_FinishDialog.setInitialState(self.state_Game_FinishDialog_yesSelected)

        self.state_Game_PostGame = QState(self.state_Game)



        self.state_View_Ranking = QState()

        # Add State transitions
        self.state_View_Home.addTransition(self.btc.button_7.clicked,self.state_View_PlayerSelection)
        self.state_View_PlayerSelection.addTransition(self.btc.button_5.clicked,self.state_View_Home)
        self.state_View_PlayerSelection.addTransition(self.btc.button_6.clicked,self.state_Enter_PlayerSelection)
        self.state_View_PlayerSelection.addTransition(self.btc.button_7.clicked,self.state_View_Ranking)
        self.state_View_Ranking.addTransition(self.btc.button_5.clicked,self.state_View_PlayerSelection)
        self.state_Enter_PlayerSelection.addTransition(self.btc.button_6.clicked,self.state_View_PlayerSelection)
        self.state_Enter_PlayerSelection_Invalid.addTransition(self.gc.validSelection.clicked,self.state_Enter_PlayerSelection_Valid)
        self.state_Enter_PlayerSelection_Valid.addTransition(self.gc.invalidSelection.clicked,self.state_Enter_PlayerSelection_Invalid)
        self.state_Enter_PlayerSelection_Valid.addTransition(self.btc.button_7.clicked,self.state_Game)


        self.state_Game_Running.addTransition(self.btc.button_6.clicked,self.state_Game_Paused)
        self.state_Game_Paused_UnPauseSelected.addTransition(self.btc.button_6.clicked,self.state_Game_Running)
        self.state_Game_Paused_UnPauseSelected.addTransition(self.btc.button_7.clicked,self.state_Game_Paused_CancelSelected)
        self.state_Game_Paused_CancelSelected.addTransition(self.btc.button_5.clicked,self.state_Game_Paused_UnPauseSelected)
        self.state_Game_Paused_CancelSelected.addTransition(self.btc.button_6.clicked,self.state_Game_Paused_CancelDialog)

        self.state_Game_Paused_CancelDialog_noSelected.addTransition(self.btc.button_5.clicked,self.state_Game_Paused_CancelDialog_yesSelected)
        self.state_Game_Paused_CancelDialog_noSelected.addTransition(self.btc.button_6.clicked,self.state_Game_Paused)
        self.state_Game_Paused_CancelDialog_yesSelected.addTransition(self.btc.button_7.clicked,self.state_Game_Paused_CancelDialog_noSelected)
        self.state_Game_Paused_CancelDialog_yesSelected.addTransition(self.btc.button_6.clicked,self.state_View_Home)

        self.state_Game_Running.addTransition(self.gc.finished.clicked,self.state_Game_FinishDialog)
        self.state_Game_FinishDialog_yesSelected.addTransition(self.btc.button_7.clicked,self.state_Game_FinishDialog_noSelected)
        self.state_Game_FinishDialog_yesSelected.addTransition(self.btc.button_6.clicked,self.state_Game_Saving)
        self.state_Game_FinishDialog_noSelected.addTransition(self.btc.button_5.clicked,self.state_Game_FinishDialog_yesSelected)
        self.state_Game_FinishDialog_noSelected.addTransition(self.btc.button_6.clicked,self.state_Game_FinishDialog_cancelling)
        self.state_Game_FinishDialog_cancelling.addTransition(self.gc.timer.timeout,self.state_Game_Running)
        
        self.state_Game_Saving.addTransition(self.dataInitializer.playersSetupFinished,self.state_View_Home)




        # Signal connections
        self.state_View_Home.entered.connect(lambda: self.main_window.ui.bottom_menu.select_only_one("btn_home")) 
        self.state_View_Home.entered.connect(lambda: MainFunctions.set_page(self.main_window, self.main_window.ui.load_pages.page_home)) 
        
        self.state_View_PlayerSelection.entered.connect(lambda: print("enter playerselection view"))
        self.state_View_PlayerSelection.entered.connect(lambda: self.main_window.ui.bottom_menu.select_only_one("btn_widgets")) 
        self.state_View_PlayerSelection.entered.connect(lambda: MainFunctions.set_page(self.main_window, self.main_window.ui.load_pages.page_playerSelection))
        self.state_View_PlayerSelection.entered.connect(self.main_window.initPlayerSelectionPage)

        self.state_Enter_PlayerSelection.entered.connect(lambda: self.main_window.ui.bottom_menu.select_only_one("btn_widgets")) 
        self.state_Enter_PlayerSelection.entered.connect(lambda: MainFunctions.set_page(self.main_window, self.main_window.ui.load_pages.page_playerSelection))
        self.state_Enter_PlayerSelection.entered.connect(self.main_window.initPlayerSelectionButtonConnections)
        self.state_Enter_PlayerSelection.entered.connect(self.main_window.ui.bottom_menu_frame.hide)
        self.state_Enter_PlayerSelection.entered.connect(self.main_window.ui.load_pages.page_playerSelection.bottom_button_bar_frame.show)

        self.state_Enter_PlayerSelection_Valid.entered.connect(lambda: self.main_window.ui.load_pages.page_playerSelection.bottom_button_bar.button_right.opacity_effect.setOpacity(1))
        self.state_Enter_PlayerSelection_Invalid.entered.connect(lambda: self.main_window.ui.load_pages.page_playerSelection.bottom_button_bar.button_right.opacity_effect.setOpacity(0.2))

        self.state_Enter_PlayerSelection.exited.connect(self.main_window.ui.bottom_menu_frame.show)
        self.state_Enter_PlayerSelection.exited.connect(self.main_window.ui.load_pages.page_playerSelection.bottom_button_bar_frame.hide)
        self.state_Enter_PlayerSelection.exited.connect(self.main_window.disconnectPlayerButtons)

        self.state_Game.entered.connect(lambda: MainFunctions.set_page(self.main_window, self.main_window.ui.load_pages.page_game))
        self.state_Game.entered.connect(self.main_window.startNewGame)
        self.state_Game.entered.connect(self.main_window.ui.load_pages.page_game.updateScores)
        self.state_Game.entered.connect(self.main_window.ui.bottom_menu.hide)
        self.state_Game.entered.connect(self.main_window.ui.load_pages.page_game.initWidgets)
        self.state_Game.exited.connect(self.main_window.ui.bottom_menu.show)
        self.state_Game.exited.connect(self.gc.endGame)
        self.state_Game.exited.connect(self.main_window.ui.load_pages.page_game.widget_timeline.endGame)

        self.state_Game_Running.entered.connect(self.main_window.initGameButtonConnections)
        self.state_Game_Running.entered.connect(self.gc.start)
        self.state_Game_Running.entered.connect(self.main_window.ui.load_pages.page_game.widget_timeline.start)


        self.state_Game_Running.exited.connect(self.main_window.disconnectPlayerButtons
        )
        self.state_Game_Running.exited.connect(lambda: self.btc.button_5.clicked.disconnect(self.main_window.deleteGoal))
        self.state_Game_Running.exited.connect(self.main_window.ui.load_pages.page_game.widget_timeline.pause)


        self.state_Game_Paused.entered.connect(self.game_pause_dialog.show)
        self.state_Game_Paused.entered.connect(self.gc.pause)
        
        self.state_Game_Paused.entered.connect(self.game_pause_dialog.setFocus)
        self.state_Game_Paused.exited.connect(self.game_pause_dialog.close)
        #self.state_Game_Paused.exited.connect(self.gc.start)

        self.state_Game_Paused_UnPauseSelected.entered.connect(self.game_pause_dialog.ui.pushButton_unPause.setFocus)
        self.state_Game_Paused_CancelSelected.entered.connect(self.game_pause_dialog.ui.pushButton_CancelGame.setFocus)
        self.state_Game_Paused_CancelDialog.entered.connect(self.game_cancel_dialog.show)
        self.state_Game_Paused_CancelDialog.entered.connect(self.game_cancel_dialog.setFocus)
        self.state_Game_Paused_CancelDialog.exited.connect(self.game_cancel_dialog.close)
        self.state_Game_Paused_CancelDialog_noSelected.entered.connect(self.game_cancel_dialog.ui.pushButton_no.setFocus)
        self.state_Game_Paused_CancelDialog_yesSelected.entered.connect(self.game_cancel_dialog.ui.pushButton_yes.setFocus)

        self.state_Game_FinishDialog.entered.connect(self.game_finish_dialog.show)
        self.state_Game_FinishDialog.entered.connect(self.game_finish_dialog.setFocus)
        self.state_Game_FinishDialog.entered.connect(self.gc.pause)
        self.state_Game_FinishDialog.exited.connect(self.game_finish_dialog.close)
        self.state_Game_FinishDialog_yesSelected.entered.connect(self.game_finish_dialog.ui.pushButton_yes.setFocus)
        self.state_Game_FinishDialog_noSelected.entered.connect(self.game_finish_dialog.ui.pushButton_no.setFocus)
        self.state_Game_FinishDialog_cancelling.entered.connect(self.main_window.deleteGoal)

        self.state_Game_Saving.entered.connect(lambda: self.dataController.postGame(self.gc.game))

        #self.state_Game_Paused.entered.connect(self.game_pause_dialog.showFullScreen)

        self.state_View_Ranking.entered.connect(lambda: self.main_window.ui.bottom_menu.select_only_one("btn_add_user")) 
        self.state_View_Ranking.entered.connect(lambda: MainFunctions.set_page(self.main_window, self.main_window.ui.load_pages.page_ranking))

        # Add States to StateMachine
        self.stateMachine.addState(self.state_View_Home)
        self.stateMachine.addState(self.state_View_PlayerSelection)
        self.stateMachine.addState(self.state_Enter_PlayerSelection)
        self.stateMachine.addState(self.state_View_Ranking)
        self.stateMachine.addState(self.state_Game)

        self.stateMachine.setInitialState(self.state_View_Home)
        
        # Start State machine
        self.stateMachine.start()
      
# MAIN WINDOW
# ///////////////////////////////////////////////////////////////
class MainWindow(QMainWindow):

    def __init__(self,buttonController:ButtonController,app:MainApp,dti:DataInitializer):
        super().__init__()
        self.btc = buttonController
        self.dti = dti
        self.app = app
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self,dti=self.dti,gc=self.app.gc)
        self.initializeUI()
        
    def keyPressEvent(self,event):
        keyPressEventHandler(app.btc,event=event)
        

    def initializeUI(self):
        settings = Settings()
        self.settings = settings.items
         # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(self.settings["app_name"])
        
        # # REMOVE TITLE BAR
        # # ///////////////////////////////////////////////////////////////
        # if self.settings["custom_title_bar"]:
        #     self.setWindowFlag(Qt.FramelessWindowHint)
        #     self.setAttribute(Qt.WA_TranslucentBackground)

        # ADD BOTTOM MENUS
        # ///////////////////////////////////////////////////////////////
        self.bottom_menus = [
            {
                "btn_icon" : "icon_home.svg",
                "btn_id" : "btn_home",
                "is_active" : True
            },
            {
                "btn_icon" : "icon_player.svg",
                "btn_id" : "btn_widgets",
                "is_active" : False
            },
            {
                "btn_icon" : "icon_trophy.svg",
                "btn_id" : "btn_add_user",
                "is_active" : False
            }
        ]

        # BOTTOM MENUS / GET SIGNALS WHEN BOTTOM MENU BTN IS CLICKED / RELEASED
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.bottom_menu.add_menus(self.bottom_menus)
        self.ui.bottom_menu.menu.is_active()




        self.initPlayerSelectionPage()
        # self.app.gc.timeUpdate.connect(self.ui.load_pages.game_label_duration.setText)
        #self.app.gc.scoreUpdate.connect(self.updateScore)
        self.initGameScreen()

    def initPlayerSelectionPage(self):
        self.app.gc.initPlayers()
        self.updatePlayerSelectionPage()

    def selectPlayer(self,position):
        self.app.gc.togglePlayer(position)
        self.updatePlayerSelectionPage()
        self.checkSelectionValidity()
    
    def checkSelectionValidity(self):
        if len(self.app.gc.game.players) == len(set(self.app.gc.game.players)):
            self.app.gc.validSelection.clicked.emit()
        else:
            self.app.gc.invalidSelection.clicked.emit()

    def updatePlayerSelectionPage(self):
        self.ui.load_pages.page_playerSelection.redDef_widget.widget_pic.setPixmap(self.app.gc.game.players[0].pixMap)
        self.ui.load_pages.page_playerSelection.redOff_widget.widget_pic.setPixmap(self.app.gc.game.players[1].pixMap)
        self.ui.load_pages.page_playerSelection.greDef_widget.widget_pic.setPixmap(self.app.gc.game.players[2].pixMap)
        self.ui.load_pages.page_playerSelection.greOff_widget.widget_pic.setPixmap(self.app.gc.game.players[3].pixMap)

        self.ui.load_pages.page_playerSelection.redDef_widget.label_name.setText(self.app.gc.game.players[0].name)
        self.ui.load_pages.page_playerSelection.redOff_widget.label_name.setText(self.app.gc.game.players[1].name)
        self.ui.load_pages.page_playerSelection.greDef_widget.label_name.setText(self.app.gc.game.players[2].name)
        self.ui.load_pages.page_playerSelection.greOff_widget.label_name.setText(self.app.gc.game.players[3].name)

        winchance_red = calculate_winchance_red(self.app.gc.game.duos[0],self.app.gc.game.duos[1])
        print(winchance_red)
        print(self.app.gc.game.duos[0].def_player.name)
        print(self.app.gc.game.duos[0].off_player.name)

        print(self.app.gc.game.duos[1].winrate)

        self.ui.load_pages.page_playerSelection.winchance_widget.set_value(winchance_red)
        self.ui.load_pages.page_playerSelection.label_winchance_red.setText(f"{round(winchance_red*100)}%")
        self.ui.load_pages.page_playerSelection.label_winchance_gre.setText(f"{round(100-(winchance_red*100))}%")

    def initPlayerSelectionButtonConnections(self):
        self.btc.button_1.clicked.connect(lambda: self.selectPlayer(0))
        self.btc.button_2.clicked.connect(lambda: self.selectPlayer(1))
        self.btc.button_3.clicked.connect(lambda: self.selectPlayer(2))
        self.btc.button_4.clicked.connect(lambda: self.selectPlayer(3))

    def disconnectPlayerButtons(self):
        self.btc.button_1.clicked.disconnect()
        self.btc.button_2.clicked.disconnect()
        self.btc.button_3.clicked.disconnect()
        self.btc.button_4.clicked.disconnect()

    def startNewGame(self):
        print("Starting New Game")
        self.app.gc.reset()
        self.app.gc.start()

    def initGameScreen(self):
        
        self.ui.load_pages.page_game.updateScores()

    def initGameButtonConnections(self):
        self.btc.button_1.clicked.connect(lambda: self.addGoal(0))
        self.btc.button_2.clicked.connect(lambda: self.addGoal(1))
        self.btc.button_3.clicked.connect(lambda: self.addGoal(2))
        self.btc.button_4.clicked.connect(lambda: self.addGoal(3))
        self.btc.button_5.clicked.connect(self.deleteGoal)

    def addGoal(self,pos):
        app.gc.addGoal(app.gc.game.players[pos])
        if pos < 2:
            self.ui.load_pages.page_game.widget_timeline.addGoal(app.gc.game.players[pos],"red",app.gc.game.duration_precise)
        else:
            self.ui.load_pages.page_game.widget_timeline.addGoal(app.gc.game.players[pos],"green",app.gc.game.duration_precise)
        self.ui.load_pages.page_game.updateScores()

    def deleteGoal(self):
        app.gc.deleteLastGoal()
        self.ui.load_pages.page_game.widget_timeline.deleteLastGoal()
        self.ui.load_pages.page_game.updateScores()

    

    def updateScore(self):
        # self.ui.load_pages.game_label_redScore.setText(str(app.gc.game.scoreRed))
        # self.ui.load_pages.game_label_greScore.setText(str(app.gc.game.scoreGre))
        pass


# GAME PAUSED DIALOG
# ///////////////////////////////////////////////////////////////
class GamePauseDialog(QDialog):
    def __init__(self,buttonController):
        super().__init__()
        self.btc = buttonController
        self.ui = Ui_dialog_gamePaused()
        self.ui.setupUi(self)

    def keyPressEvent(self,event):
        keyPressEventHandler(self.btc,event)
# GAME CANCEL DIALOG
# ///////////////////////////////////////////////////////////////
class GameCancelDialog(QDialog):
    def __init__(self,buttonController):
        super().__init__()
        self.btc = buttonController
        self.ui = Ui_dialog_gameCancel()
        self.ui.setupUi(self)

    def keyPressEvent(self,event):
        keyPressEventHandler(self.btc,event)

# GAME FINISHED DIALOG
# ///////////////////////////////////////////////////////////////
class GameFinishDialog(QDialog):
    def __init__(self,buttonController):
        super().__init__()
        self.btc = buttonController
        self.ui = Ui_dialog_gameFinished()
        self.ui.setupUi(self)

    def keyPressEvent(self,event):
        keyPressEventHandler(self.btc,event)
                


if __name__ == "__main__":
    app = MainApp(sys.argv)
    sys.exit(app.exec_())