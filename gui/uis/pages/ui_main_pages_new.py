# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagesWbPbym.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from qt_core import *
from gui.widgets import *

class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(1178, 760)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.page_home.setStyleSheet(u"font-size: 14pt")
        self.page_1_layout = QVBoxLayout(self.page_home)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.frame_welcome = QFrame(self.page_home)
        self.frame_welcome.setObjectName(u"frame_welcome")
        self.frame_welcome.setFrameShape(QFrame.StyledPanel)
        self.frame_welcome.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_welcome)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_welcome = QLabel(self.frame_welcome)
        self.label_welcome.setObjectName(u"label_welcome")
        font = QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_welcome.setFont(font)
        self.label_welcome.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_welcome)

        self.last_game_widget = QFrame(self.page_home)
        self.last_game_widget_layout = QHBoxLayout(self.last_game_widget)
        self.page_1_layout.addWidget(self.last_game_widget)


        self.frame_bottom = QFrame(self.page_home)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_bottom)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ranking = QFrame(self.frame_bottom)
        self.ranking.setObjectName(u"ranking")
        self.ranking.setFrameShape(QFrame.StyledPanel)
        self.ranking.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.ranking)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.ranking)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.ranking)

        self.frame_games_today = QFrame(self.frame_bottom)
        self.frame_games_today.setObjectName(u"frame_games_today")
        self.frame_games_today.setFrameShape(QFrame.StyledPanel)
        self.frame_games_today.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_games_today)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.frame_games_today)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)


        self.horizontalLayout.addWidget(self.frame_games_today)


        self.page_1_layout.addWidget(self.frame_bottom)

        self.pages.addWidget(self.page_home)
        self.page_playerSelection = QWidget()
        self.page_playerSelection.setStyleSheet("background: qlineargradient(spread:reflect, x1:1, y1:0.5, x2:0, y2:0.5, stop:0.15 rgba(58, 140, 58, 255), stop:0.5 rgba(255, 255, 225, 255), stop:0.85 rgba(255, 72, 55, 255))")
        self.page_playerSelection.setObjectName(u"page_playerSelection")
        self.page_2_layout = QVBoxLayout(self.page_playerSelection)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.frame_players = QFrame(self.page_playerSelection)
        self.frame_players.setObjectName(u"frame_players")
        self.frame_players.setFrameShape(QFrame.StyledPanel)
        self.frame_players.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_players)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_teamRed = QFrame(self.frame_players)
        self.frame_teamRed.setObjectName(u"frame_teamRed")
        self.frame_teamRed.setFrameShape(QFrame.StyledPanel)
        self.frame_teamRed.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_teamRed)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_playersRed = QFrame(self.frame_teamRed)
        self.frame_playersRed.setObjectName(u"frame_playersRed")
        self.frame_playersRed.setFrameShape(QFrame.StyledPanel)
        self.frame_playersRed.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_playersRed)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_redDef = QFrame(self.frame_playersRed)
        self.frame_redDef.setObjectName(u"frame_redDef")
        self.frame_redDef.setFrameShape(QFrame.StyledPanel)
        self.frame_redDef.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_redDef)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_redDefPic = QLabel(self.frame_redDef)
        self.label_redDefPic.setObjectName(u"label_redDefPic")
        self.label_redDefPic.setMaximumSize(QSize(240, 600))
        self.label_redDefPic.setPixmap(QPixmap(u"../PyOneDark_Qt_Widgets_Modern_GUI-7a58b37247870f5b0425a5c1c633dfdef56e73ae/PyOneDark_Qt_Widgets_Modern_GUI-7a58b37247870f5b0425a5c1c633dfdef56e73ae/gui/images/images/Bert.JPG"))
        self.label_redDefPic.setScaledContents(True)
        self.label_redDefPic.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_redDefPic, 0, Qt.AlignHCenter)

        self.label_redDefName = QLabel(self.frame_redDef)
        self.label_redDefName.setObjectName(u"label_redDefName")
        self.label_redDefName.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_redDefName)


        self.horizontalLayout_6.addWidget(self.frame_redDef)

        self.frame_redOff = QFrame(self.frame_playersRed)
        self.frame_redOff.setObjectName(u"frame_redOff")
        self.frame_redOff.setFrameShape(QFrame.StyledPanel)
        self.frame_redOff.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_redOff)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_redOffPic = QLabel(self.frame_redOff)
        self.label_redOffPic.setObjectName(u"label_redOffPic")
        self.label_redOffPic.setMaximumSize(QSize(240, 600))
        self.label_redOffPic.setPixmap(QPixmap(u"../PyOneDark_Qt_Widgets_Modern_GUI-7a58b37247870f5b0425a5c1c633dfdef56e73ae/PyOneDark_Qt_Widgets_Modern_GUI-7a58b37247870f5b0425a5c1c633dfdef56e73ae/gui/images/images/Bert.JPG"))
        self.label_redOffPic.setScaledContents(True)
        self.label_redOffPic.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_redOffPic, 0, Qt.AlignHCenter)

        self.label_redOffName = QLabel(self.frame_redOff)
        self.label_redOffName.setObjectName(u"label_redOffName")
        self.label_redOffName.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_redOffName)


        self.horizontalLayout_6.addWidget(self.frame_redOff)


        self.verticalLayout_6.addWidget(self.frame_playersRed)

        self.frame_statsRed = QFrame(self.frame_teamRed)
        self.frame_statsRed.setObjectName(u"frame_statsRed")
        self.frame_statsRed.setFrameShape(QFrame.StyledPanel)
        self.frame_statsRed.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_statsRed)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_statsRed = QLabel(self.frame_statsRed)
        self.label_statsRed.setObjectName(u"label_statsRed")

        self.verticalLayout_9.addWidget(self.label_statsRed)


        self.verticalLayout_6.addWidget(self.frame_statsRed)


        self.horizontalLayout_5.addWidget(self.frame_teamRed)

        self.frame_teamGreen = QFrame(self.frame_players)
        self.frame_teamGreen.setObjectName(u"frame_teamGreen")
        self.frame_teamGreen.setFrameShape(QFrame.StyledPanel)
        self.frame_teamGreen.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_teamGreen)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_playersGreen = QFrame(self.frame_teamGreen)
        self.frame_playersGreen.setObjectName(u"frame_playersGreen")
        self.frame_playersGreen.setFrameShape(QFrame.StyledPanel)
        self.frame_playersGreen.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_playersGreen)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_greDef = QFrame(self.frame_playersGreen)
        self.frame_greDef.setObjectName(u"frame_greDef")
        self.frame_greDef.setFrameShape(QFrame.StyledPanel)
        self.frame_greDef.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_greDef)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_greDefPic = QLabel(self.frame_greDef)
        self.label_greDefPic.setObjectName(u"label_greDefPic")
        self.label_greDefPic.setMaximumSize(QSize(240, 600))
        self.label_greDefPic.setPixmap(QPixmap(u"../PyOneDark_Qt_Widgets_Modern_GUI-7a58b37247870f5b0425a5c1c633dfdef56e73ae/PyOneDark_Qt_Widgets_Modern_GUI-7a58b37247870f5b0425a5c1c633dfdef56e73ae/gui/images/images/Bert.JPG"))
        self.label_greDefPic.setScaledContents(True)
        self.label_greDefPic.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_greDefPic, 0, Qt.AlignHCenter)

        self.label_greDefName = QLabel(self.frame_greDef)
        self.label_greDefName.setObjectName(u"label_greDefName")
        self.label_greDefName.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_greDefName)


        self.horizontalLayout_7.addWidget(self.frame_greDef)

        self.frame_greOff = QFrame(self.frame_playersGreen)
        self.frame_greOff.setObjectName(u"frame_greOff")
        self.frame_greOff.setFrameShape(QFrame.StyledPanel)
        self.frame_greOff.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_greOff)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_greOffPic = QLabel(self.frame_greOff)
        self.label_greOffPic.setObjectName(u"label_greOffPic")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_greOffPic.sizePolicy().hasHeightForWidth())
        self.label_greOffPic.setSizePolicy(sizePolicy)
        self.label_greOffPic.setMaximumSize(QSize(240, 600))
        self.label_greOffPic.setPixmap(QPixmap(u"../PyOneDark_Qt_Widgets_Modern_GUI-7a58b37247870f5b0425a5c1c633dfdef56e73ae/PyOneDark_Qt_Widgets_Modern_GUI-7a58b37247870f5b0425a5c1c633dfdef56e73ae/gui/images/images/Bert.JPG"))
        self.label_greOffPic.setScaledContents(True)
        self.label_greOffPic.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_greOffPic, 0, Qt.AlignHCenter)

        self.label_greOffName = QLabel(self.frame_greOff)
        self.label_greOffName.setObjectName(u"label_greOffName")
        self.label_greOffName.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_greOffName)


        self.horizontalLayout_7.addWidget(self.frame_greOff)


        self.verticalLayout_3.addWidget(self.frame_playersGreen)

        self.frame_statsGreen = QFrame(self.frame_teamGreen)
        self.frame_statsGreen.setObjectName(u"frame_statsGreen")
        self.frame_statsGreen.setFrameShape(QFrame.StyledPanel)
        self.frame_statsGreen.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_statsGreen)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_statsGreen = QLabel(self.frame_statsGreen)
        self.label_statsGreen.setObjectName(u"label_statsGreen")

        self.verticalLayout_8.addWidget(self.label_statsGreen)


        self.verticalLayout_3.addWidget(self.frame_statsGreen)


        self.horizontalLayout_5.addWidget(self.frame_teamGreen)


        self.page_2_layout.addWidget(self.frame_players)

        self.pages.addWidget(self.page_playerSelection)
        self.page_ranking = QWidget()
        self.page_ranking.setObjectName(u"page_ranking")
        self.page_ranking.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.page_3_layout = QVBoxLayout(self.page_ranking)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.label_ranking = QLabel(self.page_ranking)
        self.label_ranking.setObjectName(u"label_ranking")
        font1 = QFont()
        font1.setPointSize(16)
        self.label_ranking.setFont(font1)
        self.label_ranking.setAlignment(Qt.AlignCenter)

        self.page_3_layout.addWidget(self.label_ranking)

        self.pages.addWidget(self.page_ranking)
        self.Game = QWidget()
        self.Game.setObjectName(u"Game")
        self.verticalLayout_10 = QVBoxLayout(self.Game)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_game_title = QFrame(self.Game)
        self.frame_game_title.setObjectName(u"frame_game_title")
        self.frame_game_title.setFrameShape(QFrame.StyledPanel)
        self.frame_game_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_game_title)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.frame_game_title)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_8.addWidget(self.label_4, 0, Qt.AlignHCenter)


        self.verticalLayout_10.addWidget(self.frame_game_title)

        self.frame_game_stats = QFrame(self.Game)
        self.frame_game_stats.setObjectName(u"frame_game_stats")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_game_stats.sizePolicy().hasHeightForWidth())
        self.frame_game_stats.setSizePolicy(sizePolicy1)
        self.frame_game_stats.setFrameShape(QFrame.StyledPanel)
        self.frame_game_stats.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_game_stats)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame = QFrame(self.frame_game_stats)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_5)


        self.horizontalLayout_9.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_11.addWidget(self.label_6, 0, Qt.AlignRight)


        self.horizontalLayout_9.addWidget(self.frame_4)


        self.verticalLayout_11.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_game_stats)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_11.addWidget(self.frame_2)


        self.verticalLayout_10.addWidget(self.frame_game_stats)

        self.pages.addWidget(self.Game)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label_welcome.setText(QCoreApplication.translate("MainPages", u"Welcome Back, Friends of the Mighty Bak!", None))
        #self.label.setText(QCoreApplication.translate("MainPages", u"Last Game", None))
        self.label_2.setText(QCoreApplication.translate("MainPages", u"Ranking", None))
        self.label_3.setText(QCoreApplication.translate("MainPages", u"Games Today", None))
        self.label_redDefPic.setText("")
        self.label_redDefName.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.label_redOffPic.setText("")
        self.label_redOffName.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.label_statsRed.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.label_greDefPic.setText("")
        self.label_greDefName.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.label_greOffPic.setText("")
        self.label_greOffName.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.label_statsGreen.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.label_ranking.setText(QCoreApplication.translate("MainPages", u"Empty Page", None))
        self.label_4.setText(QCoreApplication.translate("MainPages", u"Timer", None))
        self.label_5.setText(QCoreApplication.translate("MainPages", u"0", None))
        self.label_6.setText(QCoreApplication.translate("MainPages", u"0", None))
    # retranslateUi

