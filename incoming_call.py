# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'incoming_callQUKhwM.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_IncomingScreen(object):
    def setupUi(self, IncomingScreen):
        if not IncomingScreen.objectName():
            IncomingScreen.setObjectName(u"IncomingScreen")
        IncomingScreen.setWindowModality(Qt.ApplicationModal)
        IncomingScreen.resize(391, 267)
        IncomingScreen.setCursor(QCursor(Qt.ArrowCursor))
        IncomingScreen.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	margin: 0;\n"
"	padding: 0;\n"
"	color: rgb(2, 27, 61);\n"
"}\n"
"#acceptBtn{\n"
"	background-color: rgba(0,255,0);\n"
"	border: 1px solid rgb(0, 255, 0);\n"
"}\n"
"#acceptBtn:hover, #discardBtn:hover{\n"
"	background-color: transparent;\n"
"}\n"
"#discardBtn{\n"
"	background-color: rgb(255, 58, 23);\n"
"	border: 1px solid rgb(255, 58, 23);\n"
"}\n"
"QPushButton{\n"
"	border-radius: 17px;\n"
"}\n"
"#header{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(71, 122, 150, 255), stop:0.299435 rgba(36, 50, 121, 255), stop:0.7 rgba(64, 173, 156, 255), stop:1 rgba(31, 43, 103, 255));\n"
"	border-bottom: 1px solid #eee;\n"
"}\n"
"#bodyContainer{\n"
"	border: 1px solid qlineargradient(spread:repeat, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(199, 215, 226, 255), stop:1 rgba(102, 142, 255, 255));\n"
"	border-top: none;\n"
"}")
        self.verticalLayout = QVBoxLayout(IncomingScreen)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(IncomingScreen)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.header)

        self.bodyContainer = QWidget(IncomingScreen)
        self.bodyContainer.setObjectName(u"bodyContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bodyContainer.sizePolicy().hasHeightForWidth())
        self.bodyContainer.setSizePolicy(sizePolicy)
        self.informLabel = QLabel(self.bodyContainer)
        self.informLabel.setObjectName(u"informLabel")
        self.informLabel.setGeometry(QRect(0, 20, 391, 28))
        font = QFont()
        font.setFamily(u"Noto Sans")
        font.setPointSize(13)
        self.informLabel.setFont(font)
        self.informLabel.setAlignment(Qt.AlignCenter)
        self.discardBtn = QPushButton(self.bodyContainer)
        self.discardBtn.setObjectName(u"discardBtn")
        self.discardBtn.setGeometry(QRect(251, 184, 100, 34))
        font1 = QFont()
        font1.setFamily(u"Noto Sans")
        font1.setPointSize(13)
        font1.setBold(False)
        font1.setWeight(50)
        self.discardBtn.setFont(font1)
        self.discardBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.acceptBtn = QPushButton(self.bodyContainer)
        self.acceptBtn.setObjectName(u"acceptBtn")
        self.acceptBtn.setGeometry(QRect(40, 184, 100, 34))
        self.acceptBtn.setFont(font1)
        self.acceptBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.bodyContainer)


        self.retranslateUi(IncomingScreen)

        QMetaObject.connectSlotsByName(IncomingScreen)
    # setupUi

    def retranslateUi(self, IncomingScreen):
        self.informLabel.setText(QCoreApplication.translate("IncomingScreen", u"Incoming Call from Extension #2343", None))
        self.discardBtn.setText(QCoreApplication.translate("IncomingScreen", u"DISCARD", None))
        self.acceptBtn.setText(QCoreApplication.translate("IncomingScreen", u"ACCEPT", None))
        pass
    # retranslateUi

