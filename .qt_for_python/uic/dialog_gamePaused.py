# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_gamePaused.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_dialog_gamePaused(object):
    def setupUi(self, dialog_gamePaused):
        if not dialog_gamePaused.objectName():
            dialog_gamePaused.setObjectName(u"dialog_gamePaused")
        dialog_gamePaused.resize(219, 175)
        self.verticalLayout = QVBoxLayout(dialog_gamePaused)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_gamePaused = QLabel(dialog_gamePaused)
        self.label_gamePaused.setObjectName(u"label_gamePaused")

        self.verticalLayout.addWidget(self.label_gamePaused, 0, Qt.AlignHCenter)

        self.frame_buttons = QFrame(dialog_gamePaused)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.frame_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_buttons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_unPause = QPushButton(self.frame_buttons)
        self.pushButton_unPause.setObjectName(u"pushButton_unPause")

        self.horizontalLayout.addWidget(self.pushButton_unPause)

        self.pushButton_CancelGame = QPushButton(self.frame_buttons)
        self.pushButton_CancelGame.setObjectName(u"pushButton_CancelGame")

        self.horizontalLayout.addWidget(self.pushButton_CancelGame)


        self.verticalLayout.addWidget(self.frame_buttons)


        self.retranslateUi(dialog_gamePaused)

        self.pushButton_unPause.setDefault(True)


        QMetaObject.connectSlotsByName(dialog_gamePaused)
    # setupUi

    def retranslateUi(self, dialog_gamePaused):
        dialog_gamePaused.setWindowTitle(QCoreApplication.translate("dialog_gamePaused", u"Dialog", None))
        self.label_gamePaused.setText(QCoreApplication.translate("dialog_gamePaused", u"Game Paused", None))
        self.pushButton_unPause.setText(QCoreApplication.translate("dialog_gamePaused", u"Resume", None))
        self.pushButton_CancelGame.setText(QCoreApplication.translate("dialog_gamePaused", u"Cancel Game", None))
    # retranslateUi

