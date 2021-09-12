# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_gameCancel.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_dialog_gameCancel(object):
    def setupUi(self, dialog_gameCancel):
        if not dialog_gameCancel.objectName():
            dialog_gameCancel.setObjectName(u"dialog_gameCancel")
        dialog_gameCancel.resize(237, 179)
        self.verticalLayout = QVBoxLayout(dialog_gameCancel)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QTextBrowser(dialog_gameCancel)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setAutoFillBackground(True)
        self.textBrowser.setStyleSheet(u"background-color: transparent;")
        self.textBrowser.setFrameShape(QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QFrame.Plain)

        self.verticalLayout.addWidget(self.textBrowser)

        self.frame_buttons = QFrame(dialog_gameCancel)
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

        self.textBrowser.raise_()
        self.frame_buttons.raise_()

        self.retranslateUi(dialog_gameCancel)

        self.pushButton_no.setDefault(True)


        QMetaObject.connectSlotsByName(dialog_gameCancel)
    # setupUi

    def retranslateUi(self, dialog_gameCancel):
        dialog_gameCancel.setWindowTitle(QCoreApplication.translate("dialog_gameCancel", u"Dialog", None))
        self.textBrowser.setHtml(QCoreApplication.translate("dialog_gameCancel", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Are you sure you want to cancel the current game?</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-inden"
                        "t:0px;\">All progress will be lost.</p></body></html>", None))
        self.pushButton_yes.setText(QCoreApplication.translate("dialog_gameCancel", u"Yes", None))
        self.pushButton_no.setText(QCoreApplication.translate("dialog_gameCancel", u"No, keep playing", None))
    # retranslateUi

