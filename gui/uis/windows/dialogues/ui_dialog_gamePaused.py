# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_gamePausedYONRYF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from qt_core import *

class Ui_dialog_gamePaused(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(229, 160)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_gamePaused = QLabel(Dialog)
        self.label_gamePaused.setObjectName(u"label_gamePaused")

        self.verticalLayout.addWidget(self.label_gamePaused, 0, Qt.AlignHCenter)

        self.frame_buttons = QFrame(Dialog)
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


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_gamePaused.setText(QCoreApplication.translate("Dialog", u"Game Paused", None))
        self.pushButton_unPause.setText(QCoreApplication.translate("Dialog", u"Resume", None))
        self.pushButton_CancelGame.setText(QCoreApplication.translate("Dialog", u"Cancel Game", None))
    # retranslateUi

