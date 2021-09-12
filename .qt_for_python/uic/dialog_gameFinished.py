# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_gameFinished.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_dialog_gameFinished(object):
    def setupUi(self, dialog_gameFinished):
        if not dialog_gameFinished.objectName():
            dialog_gameFinished.setObjectName(u"dialog_gameFinished")
        dialog_gameFinished.resize(220, 184)
        self.verticalLayout = QVBoxLayout(dialog_gameFinished)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(dialog_gameFinished)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.frame_buttons = QFrame(dialog_gameFinished)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.frame_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_buttons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_yes = QPushButton(self.frame_buttons)
        self.pushButton_yes.setObjectName(u"pushButton_yes")

        self.horizontalLayout.addWidget(self.pushButton_yes)

        self.pushButton_no = QPushButton(self.frame_buttons)
        self.pushButton_no.setObjectName(u"pushButton_no")

        self.horizontalLayout.addWidget(self.pushButton_no)


        self.verticalLayout.addWidget(self.frame_buttons)


        self.retranslateUi(dialog_gameFinished)

        self.pushButton_yes.setDefault(True)


        QMetaObject.connectSlotsByName(dialog_gameFinished)
    # setupUi

    def retranslateUi(self, dialog_gameFinished):
        dialog_gameFinished.setWindowTitle(QCoreApplication.translate("dialog_gameFinished", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("dialog_gameFinished", u"Game finished?", None))
        self.pushButton_yes.setText(QCoreApplication.translate("dialog_gameFinished", u"Yes", None))
        self.pushButton_no.setText(QCoreApplication.translate("dialog_gameFinished", u"No, cancel last goal", None))
    # retranslateUi

