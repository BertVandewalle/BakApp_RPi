# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'py_last_game.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_lastGame(object):
    def setupUi(self, lastGame):
        if not lastGame.objectName():
            lastGame.setObjectName(u"lastGame")
        lastGame.resize(400, 300)
        lastGame.setStyleSheet(u"background: white;\n"
"border-radius: 8")
        self.verticalLayout = QVBoxLayout(lastGame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(lastGame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalFrame = QFrame(lastGame)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.horizontalFrame.sizePolicy().hasHeightForWidth())
        self.horizontalFrame.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.horizontalFrame)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_6)

        self.label_5 = QLabel(self.horizontalFrame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.label_4 = QLabel(self.horizontalFrame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.label_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.label_2 = QLabel(self.horizontalFrame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_3 = QLabel(self.horizontalFrame)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout.addWidget(self.horizontalFrame)


        self.retranslateUi(lastGame)

        QMetaObject.connectSlotsByName(lastGame)
    # setupUi

    def retranslateUi(self, lastGame):
        lastGame.setWindowTitle(QCoreApplication.translate("lastGame", u"Form", None))
        self.label.setText(QCoreApplication.translate("lastGame", u"Last Game", None))
        self.label_6.setText(QCoreApplication.translate("lastGame", u"11", None))
        self.label_5.setText(QCoreApplication.translate("lastGame", u"-", None))
        self.label_4.setText(QCoreApplication.translate("lastGame", u"9", None))
        self.label_2.setText(QCoreApplication.translate("lastGame", u"image", None))
        self.label_3.setText(QCoreApplication.translate("lastGame", u"duration", None))
    # retranslateUi

