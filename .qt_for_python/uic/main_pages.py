# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pages.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_main_pages(object):
    def setupUi(self, main_pages):
        if not main_pages.objectName():
            main_pages.setObjectName(u"main_pages")
        main_pages.resize(568, 432)
        self.horizontalLayout = QHBoxLayout(main_pages)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pages = QStackedWidget(main_pages)
        self.pages.setObjectName(u"pages")
        self.page_ranking = QWidget()
        self.page_ranking.setObjectName(u"page_ranking")
        self.label = QLabel(self.page_ranking)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 170, 47, 13))
        self.label_2 = QLabel(self.page_ranking)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 170, 47, 13))
        self.label_3 = QLabel(self.page_ranking)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(290, 170, 47, 13))
        self.label_4 = QLabel(self.page_ranking)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(400, 170, 47, 13))
        self.pages.addWidget(self.page_ranking)
        self.page_playerSelection = QWidget()
        self.page_playerSelection.setObjectName(u"page_playerSelection")
        self.ps_label_redDefPic = QLabel(self.page_playerSelection)
        self.ps_label_redDefPic.setObjectName(u"ps_label_redDefPic")
        self.ps_label_redDefPic.setGeometry(QRect(120, 110, 47, 13))
        self.ps_label_redDefName = QLabel(self.page_playerSelection)
        self.ps_label_redDefName.setObjectName(u"ps_label_redDefName")
        self.ps_label_redDefName.setGeometry(QRect(120, 160, 47, 13))
        self.ps_label_redOffPic = QLabel(self.page_playerSelection)
        self.ps_label_redOffPic.setObjectName(u"ps_label_redOffPic")
        self.ps_label_redOffPic.setGeometry(QRect(120, 270, 47, 13))
        self.ps_label_redOffName = QLabel(self.page_playerSelection)
        self.ps_label_redOffName.setObjectName(u"ps_label_redOffName")
        self.ps_label_redOffName.setGeometry(QRect(110, 320, 47, 13))
        self.ps_label_greOffName = QLabel(self.page_playerSelection)
        self.ps_label_greOffName.setObjectName(u"ps_label_greOffName")
        self.ps_label_greOffName.setGeometry(QRect(350, 130, 47, 13))
        self.ps_label_greOffPic = QLabel(self.page_playerSelection)
        self.ps_label_greOffPic.setObjectName(u"ps_label_greOffPic")
        self.ps_label_greOffPic.setGeometry(QRect(350, 100, 47, 13))
        self.ps_label_greDefPic = QLabel(self.page_playerSelection)
        self.ps_label_greDefPic.setObjectName(u"ps_label_greDefPic")
        self.ps_label_greDefPic.setGeometry(QRect(340, 280, 47, 13))
        self.ps_label_greDefName = QLabel(self.page_playerSelection)
        self.ps_label_greDefName.setObjectName(u"ps_label_greDefName")
        self.ps_label_greDefName.setGeometry(QRect(340, 320, 47, 13))
        self.pages.addWidget(self.page_playerSelection)
        self.page_game = QWidget()
        self.page_game.setObjectName(u"page_game")
        self.verticalLayout_2 = QVBoxLayout(self.page_game)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.game_label_duration = QLabel(self.page_game)
        self.game_label_duration.setObjectName(u"game_label_duration")

        self.verticalLayout_2.addWidget(self.game_label_duration)

        self.frame = QFrame(self.page_game)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.game_frame_red = QFrame(self.frame)
        self.game_frame_red.setObjectName(u"game_frame_red")
        self.game_frame_red.setFrameShape(QFrame.StyledPanel)
        self.game_frame_red.setFrameShadow(QFrame.Raised)
        self.game_label_redScore = QLabel(self.game_frame_red)
        self.game_label_redScore.setObjectName(u"game_label_redScore")
        self.game_label_redScore.setGeometry(QRect(70, 60, 47, 13))

        self.horizontalLayout_4.addWidget(self.game_frame_red)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.game_label_greScore = QLabel(self.frame_2)
        self.game_label_greScore.setObjectName(u"game_label_greScore")
        self.game_label_greScore.setGeometry(QRect(80, 70, 47, 13))

        self.horizontalLayout_4.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.frame)

        self.pages.addWidget(self.page_game)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout = QVBoxLayout(self.page_home)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_welcome = QLabel(self.page_home)
        self.label_welcome.setObjectName(u"label_welcome")
        self.label_welcome.setStyleSheet(u"font: 30pt Arial;\n"
"")
        self.label_welcome.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_welcome)

        self.home_frame_lastGame = QFrame(self.page_home)
        self.home_frame_lastGame.setObjectName(u"home_frame_lastGame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.home_frame_lastGame.sizePolicy().hasHeightForWidth())
        self.home_frame_lastGame.setSizePolicy(sizePolicy)
        self.home_frame_lastGame.setFrameShape(QFrame.StyledPanel)
        self.home_frame_lastGame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.home_frame_lastGame)

        self.home_frame_bottom = QFrame(self.page_home)
        self.home_frame_bottom.setObjectName(u"home_frame_bottom")
        sizePolicy.setHeightForWidth(self.home_frame_bottom.sizePolicy().hasHeightForWidth())
        self.home_frame_bottom.setSizePolicy(sizePolicy)
        self.home_frame_bottom.setFrameShape(QFrame.StyledPanel)
        self.home_frame_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.home_frame_bottom)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_ranking = QFrame(self.home_frame_bottom)
        self.frame_ranking.setObjectName(u"frame_ranking")
        self.frame_ranking.setFrameShape(QFrame.StyledPanel)
        self.frame_ranking.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_ranking)

        self.home_frame_gamesToday = QFrame(self.home_frame_bottom)
        self.home_frame_gamesToday.setObjectName(u"home_frame_gamesToday")
        self.home_frame_gamesToday.setFrameShape(QFrame.StyledPanel)
        self.home_frame_gamesToday.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.home_frame_gamesToday)


        self.verticalLayout.addWidget(self.home_frame_bottom)

        self.pages.addWidget(self.page_home)

        self.horizontalLayout.addWidget(self.pages)


        self.retranslateUi(main_pages)

        self.pages.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(main_pages)
    # setupUi

    def retranslateUi(self, main_pages):
        main_pages.setWindowTitle(QCoreApplication.translate("main_pages", u"Form", None))
        self.label.setText(QCoreApplication.translate("main_pages", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("main_pages", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("main_pages", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("main_pages", u"TextLabel", None))
        self.ps_label_redDefPic.setText(QCoreApplication.translate("main_pages", u"TextLabel", None))
        self.ps_label_redDefName.setText(QCoreApplication.translate("main_pages", u"TextLabel", None))
        self.ps_label_redOffPic.setText(QCoreApplication.translate("main_pages", u"TextLabel", None))
        self.ps_label_redOffName.setText(QCoreApplication.translate("main_pages", u"TextLabel", None))
        self.ps_label_greOffName.setText(QCoreApplication.translate("main_pages", u"TextLabel", None))
        self.ps_label_greOffPic.setText(QCoreApplication.translate("main_pages", u"TextLabel", None))
        self.ps_label_greDefPic.setText(QCoreApplication.translate("main_pages", u"TextLabel", None))
        self.ps_label_greDefName.setText(QCoreApplication.translate("main_pages", u"TextLabel", None))
        self.game_label_duration.setText(QCoreApplication.translate("main_pages", u"TextLabel", None))
        self.game_label_redScore.setText(QCoreApplication.translate("main_pages", u"TextLabel", None))
        self.game_label_greScore.setText(QCoreApplication.translate("main_pages", u"TextLabel", None))
        self.label_welcome.setText(QCoreApplication.translate("main_pages", u"TextLabel", None))
    # retranslateUi

