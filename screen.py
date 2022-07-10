# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'screenuRbRka.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1280, 720)
        MainWindow.setMaximumSize(QSize(1280, 720))
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	margin: 0;\n"
"	padding: 0;\n"
"	color: #eee;\n"
"}\n"
"#MainWindow, #centralwidget{\n"
"	border-radius: 8px;\n"
"}\n"
"#body_container{\n"
"	border-bottom-left-radius: 8px;\n"
"	border-bottom-right-radius: 8px;\n"
"}\n"
"#sidebar_widget, #sidebar_sub_widget{\n"
"	border-bottom-left-radius: 8px;\n"
"}\n"
"#content_widget, #footer_container{\n"
"	border-bottom-right-radius: 8px;\n"
"}\n"
"#content_widget{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.45, x2:0.95, y2:1, stop:0 rgba(37, 52, 120, 255), stop:0.35 rgba(46, 64, 123, 255), stop:0.75 rgba(25, 36, 95, 255), stop:1 rgba(31, 61, 111, 255));\n"
"}\n"
"#sidebar_sub_widget{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(24, 47, 94, 255), stop:1 rgba(22, 35, 93, 255));\n"
"}\n"
"#sidebar_sub_widget QPushButton{\n"
"	text-align: left;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-le"
                        "ft-radius: 10px;\n"
"}\n"
"#center_menu_sub, #right_menu_sub_container, #footer_container{\n"
"	background-color: #233972;\n"
"}\n"
"#frame_more_menu, #frame_right_menu{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(31, 42, 97, 255), stop:0.4 rgba(19, 32, 85, 255), stop:0.7 rgba(18, 44, 100, 255), stop:1 rgba(17, 39, 93, 255));\n"
"	border-radius: 10px;\n"
"}\n"
"#popup_notification_sub_container{\n"
"	background-color: qlineargradient(spread:pad, x1:0.149847, y1:0.028, x2:0.506, y2:0.865909, stop:0.0734463 rgba(27, 51, 106, 255), stop:0.344633 rgba(34, 84, 114, 255), stop:0.751412 rgba(27, 51, 106, 255));\n"
"	border: 1px solid qlineargradient(spread:repeat, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(70, 124, 160, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border-right: 10px solid qlineargradient(spread:repeat, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(70, 124, 160, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"#header_container{\n"
"	background-color: qlineargrad"
                        "ient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(71, 122, 150, 255), stop:0.299435 rgba(36, 50, 121, 255), stop:0.7 rgba(64, 173, 156, 255), stop:1 rgba(31, 43, 103, 255));\n"
"	border-bottom: 1px solid #eee;\n"
"	border-top-left-radius: 8px;\n"
"	border-top-right-radius: 8px;\n"
"}\n"
"#zonesContainer, #fieldContainer, #scheduleContainer, #recordContainer, #cameraContainer{\n"
"	border: 1px solid #eee;\n"
"	border-radius: 4px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.149847, y1:0.028, x2:0.506, y2:0.865909, stop:0.0734463 rgba(27, 51, 106, 255), stop:0.344633 rgba(34, 84, 114, 255), stop:0.751412 rgba(27, 51, 106, 255));\n"
"}\n"
"#zonesContainer:hover, #fieldContainer:hover, #scheduleContainer:hover, #recordContainer:hover, #cameraContainer:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.083, y1:0.177, x2:0.762, y2:0.534, stop:0 rgba(192, 210, 218, 255), stop:0.19774 rgba(125, 202, 194, 255), stop:0.59322 rgba(95, 145, 182, 255), stop:1 rgba(125, 202, 194, 255));\n"
"}\n"
""
                        "#btnHome, #btnDataAnalysis, #btnReports{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(31, 42, 97, 255), stop:0.4 rgba(19, 32, 85, 255), stop:0.7 rgba(18, 44, 100, 255), stop:1 rgba(17, 39, 93, 255));\n"
"	border: 1px solid qlineargradient(spread:repeat, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(63, 127, 157, 255), stop:1 rgba(102, 142, 255, 255));\n"
"	border-right: none;\n"
"}\n"
"#btnHome:hover, #btnDataAnalysis:hover, #btnReports:hover, #btnSettings:hover, #btnInfo:hover, #btnHelp:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(82, 124, 148, 255), stop:0.457627 rgba(46, 78, 121, 255), stop:0.542373 rgba(36, 66, 113, 255), stop:0.79096 rgba(42, 98, 123, 255), stop:1 rgba(125, 164, 203, 255));\n"
"}\n"
"#btnSettings, #btnInfo, #btnHelp{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(31, 42, 97, 255), stop:0.4 rgba(19, 32, 85, 255), stop:0.7 rgba(18, 44, 100, 255), stop:1 rgba(1"
                        "7, 39, 93, 255));\n"
"	border: 1px solid qlineargradient(spread:repeat, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(63, 127, 157, 255), stop:1 rgba(102, 142, 255, 255));\n"
"	border-right: none;\n"
"}\n"
"#center_menu_sub{\n"
"	border-right: 1px solid qlineargradient(spread:repeat, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(70, 124, 160, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"#right_menu_sub_container{\n"
"	border: 1px solid qlineargradient(spread:repeat, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(70, 124, 160, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"#btnStart, #btnStartInField, #btnAddToSchedule{\n"
"	padding: 0px 12px;\n"
"	border: 1px solid qlineargradient(spread:repeat, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(199, 215, 226, 255), stop:1 rgba(102, 142, 255, 255));\n"
"	border-radius: 6px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.149847, y1:0.028, x2:0.506, y2:0.865909, stop:0.0734463 rgba(27, 51, 106, 255), stop:0.344633 rgba(34, 84, 114, 255), stop:0.751412 rgba(27, 51, 106, 255))"
                        ";\n"
"}\n"
"#btnStart:hover, #btnStartInField:hover, #btnAddToSchedule:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.083, y1:0.177, x2:0.762, y2:0.534, stop:0 rgba(192, 210, 218, 255), stop:0.19774 rgba(125, 202, 194, 255), stop:0.59322 rgba(95, 145, 182, 255), stop:1 rgba(125, 202, 194, 255));\n"
"}\n"
"#listRecordedAudio, #listRecordedAudio_2, #listRecordedAudio_3, #zonesScrollArea, #listSchedule, #ipExtListContainer{\n"
"	border: 1px solid qlineargradient(spread:repeat, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(199, 215, 226, 255), stop:1 rgba(102, 142, 255, 255));\n"
"	padding: 6px 2px;\n"
"}\n"
"#listField{\n"
"	padding: 6px 5px;\n"
"}\n"
"#labelRecordedAudio, #labelRecordedAudio_2, #labelRecordedAudio_3, #labelZones, #labelListSchedule, #labelFieldList, #label_ip_ext{\n"
"	border: 1px solid qlineargradient(spread:repeat, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(199, 215, 226, 255), stop:1 rgba(102, 142, 255, 255));\n"
"	border-bottom: none;\n"
"	padding: 6px;\n"
"}\n"
"#lobbyContainer, #pan"
                        "tryContainer, #accountsContainer, #mainOfficeContainer, #gate1Container, #gate2Container{\n"
"	border: 1px solid qlineargradient(spread:repeat, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(199, 215, 226, 255), stop:1 rgba(102, 142, 255, 255));\n"
"	border-radius: 8px;\n"
"}\n"
"#firstStartBtn{\n"
"	border: 1px solid qlineargradient(spread:repeat, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(199, 215, 226, 255), stop:1 rgba(102, 142, 255, 255));\n"
"	border-radius: 10px;\n"
"}\n"
"#firstStartBtn:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.068, y1:0.25, x2:1, y2:0.801, stop:0 rgba(74, 153, 220, 185), stop:0.34981 rgba(99, 138, 216, 207), stop:0.714829 rgba(170, 204, 181, 203), stop:1 rgba(92, 96, 184, 215));\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_21 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.centralStackedWidget = QCustomStackedWidget(self.centralwidget)
        self.centralStackedWidget.setObjectName(u"centralStackedWidget")
        self.mainScreen = QWidget()
        self.mainScreen.setObjectName(u"mainScreen")
        self.verticalLayout_44 = QVBoxLayout(self.mainScreen)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.header_container = QWidget(self.mainScreen)
        self.header_container.setObjectName(u"header_container")
        self.horizontalLayout_5 = QHBoxLayout(self.header_container)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 10, 0, 10)
        self.frame_5 = QFrame(self.header_container)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btnNotification = QPushButton(self.frame_5)
        self.btnNotification.setObjectName(u"btnNotification")
        self.btnNotification.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnNotification.setIcon(icon)
        self.btnNotification.setIconSize(QSize(28, 28))

        self.horizontalLayout_6.addWidget(self.btnNotification)

        self.btnMore = QPushButton(self.frame_5)
        self.btnMore.setObjectName(u"btnMore")
        self.btnMore.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/more-horizontal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnMore.setIcon(icon1)
        self.btnMore.setIconSize(QSize(28, 28))

        self.horizontalLayout_6.addWidget(self.btnMore)

        self.btnProfile = QPushButton(self.frame_5)
        self.btnProfile.setObjectName(u"btnProfile")
        self.btnProfile.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnProfile.setIcon(icon2)
        self.btnProfile.setIconSize(QSize(28, 28))

        self.horizontalLayout_6.addWidget(self.btnProfile)


        self.horizontalLayout_5.addWidget(self.frame_5, 0, Qt.AlignHCenter)


        self.verticalLayout_44.addWidget(self.header_container)

        self.body_container = QWidget(self.mainScreen)
        self.body_container.setObjectName(u"body_container")
        self.horizontalLayout_13 = QHBoxLayout(self.body_container)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.sidebar_widget = QCustomSlideMenu(self.body_container)
        self.sidebar_widget.setObjectName(u"sidebar_widget")
        self.sidebar_widget.setMaximumSize(QSize(160, 16777215))
        self.sidebar_widget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.sidebar_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebar_sub_widget = QWidget(self.sidebar_widget)
        self.sidebar_sub_widget.setObjectName(u"sidebar_sub_widget")
        self.verticalLayout_2 = QVBoxLayout(self.sidebar_sub_widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.frame = QFrame(self.sidebar_sub_widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/chevron-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon3)
        self.menuBtn.setIconSize(QSize(28, 28))

        self.horizontalLayout_2.addWidget(self.menuBtn)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.sidebar_sub_widget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.btnHome = QPushButton(self.frame_2)
        self.btnHome.setObjectName(u"btnHome")
        font = QFont()
        font.setFamily(u"Noto Sans")
        font.setPointSize(12)
        self.btnHome.setFont(font)
        self.btnHome.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnHome.setStyleSheet(u"background-color: #253478;")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnHome.setIcon(icon4)
        self.btnHome.setIconSize(QSize(28, 28))

        self.verticalLayout_3.addWidget(self.btnHome)

        self.btnDataAnalysis = QPushButton(self.frame_2)
        self.btnDataAnalysis.setObjectName(u"btnDataAnalysis")
        self.btnDataAnalysis.setFont(font)
        self.btnDataAnalysis.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/list.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnDataAnalysis.setIcon(icon5)
        self.btnDataAnalysis.setIconSize(QSize(28, 28))

        self.verticalLayout_3.addWidget(self.btnDataAnalysis)

        self.btnReports = QPushButton(self.frame_2)
        self.btnReports.setObjectName(u"btnReports")
        self.btnReports.setFont(font)
        self.btnReports.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/printer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnReports.setIcon(icon6)
        self.btnReports.setIconSize(QSize(28, 28))

        self.verticalLayout_3.addWidget(self.btnReports)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.sidebar_sub_widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.btnSettings = QPushButton(self.frame_3)
        self.btnSettings.setObjectName(u"btnSettings")
        self.btnSettings.setFont(font)
        self.btnSettings.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSettings.setIcon(icon7)
        self.btnSettings.setIconSize(QSize(28, 28))

        self.verticalLayout_4.addWidget(self.btnSettings)

        self.btnInfo = QPushButton(self.frame_3)
        self.btnInfo.setObjectName(u"btnInfo")
        self.btnInfo.setFont(font)
        self.btnInfo.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnInfo.setIcon(icon8)
        self.btnInfo.setIconSize(QSize(28, 28))

        self.verticalLayout_4.addWidget(self.btnInfo)

        self.btnHelp = QPushButton(self.frame_3)
        self.btnHelp.setObjectName(u"btnHelp")
        self.btnHelp.setFont(font)
        self.btnHelp.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnHelp.setIcon(icon9)
        self.btnHelp.setIconSize(QSize(28, 28))

        self.verticalLayout_4.addWidget(self.btnHelp)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.sidebar_sub_widget)


        self.horizontalLayout_13.addWidget(self.sidebar_widget)

        self.center_menu = QCustomSlideMenu(self.body_container)
        self.center_menu.setObjectName(u"center_menu")
        self.center_menu.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.center_menu)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 1, 0)
        self.center_menu_sub = QWidget(self.center_menu)
        self.center_menu_sub.setObjectName(u"center_menu_sub")
        self.center_menu_sub.setMinimumSize(QSize(200, 0))
        self.verticalLayout_6 = QVBoxLayout(self.center_menu_sub)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_more_menu = QFrame(self.center_menu_sub)
        self.frame_more_menu.setObjectName(u"frame_more_menu")
        self.frame_more_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_more_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_more_menu)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(18, 6, 6, 6)
        self.moreMenuLabel = QLabel(self.frame_more_menu)
        self.moreMenuLabel.setObjectName(u"moreMenuLabel")
        self.moreMenuLabel.setFont(font)

        self.horizontalLayout_3.addWidget(self.moreMenuLabel)

        self.closeCenterMenuBtn = QPushButton(self.frame_more_menu)
        self.closeCenterMenuBtn.setObjectName(u"closeCenterMenuBtn")
        self.closeCenterMenuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeCenterMenuBtn.setIcon(icon10)
        self.closeCenterMenuBtn.setIconSize(QSize(28, 28))

        self.horizontalLayout_3.addWidget(self.closeCenterMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_more_menu, 0, Qt.AlignTop)

        self.centerMenuPage = QCustomStackedWidget(self.center_menu_sub)
        self.centerMenuPage.setObjectName(u"centerMenuPage")
        self.centerMenuSettingsPage = QWidget()
        self.centerMenuSettingsPage.setObjectName(u"centerMenuSettingsPage")
        self.verticalLayout_7 = QVBoxLayout(self.centerMenuSettingsPage)
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(6, 10, 6, 6)
        self.label_2 = QLabel(self.centerMenuSettingsPage)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_2)

        self.centerMenuPage.addWidget(self.centerMenuSettingsPage)
        self.centerMenuInfoPage = QWidget()
        self.centerMenuInfoPage.setObjectName(u"centerMenuInfoPage")
        self.verticalLayout_8 = QVBoxLayout(self.centerMenuInfoPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(6, 6, 6, 6)
        self.label_3 = QLabel(self.centerMenuInfoPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_3)

        self.centerMenuPage.addWidget(self.centerMenuInfoPage)
        self.centerMenuHelpPage = QWidget()
        self.centerMenuHelpPage.setObjectName(u"centerMenuHelpPage")
        self.verticalLayout_9 = QVBoxLayout(self.centerMenuHelpPage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(4, 14, 4, 6)
        self.help_content = QLabel(self.centerMenuHelpPage)
        self.help_content.setObjectName(u"help_content")
        self.help_content.setFont(font1)
        self.help_content.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.help_content.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.help_content)

        self.centerMenuPage.addWidget(self.centerMenuHelpPage)

        self.verticalLayout_6.addWidget(self.centerMenuPage)


        self.verticalLayout_5.addWidget(self.center_menu_sub, 0, Qt.AlignLeft)


        self.horizontalLayout_13.addWidget(self.center_menu)

        self.content_widget = QWidget(self.body_container)
        self.content_widget.setObjectName(u"content_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.content_widget.sizePolicy().hasHeightForWidth())
        self.content_widget.setSizePolicy(sizePolicy1)
        self.content_widget.setMinimumSize(QSize(718, 438))
        self.content_widget.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.content_widget)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.content_container = QWidget(self.content_widget)
        self.content_container.setObjectName(u"content_container")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.content_container.sizePolicy().hasHeightForWidth())
        self.content_container.setSizePolicy(sizePolicy2)
        self.content_container.setMinimumSize(QSize(718, 330))
        self.horizontalLayout_8 = QHBoxLayout(self.content_container)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(6, 6, 6, 6)
        self.main_contents_container = QWidget(self.content_container)
        self.main_contents_container.setObjectName(u"main_contents_container")
        self.main_contents_container.setMinimumSize(QSize(498, 0))
        self.verticalLayout_15 = QVBoxLayout(self.main_contents_container)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.mainPage = QCustomStackedWidget(self.main_contents_container)
        self.mainPage.setObjectName(u"mainPage")
        self.mainHomePage = QWidget()
        self.mainHomePage.setObjectName(u"mainHomePage")
        self.verticalLayout_36 = QVBoxLayout(self.mainHomePage)
        self.verticalLayout_36.setSpacing(30)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(8, 30, 8, 8)
        self.frame_9 = QFrame(self.mainHomePage)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 300))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.homePageLogoLabel = QLabel(self.frame_9)
        self.homePageLogoLabel.setObjectName(u"homePageLogoLabel")
        self.homePageLogoLabel.setMaximumSize(QSize(280, 150))
        self.homePageLogoLabel.setPixmap(QPixmap(u":/images/images/EVERCON 2nd style.png"))
        self.homePageLogoLabel.setScaledContents(True)

        self.horizontalLayout_26.addWidget(self.homePageLogoLabel)


        self.verticalLayout_36.addWidget(self.frame_9)

        self.homePageBtnGroup = QFrame(self.mainHomePage)
        self.homePageBtnGroup.setObjectName(u"homePageBtnGroup")
        self.homePageBtnGroup.setFrameShape(QFrame.StyledPanel)
        self.homePageBtnGroup.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.homePageBtnGroup)
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.zonesContainer = QWidget(self.homePageBtnGroup)
        self.zonesContainer.setObjectName(u"zonesContainer")
        self.zonesContainer.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_16 = QVBoxLayout(self.zonesContainer)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(5, 5, 5, 5)
        self.btnZones = QPushButton(self.zonesContainer)
        self.btnZones.setObjectName(u"btnZones")
        self.btnZones.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/icons8-grid-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnZones.setIcon(icon11)
        self.btnZones.setIconSize(QSize(118, 80))

        self.verticalLayout_16.addWidget(self.btnZones, 0, Qt.AlignHCenter)

        self.label_9 = QLabel(self.zonesContainer)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_9)


        self.horizontalLayout_11.addWidget(self.zonesContainer, 0, Qt.AlignTop)

        self.cameraContainer = QWidget(self.homePageBtnGroup)
        self.cameraContainer.setObjectName(u"cameraContainer")
        self.cameraContainer.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_32 = QVBoxLayout(self.cameraContainer)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(5, 5, 5, 5)
        self.btnCamera = QPushButton(self.cameraContainer)
        self.btnCamera.setObjectName(u"btnCamera")
        self.btnCamera.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/camera.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnCamera.setIcon(icon12)
        self.btnCamera.setIconSize(QSize(118, 80))

        self.verticalLayout_32.addWidget(self.btnCamera, 0, Qt.AlignHCenter)

        self.label_18 = QLabel(self.cameraContainer)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_18)


        self.horizontalLayout_11.addWidget(self.cameraContainer, 0, Qt.AlignTop)

        self.fieldContainer = QWidget(self.homePageBtnGroup)
        self.fieldContainer.setObjectName(u"fieldContainer")
        self.fieldContainer.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_22 = QVBoxLayout(self.fieldContainer)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(5, 5, 5, 5)
        self.btnFieldStations = QPushButton(self.fieldContainer)
        self.btnFieldStations.setObjectName(u"btnFieldStations")
        self.btnFieldStations.setCursor(QCursor(Qt.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/icons8-telephone-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnFieldStations.setIcon(icon13)
        self.btnFieldStations.setIconSize(QSize(118, 80))

        self.verticalLayout_22.addWidget(self.btnFieldStations, 0, Qt.AlignHCenter)

        self.label_14 = QLabel(self.fieldContainer)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 0))
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_14)


        self.horizontalLayout_11.addWidget(self.fieldContainer, 0, Qt.AlignTop)

        self.scheduleContainer = QWidget(self.homePageBtnGroup)
        self.scheduleContainer.setObjectName(u"scheduleContainer")
        self.scheduleContainer.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_23 = QVBoxLayout(self.scheduleContainer)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(5, 5, 5, 5)
        self.btnSchedule = QPushButton(self.scheduleContainer)
        self.btnSchedule.setObjectName(u"btnSchedule")
        self.btnSchedule.setCursor(QCursor(Qt.PointingHandCursor))
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/icons8-schedule-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSchedule.setIcon(icon14)
        self.btnSchedule.setIconSize(QSize(118, 80))

        self.verticalLayout_23.addWidget(self.btnSchedule, 0, Qt.AlignHCenter)

        self.label_15 = QLabel(self.scheduleContainer)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_15)


        self.horizontalLayout_11.addWidget(self.scheduleContainer, 0, Qt.AlignTop)

        self.recordContainer = QWidget(self.homePageBtnGroup)
        self.recordContainer.setObjectName(u"recordContainer")
        self.recordContainer.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_24 = QVBoxLayout(self.recordContainer)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(5, 5, 5, 5)
        self.btnRecord = QPushButton(self.recordContainer)
        self.btnRecord.setObjectName(u"btnRecord")
        self.btnRecord.setCursor(QCursor(Qt.PointingHandCursor))
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/icons8-record-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnRecord.setIcon(icon15)
        self.btnRecord.setIconSize(QSize(118, 80))

        self.verticalLayout_24.addWidget(self.btnRecord, 0, Qt.AlignHCenter)

        self.label_16 = QLabel(self.recordContainer)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_16)


        self.horizontalLayout_11.addWidget(self.recordContainer, 0, Qt.AlignTop)


        self.verticalLayout_36.addWidget(self.homePageBtnGroup)

        self.mainPage.addWidget(self.mainHomePage)
        self.mainDataPage = QWidget()
        self.mainDataPage.setObjectName(u"mainDataPage")
        self.verticalLayout_17 = QVBoxLayout(self.mainDataPage)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.mainDataPage)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_10)

        self.mainPage.addWidget(self.mainDataPage)
        self.mainReportPage = QWidget()
        self.mainReportPage.setObjectName(u"mainReportPage")
        self.verticalLayout_18 = QVBoxLayout(self.mainReportPage)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.mainReportPage)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_11)

        self.mainPage.addWidget(self.mainReportPage)
        self.mainZonePage = QWidget()
        self.mainZonePage.setObjectName(u"mainZonePage")
        self.verticalLayout_25 = QVBoxLayout(self.mainZonePage)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.zonePageHeader = QFrame(self.mainZonePage)
        self.zonePageHeader.setObjectName(u"zonePageHeader")
        self.zonePageHeader.setFrameShape(QFrame.StyledPanel)
        self.zonePageHeader.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.zonePageHeader)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 10, 0, 10)
        self.VirtualFrame = QFrame(self.zonePageHeader)
        self.VirtualFrame.setObjectName(u"VirtualFrame")
        self.VirtualFrame.setFrameShape(QFrame.StyledPanel)
        self.VirtualFrame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_16.addWidget(self.VirtualFrame)

        self.radioBtnGroup = QFrame(self.zonePageHeader)
        self.radioBtnGroup.setObjectName(u"radioBtnGroup")
        self.radioBtnGroup.setStyleSheet(u"")
        self.radioBtnGroup.setFrameShape(QFrame.StyledPanel)
        self.radioBtnGroup.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.radioBtnGroup)
        self.horizontalLayout_17.setSpacing(100)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 10, 0, 10)
        self.radioMic = QRadioButton(self.radioBtnGroup)
        self.radioMic.setObjectName(u"radioMic")
        font2 = QFont()
        font2.setFamily(u"Noto Sans")
        font2.setPointSize(14)
        self.radioMic.setFont(font2)
        self.radioMic.setStyleSheet(u"QRadioButton::indicator:unchecked {\n"
"    image: url(:/icons/icons/circle.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    image: url(:/icons/icons/check-circle.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator{\n"
"	width: 23px;\n"
"	height: 23px;\n"
"}")

        self.horizontalLayout_17.addWidget(self.radioMic)

        self.radioRecorded = QRadioButton(self.radioBtnGroup)
        self.radioRecorded.setObjectName(u"radioRecorded")
        self.radioRecorded.setFont(font2)
        self.radioRecorded.setStyleSheet(u"QRadioButton::indicator:unchecked {\n"
"    image: url(:/icons/icons/circle.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    image: url(:/icons/icons/check-circle.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator{\n"
"	width: 23px;\n"
"	height: 23px;\n"
"}")
        self.radioRecorded.setChecked(True)

        self.horizontalLayout_17.addWidget(self.radioRecorded)


        self.horizontalLayout_16.addWidget(self.radioBtnGroup, 0, Qt.AlignHCenter)


        self.verticalLayout_25.addWidget(self.zonePageHeader)

        self.zonePageBody = QFrame(self.mainZonePage)
        self.zonePageBody.setObjectName(u"zonePageBody")
        self.zonePageBody.setFrameShape(QFrame.StyledPanel)
        self.zonePageBody.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.zonePageBody)
        self.horizontalLayout_15.setSpacing(10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(5, 5, 5, 5)
        self.zonesListContainer = QFrame(self.zonePageBody)
        self.zonesListContainer.setObjectName(u"zonesListContainer")
        self.zonesListContainer.setMinimumSize(QSize(482, 0))
        self.zonesListContainer.setMaximumSize(QSize(600, 16777215))
        self.zonesListContainer.setFrameShape(QFrame.StyledPanel)
        self.zonesListContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.zonesListContainer)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(2, 2, 2, 2)
        self.labelZones = QLabel(self.zonesListContainer)
        self.labelZones.setObjectName(u"labelZones")
        font3 = QFont()
        font3.setFamily(u"Noto Sans")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.labelZones.setFont(font3)
        self.labelZones.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.labelZones)

        self.zonesScrollArea = QScrollArea(self.zonesListContainer)
        self.zonesScrollArea.setObjectName(u"zonesScrollArea")
        self.zonesScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 472, 188))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(472, 0))
        self.hboxLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.hboxLayout.setSpacing(0)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.hboxLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollAreaInnerContainer = QFrame(self.scrollAreaWidgetContents)
        self.scrollAreaInnerContainer.setObjectName(u"scrollAreaInnerContainer")
        self.scrollAreaInnerContainer.setFrameShape(QFrame.StyledPanel)
        self.scrollAreaInnerContainer.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.scrollAreaInnerContainer)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lobbyContainer = QFrame(self.scrollAreaInnerContainer)
        self.lobbyContainer.setObjectName(u"lobbyContainer")
        self.lobbyContainer.setMinimumSize(QSize(142, 80))
        self.lobbyContainer.setMaximumSize(QSize(142, 80))
        self.lobbyContainer.setFrameShape(QFrame.StyledPanel)
        self.lobbyContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.lobbyContainer)
        self.horizontalLayout_32.setSpacing(5)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(12, 12, 12, 12)
        self.lobbyLabel = QLabel(self.lobbyContainer)
        self.lobbyLabel.setObjectName(u"lobbyLabel")
        self.lobbyLabel.setFont(font2)
        self.lobbyLabel.setWordWrap(True)

        self.horizontalLayout_32.addWidget(self.lobbyLabel)

        self.lobbyCheck = QCheckBox(self.lobbyContainer)
        self.lobbyCheck.setObjectName(u"lobbyCheck")
        self.lobbyCheck.setStyleSheet(u"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icons/icons/square.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icons/icons/check-square.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"	width: 24px;\n"
"	height: 24px;\n"
"}")

        self.horizontalLayout_32.addWidget(self.lobbyCheck, 0, Qt.AlignRight|Qt.AlignBottom)


        self.gridLayout.addWidget(self.lobbyContainer, 0, 0, 1, 1)

        self.pantryContainer = QFrame(self.scrollAreaInnerContainer)
        self.pantryContainer.setObjectName(u"pantryContainer")
        self.pantryContainer.setMinimumSize(QSize(142, 80))
        self.pantryContainer.setMaximumSize(QSize(142, 80))
        self.pantryContainer.setFrameShape(QFrame.StyledPanel)
        self.pantryContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.pantryContainer)
        self.horizontalLayout_27.setSpacing(5)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(12, 12, 12, 12)
        self.pantryLabel = QLabel(self.pantryContainer)
        self.pantryLabel.setObjectName(u"pantryLabel")
        self.pantryLabel.setFont(font2)
        self.pantryLabel.setWordWrap(True)

        self.horizontalLayout_27.addWidget(self.pantryLabel)

        self.pantryCheck = QCheckBox(self.pantryContainer)
        self.pantryCheck.setObjectName(u"pantryCheck")
        self.pantryCheck.setStyleSheet(u"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icons/icons/square.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icons/icons/check-square.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"	width: 24px;\n"
"	height: 24px;\n"
"}")

        self.horizontalLayout_27.addWidget(self.pantryCheck, 0, Qt.AlignRight|Qt.AlignBottom)


        self.gridLayout.addWidget(self.pantryContainer, 0, 1, 1, 1)

        self.accountsContainer = QFrame(self.scrollAreaInnerContainer)
        self.accountsContainer.setObjectName(u"accountsContainer")
        self.accountsContainer.setMinimumSize(QSize(142, 80))
        self.accountsContainer.setMaximumSize(QSize(142, 80))
        self.accountsContainer.setFrameShape(QFrame.StyledPanel)
        self.accountsContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.accountsContainer)
        self.horizontalLayout_28.setSpacing(5)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(12, 12, 12, 12)
        self.accountsLabel = QLabel(self.accountsContainer)
        self.accountsLabel.setObjectName(u"accountsLabel")
        self.accountsLabel.setFont(font2)
        self.accountsLabel.setWordWrap(True)

        self.horizontalLayout_28.addWidget(self.accountsLabel)

        self.accountsCheck = QCheckBox(self.accountsContainer)
        self.accountsCheck.setObjectName(u"accountsCheck")
        self.accountsCheck.setStyleSheet(u"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icons/icons/square.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icons/icons/check-square.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"	width: 24px;\n"
"	height: 24px;\n"
"}")

        self.horizontalLayout_28.addWidget(self.accountsCheck, 0, Qt.AlignRight|Qt.AlignBottom)


        self.gridLayout.addWidget(self.accountsContainer, 0, 2, 1, 1)

        self.mainOfficeContainer = QFrame(self.scrollAreaInnerContainer)
        self.mainOfficeContainer.setObjectName(u"mainOfficeContainer")
        self.mainOfficeContainer.setMinimumSize(QSize(142, 80))
        self.mainOfficeContainer.setMaximumSize(QSize(142, 80))
        self.mainOfficeContainer.setFrameShape(QFrame.StyledPanel)
        self.mainOfficeContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.mainOfficeContainer)
        self.horizontalLayout_29.setSpacing(5)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(12, 12, 12, 12)
        self.mainOfficeLabel = QLabel(self.mainOfficeContainer)
        self.mainOfficeLabel.setObjectName(u"mainOfficeLabel")
        self.mainOfficeLabel.setFont(font2)
        self.mainOfficeLabel.setWordWrap(True)

        self.horizontalLayout_29.addWidget(self.mainOfficeLabel)

        self.mainOfficeCheck = QCheckBox(self.mainOfficeContainer)
        self.mainOfficeCheck.setObjectName(u"mainOfficeCheck")
        self.mainOfficeCheck.setStyleSheet(u"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icons/icons/square.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icons/icons/check-square.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"	width: 24px;\n"
"	height: 24px;\n"
"}")

        self.horizontalLayout_29.addWidget(self.mainOfficeCheck, 0, Qt.AlignRight|Qt.AlignBottom)


        self.gridLayout.addWidget(self.mainOfficeContainer, 1, 0, 1, 1)

        self.gate1Container = QFrame(self.scrollAreaInnerContainer)
        self.gate1Container.setObjectName(u"gate1Container")
        self.gate1Container.setMinimumSize(QSize(142, 80))
        self.gate1Container.setMaximumSize(QSize(142, 80))
        self.gate1Container.setFrameShape(QFrame.StyledPanel)
        self.gate1Container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.gate1Container)
        self.horizontalLayout_30.setSpacing(5)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(12, 12, 12, 12)
        self.gate1Label = QLabel(self.gate1Container)
        self.gate1Label.setObjectName(u"gate1Label")
        self.gate1Label.setFont(font2)
        self.gate1Label.setWordWrap(True)

        self.horizontalLayout_30.addWidget(self.gate1Label)

        self.gate1Check = QCheckBox(self.gate1Container)
        self.gate1Check.setObjectName(u"gate1Check")
        self.gate1Check.setStyleSheet(u"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icons/icons/square.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icons/icons/check-square.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"	width: 24px;\n"
"	height: 24px;\n"
"}")

        self.horizontalLayout_30.addWidget(self.gate1Check, 0, Qt.AlignRight|Qt.AlignBottom)


        self.gridLayout.addWidget(self.gate1Container, 1, 1, 1, 1)

        self.gate2Container = QFrame(self.scrollAreaInnerContainer)
        self.gate2Container.setObjectName(u"gate2Container")
        self.gate2Container.setMinimumSize(QSize(142, 80))
        self.gate2Container.setMaximumSize(QSize(142, 80))
        self.gate2Container.setFrameShape(QFrame.StyledPanel)
        self.gate2Container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.gate2Container)
        self.horizontalLayout_31.setSpacing(5)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(12, 12, 12, 12)
        self.gate2Label = QLabel(self.gate2Container)
        self.gate2Label.setObjectName(u"gate2Label")
        self.gate2Label.setFont(font2)
        self.gate2Label.setWordWrap(True)

        self.horizontalLayout_31.addWidget(self.gate2Label)

        self.gate2Check = QCheckBox(self.gate2Container)
        self.gate2Check.setObjectName(u"gate2Check")
        self.gate2Check.setStyleSheet(u"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icons/icons/square.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icons/icons/check-square.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"	width: 24px;\n"
"	height: 24px;\n"
"}")

        self.horizontalLayout_31.addWidget(self.gate2Check, 0, Qt.AlignRight|Qt.AlignBottom)


        self.gridLayout.addWidget(self.gate2Container, 1, 2, 1, 1)


        self.hboxLayout.addWidget(self.scrollAreaInnerContainer)

        self.zonesScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_26.addWidget(self.zonesScrollArea)


        self.horizontalLayout_15.addWidget(self.zonesListContainer)

        self.audioRecordedContainer = QFrame(self.zonePageBody)
        self.audioRecordedContainer.setObjectName(u"audioRecordedContainer")
        self.audioRecordedContainer.setMaximumSize(QSize(250, 450))
        self.audioRecordedContainer.setFrameShape(QFrame.StyledPanel)
        self.audioRecordedContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.audioRecordedContainer)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(2, 2, 2, 2)
        self.labelRecordedAudio = QLabel(self.audioRecordedContainer)
        self.labelRecordedAudio.setObjectName(u"labelRecordedAudio")
        self.labelRecordedAudio.setFont(font3)
        self.labelRecordedAudio.setScaledContents(False)
        self.labelRecordedAudio.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.labelRecordedAudio)

        self.listRecordedAudio = QListWidget(self.audioRecordedContainer)
        self.listRecordedAudio.setObjectName(u"listRecordedAudio")
        self.listRecordedAudio.setMinimumSize(QSize(180, 0))
        self.listRecordedAudio.setFont(font2)
        self.listRecordedAudio.setStyleSheet(u"QListWidget:item {\n"
"	padding: 4px 0px;\n"
"}")

        self.verticalLayout_27.addWidget(self.listRecordedAudio)


        self.horizontalLayout_15.addWidget(self.audioRecordedContainer, 0, Qt.AlignHCenter)


        self.verticalLayout_25.addWidget(self.zonePageBody)

        self.zonePageFooter = QFrame(self.mainZonePage)
        self.zonePageFooter.setObjectName(u"zonePageFooter")
        self.zonePageFooter.setFrameShape(QFrame.StyledPanel)
        self.zonePageFooter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.zonePageFooter)
        self.verticalLayout_38.setSpacing(20)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 20, 0, 20)
        self.volumeSetFrame = QFrame(self.zonePageFooter)
        self.volumeSetFrame.setObjectName(u"volumeSetFrame")
        self.volumeSetFrame.setFrameShape(QFrame.StyledPanel)
        self.volumeSetFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.volumeSetFrame)
        self.horizontalLayout_20.setSpacing(10)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(2, 5, 2, 2)
        self.btnVolume = QPushButton(self.volumeSetFrame)
        self.btnVolume.setObjectName(u"btnVolume")
        self.btnVolume.setCursor(QCursor(Qt.PointingHandCursor))
        icon16 = QIcon()
        icon16.addFile(u":/icons/icons/volume-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnVolume.setIcon(icon16)
        self.btnVolume.setIconSize(QSize(28, 28))
        self.btnVolume.setCheckable(True)

        self.horizontalLayout_20.addWidget(self.btnVolume)

        self.volumeSlider = QSlider(self.volumeSetFrame)
        self.volumeSlider.setObjectName(u"volumeSlider")
        self.volumeSlider.setMinimumSize(QSize(300, 28))
        self.volumeSlider.setCursor(QCursor(Qt.PointingHandCursor))
        self.volumeSlider.setStyleSheet(u"QSlider::groove:horizontal{\n"
"	height: 2px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.083, y1:0.177, x2:0.762, y2:0.534, stop:0 rgba(192, 210, 218, 255), stop:0.19774 rgba(125, 202, 194, 255), stop:0.59322 rgba(95, 145, 182, 255), stop:1 rgba(125, 202, 194, 255));\n"
"	margin: 10px 0px;\n"
"}\n"
"QSlider::groove:horizontal:disabled{\n"
"	background-color: #666;\n"
"}\n"
"QSlider::handle:horizontal{\n"
"	background-color: qlineargradient(spread:repeat, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(199, 215, 226, 255), stop:1 rgba(102, 142, 255, 255));\n"
"	width: 8px;\n"
"	margin: -10px 0px;\n"
"	border-radius: 4px;\n"
"}\n"
"QSlider::handle:horizontal:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.336158, y1:0.034, x2:0.63, y2:0.972, stop:0 rgba(149, 180, 134, 255), stop:0.316384 rgba(92, 168, 54, 255), stop:0.621469 rgba(79, 155, 41, 255), stop:1 rgba(216, 251, 199, 255));\n"
"}\n"
"QSlider::handle:horizontal:disabled{\n"
"	background-color: #aaa;\n"
"}")
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setValue(100)
        self.volumeSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_20.addWidget(self.volumeSlider)

        self.labelVolume = QLabel(self.volumeSetFrame)
        self.labelVolume.setObjectName(u"labelVolume")
        self.labelVolume.setMinimumSize(QSize(30, 0))
        self.labelVolume.setFont(font)
        self.labelVolume.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.labelVolume)


        self.verticalLayout_38.addWidget(self.volumeSetFrame, 0, Qt.AlignHCenter)

        self.frame_10 = QFrame(self.zonePageFooter)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_10)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.btnStart = QPushButton(self.frame_10)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setMinimumSize(QSize(0, 40))
        font4 = QFont()
        font4.setFamily(u"Noto Sans")
        font4.setPointSize(16)
        font4.setBold(True)
        font4.setWeight(75)
        self.btnStart.setFont(font4)
        self.btnStart.setCursor(QCursor(Qt.PointingHandCursor))
        icon17 = QIcon()
        icon17.addFile(u":/icons/icons/play.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnStart.setIcon(icon17)
        self.btnStart.setIconSize(QSize(28, 28))

        self.verticalLayout_37.addWidget(self.btnStart, 0, Qt.AlignHCenter)


        self.verticalLayout_38.addWidget(self.frame_10)


        self.verticalLayout_25.addWidget(self.zonePageFooter)

        self.mainPage.addWidget(self.mainZonePage)
        self.mainFieldPage = QWidget()
        self.mainFieldPage.setObjectName(u"mainFieldPage")
        self.verticalLayout_43 = QVBoxLayout(self.mainFieldPage)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.fieldPageHeader = QFrame(self.mainFieldPage)
        self.fieldPageHeader.setObjectName(u"fieldPageHeader")
        self.fieldPageHeader.setFrameShape(QFrame.StyledPanel)
        self.fieldPageHeader.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.fieldPageHeader)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 10, 0, 10)
        self.VirtualFrame_2 = QFrame(self.fieldPageHeader)
        self.VirtualFrame_2.setObjectName(u"VirtualFrame_2")
        self.VirtualFrame_2.setFrameShape(QFrame.StyledPanel)
        self.VirtualFrame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_19.addWidget(self.VirtualFrame_2)

        self.radioBtnGroup_2 = QFrame(self.fieldPageHeader)
        self.radioBtnGroup_2.setObjectName(u"radioBtnGroup_2")
        self.radioBtnGroup_2.setStyleSheet(u"")
        self.radioBtnGroup_2.setFrameShape(QFrame.StyledPanel)
        self.radioBtnGroup_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.radioBtnGroup_2)
        self.horizontalLayout_25.setSpacing(100)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 10, 0, 10)
        self.radioMicInField = QRadioButton(self.radioBtnGroup_2)
        self.radioMicInField.setObjectName(u"radioMicInField")
        self.radioMicInField.setFont(font2)
        self.radioMicInField.setStyleSheet(u"QRadioButton::indicator:unchecked {\n"
"    image: url(:/icons/icons/circle.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    image: url(:/icons/icons/check-circle.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator{\n"
"	width: 23px;\n"
"	height: 23px;\n"
"}")

        self.horizontalLayout_25.addWidget(self.radioMicInField)

        self.radioRecordedInField = QRadioButton(self.radioBtnGroup_2)
        self.radioRecordedInField.setObjectName(u"radioRecordedInField")
        self.radioRecordedInField.setFont(font2)
        self.radioRecordedInField.setStyleSheet(u"QRadioButton::indicator:unchecked {\n"
"    image: url(:/icons/icons/circle.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    image: url(:/icons/icons/check-circle.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator{\n"
"	width: 23px;\n"
"	height: 23px;\n"
"}")
        self.radioRecordedInField.setChecked(True)

        self.horizontalLayout_25.addWidget(self.radioRecordedInField)


        self.horizontalLayout_19.addWidget(self.radioBtnGroup_2, 0, Qt.AlignHCenter)


        self.verticalLayout_43.addWidget(self.fieldPageHeader)

        self.fieldPageBody = QFrame(self.mainFieldPage)
        self.fieldPageBody.setObjectName(u"fieldPageBody")
        self.fieldPageBody.setFrameShape(QFrame.StyledPanel)
        self.fieldPageBody.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.fieldPageBody)
        self.horizontalLayout_18.setSpacing(10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(5, 5, 5, 5)
        self.fieldListContainer = QFrame(self.fieldPageBody)
        self.fieldListContainer.setObjectName(u"fieldListContainer")
        self.fieldListContainer.setMinimumSize(QSize(400, 0))
        self.fieldListContainer.setMaximumSize(QSize(400, 16777215))
        self.fieldListContainer.setFrameShape(QFrame.StyledPanel)
        self.fieldListContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.fieldListContainer)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(2, 2, 2, 2)
        self.labelFieldList = QLabel(self.fieldListContainer)
        self.labelFieldList.setObjectName(u"labelFieldList")
        self.labelFieldList.setFont(font3)
        self.labelFieldList.setAlignment(Qt.AlignCenter)

        self.verticalLayout_39.addWidget(self.labelFieldList)

        self.label_ip_ext = QLabel(self.fieldListContainer)
        self.label_ip_ext.setObjectName(u"label_ip_ext")
        self.label_ip_ext.setFont(font)
        self.label_ip_ext.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_39.addWidget(self.label_ip_ext)

        self.ipExtListContainer = QFrame(self.fieldListContainer)
        self.ipExtListContainer.setObjectName(u"ipExtListContainer")
        self.ipExtListContainer.setFrameShape(QFrame.StyledPanel)
        self.ipExtListContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.ipExtListContainer)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.listField = QListWidget(self.ipExtListContainer)
        QListWidgetItem(self.listField)
        QListWidgetItem(self.listField)
        QListWidgetItem(self.listField)
        QListWidgetItem(self.listField)
        self.listField.setObjectName(u"listField")
        self.listField.setFont(font2)
        self.listField.setStyleSheet(u"QListWidget:item {\n"
"	padding: 4px 0px;\n"
"}")

        self.horizontalLayout_14.addWidget(self.listField)


        self.verticalLayout_39.addWidget(self.ipExtListContainer)


        self.horizontalLayout_18.addWidget(self.fieldListContainer, 0, Qt.AlignHCenter)

        self.audioRecordedContainer_3 = QFrame(self.fieldPageBody)
        self.audioRecordedContainer_3.setObjectName(u"audioRecordedContainer_3")
        self.audioRecordedContainer_3.setMaximumSize(QSize(250, 450))
        self.audioRecordedContainer_3.setFrameShape(QFrame.StyledPanel)
        self.audioRecordedContainer_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.audioRecordedContainer_3)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(2, 2, 2, 2)
        self.labelRecordedAudio_3 = QLabel(self.audioRecordedContainer_3)
        self.labelRecordedAudio_3.setObjectName(u"labelRecordedAudio_3")
        self.labelRecordedAudio_3.setFont(font3)
        self.labelRecordedAudio_3.setScaledContents(False)
        self.labelRecordedAudio_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_40.addWidget(self.labelRecordedAudio_3)

        self.listRecordedAudio_3 = QListWidget(self.audioRecordedContainer_3)
        self.listRecordedAudio_3.setObjectName(u"listRecordedAudio_3")
        self.listRecordedAudio_3.setMinimumSize(QSize(180, 0))
        self.listRecordedAudio_3.setFont(font2)
        self.listRecordedAudio_3.setStyleSheet(u"QListWidget:item {\n"
"	padding: 4px 0px;\n"
"}")

        self.verticalLayout_40.addWidget(self.listRecordedAudio_3)


        self.horizontalLayout_18.addWidget(self.audioRecordedContainer_3, 0, Qt.AlignHCenter)


        self.verticalLayout_43.addWidget(self.fieldPageBody)

        self.fieldPageFooter = QFrame(self.mainFieldPage)
        self.fieldPageFooter.setObjectName(u"fieldPageFooter")
        self.fieldPageFooter.setFrameShape(QFrame.StyledPanel)
        self.fieldPageFooter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.fieldPageFooter)
        self.verticalLayout_41.setSpacing(20)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 20, 0, 20)
        self.volumeSetFrame_3 = QFrame(self.fieldPageFooter)
        self.volumeSetFrame_3.setObjectName(u"volumeSetFrame_3")
        self.volumeSetFrame_3.setFrameShape(QFrame.StyledPanel)
        self.volumeSetFrame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.volumeSetFrame_3)
        self.horizontalLayout_22.setSpacing(10)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(2, 5, 2, 2)
        self.btnVolume_3 = QPushButton(self.volumeSetFrame_3)
        self.btnVolume_3.setObjectName(u"btnVolume_3")
        self.btnVolume_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnVolume_3.setIcon(icon16)
        self.btnVolume_3.setIconSize(QSize(28, 28))
        self.btnVolume_3.setCheckable(True)

        self.horizontalLayout_22.addWidget(self.btnVolume_3)

        self.volumeSlider_3 = QSlider(self.volumeSetFrame_3)
        self.volumeSlider_3.setObjectName(u"volumeSlider_3")
        self.volumeSlider_3.setMinimumSize(QSize(300, 28))
        self.volumeSlider_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.volumeSlider_3.setStyleSheet(u"QSlider::groove:horizontal{\n"
"	height: 2px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.083, y1:0.177, x2:0.762, y2:0.534, stop:0 rgba(192, 210, 218, 255), stop:0.19774 rgba(125, 202, 194, 255), stop:0.59322 rgba(95, 145, 182, 255), stop:1 rgba(125, 202, 194, 255));\n"
"	margin: 10px 0px;\n"
"}\n"
"QSlider::groove:horizontal:disabled{\n"
"	background-color: #666;\n"
"}\n"
"QSlider::handle:horizontal{\n"
"	background-color: qlineargradient(spread:repeat, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(199, 215, 226, 255), stop:1 rgba(102, 142, 255, 255));\n"
"	width: 8px;\n"
"	margin: -10px 0px;\n"
"	border-radius: 4px;\n"
"}\n"
"QSlider::handle:horizontal:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.336158, y1:0.034, x2:0.63, y2:0.972, stop:0 rgba(149, 180, 134, 255), stop:0.316384 rgba(92, 168, 54, 255), stop:0.621469 rgba(79, 155, 41, 255), stop:1 rgba(216, 251, 199, 255));\n"
"}\n"
"QSlider::handle:horizontal:disabled{\n"
"	background-color: #aaa;\n"
"}")
        self.volumeSlider_3.setMaximum(100)
        self.volumeSlider_3.setValue(100)
        self.volumeSlider_3.setOrientation(Qt.Horizontal)

        self.horizontalLayout_22.addWidget(self.volumeSlider_3)

        self.labelVolume_3 = QLabel(self.volumeSetFrame_3)
        self.labelVolume_3.setObjectName(u"labelVolume_3")
        self.labelVolume_3.setMinimumSize(QSize(30, 0))
        self.labelVolume_3.setFont(font)
        self.labelVolume_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.labelVolume_3)


        self.verticalLayout_41.addWidget(self.volumeSetFrame_3, 0, Qt.AlignHCenter)

        self.frame_11 = QFrame(self.fieldPageFooter)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_11)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.btnStartInField = QPushButton(self.frame_11)
        self.btnStartInField.setObjectName(u"btnStartInField")
        self.btnStartInField.setMinimumSize(QSize(0, 40))
        self.btnStartInField.setFont(font4)
        self.btnStartInField.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnStartInField.setIcon(icon17)
        self.btnStartInField.setIconSize(QSize(28, 28))

        self.verticalLayout_42.addWidget(self.btnStartInField, 0, Qt.AlignHCenter)


        self.verticalLayout_41.addWidget(self.frame_11)


        self.verticalLayout_43.addWidget(self.fieldPageFooter)

        self.mainPage.addWidget(self.mainFieldPage)
        self.mainSchedulePage = QWidget()
        self.mainSchedulePage.setObjectName(u"mainSchedulePage")
        self.horizontalLayout_12 = QHBoxLayout(self.mainSchedulePage)
        self.horizontalLayout_12.setSpacing(2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(2, 6, 2, 6)
        self.frame_4 = QFrame(self.mainSchedulePage)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_4)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.schedulePageBody = QFrame(self.frame_4)
        self.schedulePageBody.setObjectName(u"schedulePageBody")
        self.schedulePageBody.setFrameShape(QFrame.StyledPanel)
        self.schedulePageBody.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.schedulePageBody)
        self.horizontalLayout_21.setSpacing(10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.calendarContainer = QFrame(self.schedulePageBody)
        self.calendarContainer.setObjectName(u"calendarContainer")
        self.calendarContainer.setMinimumSize(QSize(316, 0))
        self.calendarContainer.setMaximumSize(QSize(420, 420))
        self.calendarContainer.setFrameShape(QFrame.StyledPanel)
        self.calendarContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.calendarContainer)
        self.verticalLayout_28.setSpacing(2)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(2, 2, 2, 2)
        self.calendarWidget = QCalendarWidget(self.calendarContainer)
        self.calendarWidget.setObjectName(u"calendarWidget")
        font5 = QFont()
        font5.setFamily(u"Noto Sans")
        font5.setPointSize(13)
        font5.setBold(True)
        font5.setWeight(75)
        self.calendarWidget.setFont(font5)
        self.calendarWidget.setCursor(QCursor(Qt.PointingHandCursor))
        self.calendarWidget.setStyleSheet(u"QCalendarWidget {\n"
"	font-size: 13pt;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"	height: 48px;\n"
"	width: 150px;\n"
"	background-color: rgba(30, 42, 90, 140);\n"
"	color: #eee;\n"
"	icon-size: 28px, 28px;\n"
"}\n"
"QCalendarWidget QToolButton:hover{\n"
"	border: 1px solid qlineargradient(spread:repeat, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(70, 124, 160, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(82, 124, 148, 255), stop:0.457627 rgba(46, 78, 121, 255), stop:0.542373 rgba(36, 66, 113, 255), stop:0.79096 rgba(42, 98, 123, 255), stop:1 rgba(125, 164, 203, 255));\n"
"}\n"
"#qt_calendar_prevmonth {\n"
"	qproperty-icon: url(:/icons/icons/chevron-left.svg);\n"
"	width:60px;\n"
"}\n"
"#qt_calendar_nextmonth {\n"
"	qproperty-icon: url(:/icons/icons/chevron-right.svg);\n"
"	width:60px;\n"
"}\n"
"QCalendarWidget QWidget {\n"
"	alternate-background-color: rgba(34, 84, 114, 100);\n"
"}\n"
"QCalendarWidget QAbstractItemView:enabl"
                        "ed {\n"
"	color: #eee;\n"
"	background-color: rgba(30, 42, 95);\n"
"	selection-background-color: qlineargradient(spread:pad, x1:0.068, y1:0.25, x2:1, y2:0.801, stop:0 rgba(74, 153, 220, 185), stop:0.34981 rgba(99, 138, 216, 207), stop:0.714829 rgba(170, 204, 181, 203), stop:1 rgba(92, 96, 184, 215));\n"
"	selection-color: rgb(198, 255, 209);\n"
"}\n"
"QCalendarWidget QAbstractItemView:disabled {\n"
"	color: rgb(104,104,104);\n"
"}\n"
"QCalendarWidget QTableView{\n"
"	outline: 0;\n"
"}\n"
"QCalendarWidget QMenu{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(82, 124, 148, 255), stop:0.457627 rgba(46, 78, 121, 255), stop:0.542373 rgba(36, 66, 113, 255), stop:0.79096 rgba(42, 98, 123, 255), stop:1 rgba(125, 164, 203, 255));\n"
"	color: #eee;\n"
"	border: 1px solid qlineargradient(spread:repeat, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(70, 124, 160, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QCalendarWidget QMenu::item{\n"
"	font-family: \"Noto Sans\";\n"
"	font-size: "
                        "13pt;\n"
"	padding: 8px 25px;\n"
"}\n"
"QCalendarWidget QMenu::item:selected{\n"
"	background-color: rgb(27, 51, 106);\n"
"}\n"
"QCalendarWidget QSpinBox::up-button {\n"
"	subcontrol-origin: border;\n"
"	subcontrol-position: top right;\n"
"	top: -5px;\n"
"	width: 24px;\n"
"	height: 24px;\n"
"	border-image: url(:/icons/icons/chevron-up.svg) 1;\n"
"	border-width: 1px;\n"
"}\n"
"QCalendarWidget QSpinBox::down-button {\n"
"	subcontrol-origin: border;\n"
"	subcontrol-position: bottom right;\n"
"	bottom: -5px;\n"
"	width: 24px;\n"
"	height: 24px;\n"
"	border-image: url(:/icons/icons/chevron-down.svg) 1;\n"
"	border-width: 1px;\n"
"	border-top-width: 0;\n"
"}")
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)

        self.verticalLayout_28.addWidget(self.calendarWidget)

        self.selectTime = QFrame(self.calendarContainer)
        self.selectTime.setObjectName(u"selectTime")
        self.selectTime.setFrameShape(QFrame.StyledPanel)
        self.selectTime.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.selectTime)
        self.verticalLayout_33.setSpacing(20)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 10, 0, 0)
        self.checkEveryday = QCheckBox(self.selectTime)
        self.checkEveryday.setObjectName(u"checkEveryday")
        font6 = QFont()
        font6.setFamily(u"Century Gothic")
        font6.setPointSize(18)
        font6.setBold(False)
        font6.setWeight(50)
        self.checkEveryday.setFont(font6)
        self.checkEveryday.setStyleSheet(u"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icons/icons/square.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icons/icons/check-square.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"	width: 30px;\n"
"	height: 30px;\n"
"}")

        self.verticalLayout_33.addWidget(self.checkEveryday, 0, Qt.AlignLeft)

        self.timeEdit = QTimeEdit(self.selectTime)
        self.timeEdit.setObjectName(u"timeEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.timeEdit.sizePolicy().hasHeightForWidth())
        self.timeEdit.setSizePolicy(sizePolicy3)
        self.timeEdit.setMinimumSize(QSize(100, 0))
        font7 = QFont()
        font7.setFamily(u"Century Gothic")
        font7.setPointSize(22)
        font7.setBold(False)
        font7.setWeight(50)
        self.timeEdit.setFont(font7)
        self.timeEdit.setStyleSheet(u"#timeEdit::up-button {\n"
"	subcontrol-origin: border;\n"
"	subcontrol-position: top right;\n"
"	top: -8px;\n"
"	width: 24px;\n"
"	height: 24px;\n"
"	border-image: url(:/icons/icons/chevron-up.svg) 1;\n"
"	border-width: 1px;\n"
"}\n"
"#timeEdit::down-button {\n"
"	subcontrol-origin: border;\n"
"	subcontrol-position: bottom right;\n"
"	bottom: -8px;\n"
"	width: 24px;\n"
"	height: 24px;\n"
"	border-image: url(:/icons/icons/chevron-down.svg) 1;\n"
"	border-width: 1px;\n"
"	border-top-width: 0;\n"
"}")
        self.timeEdit.setFrame(True)
        self.timeEdit.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.timeEdit.setMaximumTime(QTime(23, 59, 59))

        self.verticalLayout_33.addWidget(self.timeEdit, 0, Qt.AlignLeft)


        self.verticalLayout_28.addWidget(self.selectTime)


        self.horizontalLayout_21.addWidget(self.calendarContainer, 0, Qt.AlignHCenter)

        self.audioRecordedContainer_2 = QFrame(self.schedulePageBody)
        self.audioRecordedContainer_2.setObjectName(u"audioRecordedContainer_2")
        self.audioRecordedContainer_2.setMaximumSize(QSize(250, 450))
        self.audioRecordedContainer_2.setFrameShape(QFrame.StyledPanel)
        self.audioRecordedContainer_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.audioRecordedContainer_2)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(2, 2, 2, 2)
        self.labelRecordedAudio_2 = QLabel(self.audioRecordedContainer_2)
        self.labelRecordedAudio_2.setObjectName(u"labelRecordedAudio_2")
        self.labelRecordedAudio_2.setFont(font3)
        self.labelRecordedAudio_2.setScaledContents(False)
        self.labelRecordedAudio_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.labelRecordedAudio_2)

        self.listRecordedAudio_2 = QListWidget(self.audioRecordedContainer_2)
        self.listRecordedAudio_2.setObjectName(u"listRecordedAudio_2")
        self.listRecordedAudio_2.setMinimumSize(QSize(180, 0))
        self.listRecordedAudio_2.setFont(font2)
        self.listRecordedAudio_2.setStyleSheet(u"QListWidget:item {\n"
"	padding: 4px 0px;\n"
"}")

        self.verticalLayout_29.addWidget(self.listRecordedAudio_2)


        self.horizontalLayout_21.addWidget(self.audioRecordedContainer_2, 0, Qt.AlignHCenter)


        self.verticalLayout_30.addWidget(self.schedulePageBody)

        self.schedulePageFooter = QFrame(self.frame_4)
        self.schedulePageFooter.setObjectName(u"schedulePageFooter")
        self.schedulePageFooter.setFrameShape(QFrame.StyledPanel)
        self.schedulePageFooter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.schedulePageFooter)
        self.verticalLayout_31.setSpacing(25)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 15, 0, 5)
        self.volumeSetFrame_2 = QFrame(self.schedulePageFooter)
        self.volumeSetFrame_2.setObjectName(u"volumeSetFrame_2")
        self.volumeSetFrame_2.setFrameShape(QFrame.StyledPanel)
        self.volumeSetFrame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.volumeSetFrame_2)
        self.horizontalLayout_24.setSpacing(10)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(2, 5, 2, 2)
        self.btnVolume_2 = QPushButton(self.volumeSetFrame_2)
        self.btnVolume_2.setObjectName(u"btnVolume_2")
        self.btnVolume_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnVolume_2.setIcon(icon16)
        self.btnVolume_2.setIconSize(QSize(28, 28))
        self.btnVolume_2.setCheckable(True)

        self.horizontalLayout_24.addWidget(self.btnVolume_2)

        self.volumeSlider_2 = QSlider(self.volumeSetFrame_2)
        self.volumeSlider_2.setObjectName(u"volumeSlider_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.volumeSlider_2.sizePolicy().hasHeightForWidth())
        self.volumeSlider_2.setSizePolicy(sizePolicy4)
        self.volumeSlider_2.setMinimumSize(QSize(300, 28))
        self.volumeSlider_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.volumeSlider_2.setStyleSheet(u"QSlider::groove:horizontal{\n"
"	height: 2px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.083, y1:0.177, x2:0.762, y2:0.534, stop:0 rgba(192, 210, 218, 255), stop:0.19774 rgba(125, 202, 194, 255), stop:0.59322 rgba(95, 145, 182, 255), stop:1 rgba(125, 202, 194, 255));\n"
"	margin: 10px 0px;\n"
"}\n"
"QSlider::groove:horizontal:disabled{\n"
"	background-color: #666;\n"
"}\n"
"QSlider::handle:horizontal{\n"
"	background-color: qlineargradient(spread:repeat, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(199, 215, 226, 255), stop:1 rgba(102, 142, 255, 255));\n"
"	width: 8px;\n"
"	margin: -10px 0px;\n"
"	border-radius: 4px;\n"
"}\n"
"QSlider::handle:horizontal:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.336158, y1:0.034, x2:0.63, y2:0.972, stop:0 rgba(149, 180, 134, 255), stop:0.316384 rgba(92, 168, 54, 255), stop:0.621469 rgba(79, 155, 41, 255), stop:1 rgba(216, 251, 199, 255));\n"
"}\n"
"QSlider::handle:horizontal:disabled{\n"
"	background-color: #aaa;\n"
"}")
        self.volumeSlider_2.setMaximum(100)
        self.volumeSlider_2.setValue(100)
        self.volumeSlider_2.setOrientation(Qt.Horizontal)

        self.horizontalLayout_24.addWidget(self.volumeSlider_2)

        self.labelVolume_2 = QLabel(self.volumeSetFrame_2)
        self.labelVolume_2.setObjectName(u"labelVolume_2")
        self.labelVolume_2.setMinimumSize(QSize(30, 0))
        self.labelVolume_2.setFont(font)
        self.labelVolume_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_24.addWidget(self.labelVolume_2)


        self.verticalLayout_31.addWidget(self.volumeSetFrame_2, 0, Qt.AlignHCenter)

        self.frame_12 = QFrame(self.schedulePageFooter)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.btnAddToSchedule = QPushButton(self.frame_12)
        self.btnAddToSchedule.setObjectName(u"btnAddToSchedule")
        self.btnAddToSchedule.setMinimumSize(QSize(0, 40))
        self.btnAddToSchedule.setFont(font4)
        self.btnAddToSchedule.setCursor(QCursor(Qt.PointingHandCursor))
        icon18 = QIcon()
        icon18.addFile(u":/icons/icons/play-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAddToSchedule.setIcon(icon18)
        self.btnAddToSchedule.setIconSize(QSize(28, 28))

        self.horizontalLayout_23.addWidget(self.btnAddToSchedule, 0, Qt.AlignHCenter)


        self.verticalLayout_31.addWidget(self.frame_12)


        self.verticalLayout_30.addWidget(self.schedulePageFooter)


        self.horizontalLayout_12.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.mainSchedulePage)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_6)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.ListScheduleContainer = QFrame(self.frame_6)
        self.ListScheduleContainer.setObjectName(u"ListScheduleContainer")
        self.ListScheduleContainer.setMaximumSize(QSize(250, 450))
        self.ListScheduleContainer.setFrameShape(QFrame.StyledPanel)
        self.ListScheduleContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.ListScheduleContainer)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(2, 2, 2, 2)
        self.labelListSchedule = QLabel(self.ListScheduleContainer)
        self.labelListSchedule.setObjectName(u"labelListSchedule")
        self.labelListSchedule.setFont(font3)
        self.labelListSchedule.setScaledContents(False)
        self.labelListSchedule.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.labelListSchedule)

        self.listSchedule = QListWidget(self.ListScheduleContainer)
        self.listSchedule.setObjectName(u"listSchedule")
        self.listSchedule.setMinimumSize(QSize(180, 0))
        self.listSchedule.setFont(font2)
        self.listSchedule.setStyleSheet(u"QListWidget:item {\n"
"	padding: 4px 0px;\n"
"}")

        self.verticalLayout_34.addWidget(self.listSchedule)


        self.verticalLayout_35.addWidget(self.ListScheduleContainer)


        self.horizontalLayout_12.addWidget(self.frame_6, 0, Qt.AlignHCenter)

        self.mainPage.addWidget(self.mainSchedulePage)

        self.verticalLayout_15.addWidget(self.mainPage)


        self.horizontalLayout_8.addWidget(self.main_contents_container)

        self.right_menu_container = QCustomSlideMenu(self.content_container)
        self.right_menu_container.setObjectName(u"right_menu_container")
        self.right_menu_container.setMinimumSize(QSize(202, 0))
        self.right_menu_container.setMaximumSize(QSize(202, 460))
        self.verticalLayout_11 = QVBoxLayout(self.right_menu_container)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(1, 1, 1, 1)
        self.right_menu_sub_container = QWidget(self.right_menu_container)
        self.right_menu_sub_container.setObjectName(u"right_menu_sub_container")
        self.right_menu_sub_container.setMinimumSize(QSize(200, 0))
        self.right_menu_sub_container.setMaximumSize(QSize(200, 458))
        self.verticalLayout_12 = QVBoxLayout(self.right_menu_sub_container)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.frame_right_menu = QFrame(self.right_menu_sub_container)
        self.frame_right_menu.setObjectName(u"frame_right_menu")
        self.frame_right_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_right_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_right_menu)
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(18, 6, 6, 6)
        self.rightMenuLabel = QLabel(self.frame_right_menu)
        self.rightMenuLabel.setObjectName(u"rightMenuLabel")
        self.rightMenuLabel.setFont(font)

        self.horizontalLayout_9.addWidget(self.rightMenuLabel)

        self.closeRightMenuBtn = QPushButton(self.frame_right_menu)
        self.closeRightMenuBtn.setObjectName(u"closeRightMenuBtn")
        self.closeRightMenuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeRightMenuBtn.setIcon(icon10)
        self.closeRightMenuBtn.setIconSize(QSize(28, 28))

        self.horizontalLayout_9.addWidget(self.closeRightMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.frame_right_menu)

        self.rightMenuPage = QCustomStackedWidget(self.right_menu_sub_container)
        self.rightMenuPage.setObjectName(u"rightMenuPage")
        self.rightMenuProfilePage = QWidget()
        self.rightMenuProfilePage.setObjectName(u"rightMenuProfilePage")
        self.verticalLayout_13 = QVBoxLayout(self.rightMenuProfilePage)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(4, 14, 4, 6)
        self.profile_content = QLabel(self.rightMenuProfilePage)
        self.profile_content.setObjectName(u"profile_content")
        self.profile_content.setFont(font1)
        self.profile_content.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.profile_content.setWordWrap(True)

        self.verticalLayout_13.addWidget(self.profile_content)

        self.rightMenuPage.addWidget(self.rightMenuProfilePage)
        self.rightMenuMorePage = QWidget()
        self.rightMenuMorePage.setObjectName(u"rightMenuMorePage")
        self.verticalLayout_14 = QVBoxLayout(self.rightMenuMorePage)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(4, 14, 4, 6)
        self.label_8 = QLabel(self.rightMenuMorePage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_8)

        self.rightMenuPage.addWidget(self.rightMenuMorePage)

        self.verticalLayout_12.addWidget(self.rightMenuPage)


        self.verticalLayout_11.addWidget(self.right_menu_sub_container)


        self.horizontalLayout_8.addWidget(self.right_menu_container, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.content_container)

        self.popup_notification_container = QCustomSlideMenu(self.content_widget)
        self.popup_notification_container.setObjectName(u"popup_notification_container")
        self.verticalLayout_19 = QVBoxLayout(self.popup_notification_container)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.popup_notification_sub_container = QWidget(self.popup_notification_container)
        self.popup_notification_sub_container.setObjectName(u"popup_notification_sub_container")
        self.verticalLayout_20 = QVBoxLayout(self.popup_notification_sub_container)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(6, 6, 6, 12)
        self.label_13 = QLabel(self.popup_notification_sub_container)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)
        self.label_13.setStyleSheet(u"padding-left: 5px;")
        self.label_13.setScaledContents(False)

        self.verticalLayout_20.addWidget(self.label_13)

        self.frame_7 = QFrame(self.popup_notification_sub_container)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(6, 6, 6, 6)
        self.notification_content = QLabel(self.frame_7)
        self.notification_content.setObjectName(u"notification_content")
        sizePolicy1.setHeightForWidth(self.notification_content.sizePolicy().hasHeightForWidth())
        self.notification_content.setSizePolicy(sizePolicy1)
        self.notification_content.setFont(font)
        self.notification_content.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.notification_content)

        self.closeNotificationBtn = QPushButton(self.frame_7)
        self.closeNotificationBtn.setObjectName(u"closeNotificationBtn")
        self.closeNotificationBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon19 = QIcon()
        icon19.addFile(u":/icons/icons/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeNotificationBtn.setIcon(icon19)
        self.closeNotificationBtn.setIconSize(QSize(28, 28))

        self.horizontalLayout_10.addWidget(self.closeNotificationBtn, 0, Qt.AlignRight)


        self.verticalLayout_20.addWidget(self.frame_7)


        self.verticalLayout_19.addWidget(self.popup_notification_sub_container)


        self.verticalLayout_10.addWidget(self.popup_notification_container)

        self.footer_container = QWidget(self.content_widget)
        self.footer_container.setObjectName(u"footer_container")
        self.horizontalLayout_7 = QHBoxLayout(self.footer_container)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.footer_container)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 50))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_8)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.dateShowLabel = QLabel(self.frame_8)
        self.dateShowLabel.setObjectName(u"dateShowLabel")
        self.dateShowLabel.setFont(font)
        self.dateShowLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.dateShowLabel, 0, Qt.AlignRight)

        self.timeShowLabel = QLabel(self.frame_8)
        self.timeShowLabel.setObjectName(u"timeShowLabel")
        self.timeShowLabel.setFont(font)

        self.horizontalLayout.addWidget(self.timeShowLabel, 0, Qt.AlignLeft)


        self.horizontalLayout_7.addWidget(self.frame_8)

        self.bottom_logo_container = QFrame(self.footer_container)
        self.bottom_logo_container.setObjectName(u"bottom_logo_container")
        self.bottom_logo_container.setMaximumSize(QSize(200, 16777215))
        self.bottom_logo_container.setFrameShape(QFrame.StyledPanel)
        self.bottom_logo_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.bottom_logo_container)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.bottom_logo_container)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        icon20 = QIcon()
        icon20.addFile(u":/images/images/EVERCON.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon20)
        self.pushButton.setIconSize(QSize(160, 20))

        self.horizontalLayout_4.addWidget(self.pushButton)


        self.horizontalLayout_7.addWidget(self.bottom_logo_container)


        self.verticalLayout_10.addWidget(self.footer_container)


        self.horizontalLayout_13.addWidget(self.content_widget)

        self.center_menu.raise_()
        self.content_widget.raise_()
        self.sidebar_widget.raise_()

        self.verticalLayout_44.addWidget(self.body_container)

        self.centralStackedWidget.addWidget(self.mainScreen)
        self.startScreen = QWidget()
        self.startScreen.setObjectName(u"startScreen")
        self.startScreen.setStyleSheet(u"")
        self.backgroundLabel = QLabel(self.startScreen)
        self.backgroundLabel.setObjectName(u"backgroundLabel")
        self.backgroundLabel.setGeometry(QRect(0, 0, 1280, 720))
        self.backgroundLabel.setMinimumSize(QSize(1280, 720))
        self.backgroundLabel.setMaximumSize(QSize(1280, 720))
        self.backgroundLabel.setPixmap(QPixmap(u":/images/images/wallpaper-blue-hd.jpg"))
        self.backgroundLabel.setScaledContents(True)
        self.logoLabel = QLabel(self.startScreen)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setGeometry(QRect(170, 80, 281, 161))
        self.logoLabel.setPixmap(QPixmap(u":/images/images/EVERCON 2nd style.png"))
        self.logoLabel.setScaledContents(True)
        self.commanderLabel = QLabel(self.startScreen)
        self.commanderLabel.setObjectName(u"commanderLabel")
        self.commanderLabel.setGeometry(QRect(240, 280, 441, 71))
        font8 = QFont()
        font8.setFamily(u"Poppins Medium")
        font8.setPointSize(50)
        font8.setBold(False)
        font8.setWeight(50)
        self.commanderLabel.setFont(font8)
        self.commanderLabel.setStyleSheet(u"color: rgb(167, 217, 255);")
        self.firstStartBtn = QPushButton(self.startScreen)
        self.firstStartBtn.setObjectName(u"firstStartBtn")
        self.firstStartBtn.setGeometry(QRect(850, 430, 211, 71))
        font9 = QFont()
        font9.setFamily(u"Noto Sans")
        font9.setPointSize(32)
        font9.setBold(True)
        font9.setWeight(75)
        self.firstStartBtn.setFont(font9)
        self.firstStartBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon21 = QIcon()
        icon21.addFile(u":/images/images/arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.firstStartBtn.setIcon(icon21)
        self.firstStartBtn.setIconSize(QSize(150, 80))
        self.centralStackedWidget.addWidget(self.startScreen)

        self.verticalLayout_21.addWidget(self.centralStackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.centralStackedWidget.setCurrentIndex(1)
        self.centerMenuPage.setCurrentIndex(0)
        self.mainPage.setCurrentIndex(0)
        self.rightMenuPage.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.btnNotification.setToolTip(QCoreApplication.translate("MainWindow", u"Show Notification", None))
#endif // QT_CONFIG(tooltip)
        self.btnNotification.setText("")
#if QT_CONFIG(tooltip)
        self.btnMore.setToolTip(QCoreApplication.translate("MainWindow", u"More", None))
#endif // QT_CONFIG(tooltip)
        self.btnMore.setText("")
#if QT_CONFIG(tooltip)
        self.btnProfile.setToolTip(QCoreApplication.translate("MainWindow", u"Profile", None))
#endif // QT_CONFIG(tooltip)
        self.btnProfile.setText("")
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.btnHome.setToolTip(QCoreApplication.translate("MainWindow", u"Go to home", None))
#endif // QT_CONFIG(tooltip)
        self.btnHome.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.btnDataAnalysis.setToolTip(QCoreApplication.translate("MainWindow", u"Data Analysis", None))
#endif // QT_CONFIG(tooltip)
        self.btnDataAnalysis.setText(QCoreApplication.translate("MainWindow", u"Data Analysis", None))
#if QT_CONFIG(tooltip)
        self.btnReports.setToolTip(QCoreApplication.translate("MainWindow", u"Show Reports", None))
#endif // QT_CONFIG(tooltip)
        self.btnReports.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
#if QT_CONFIG(tooltip)
        self.btnSettings.setToolTip(QCoreApplication.translate("MainWindow", u"Go to settings", None))
#endif // QT_CONFIG(tooltip)
        self.btnSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.btnInfo.setToolTip(QCoreApplication.translate("MainWindow", u"Show information about the application", None))
#endif // QT_CONFIG(tooltip)
        self.btnInfo.setText(QCoreApplication.translate("MainWindow", u"Information", None))
#if QT_CONFIG(tooltip)
        self.btnHelp.setToolTip(QCoreApplication.translate("MainWindow", u"Get more help", None))
#endif // QT_CONFIG(tooltip)
        self.btnHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.moreMenuLabel.setText(QCoreApplication.translate("MainWindow", u"More Menu", None))
#if QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.help_content.setText(QCoreApplication.translate("MainWindow", u"Help", None))
#if QT_CONFIG(tooltip)
        self.btnZones.setToolTip(QCoreApplication.translate("MainWindow", u"Zones", None))
#endif // QT_CONFIG(tooltip)
        self.btnZones.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"ZONES", None))
#if QT_CONFIG(tooltip)
        self.btnCamera.setToolTip(QCoreApplication.translate("MainWindow", u"Cameras", None))
#endif // QT_CONFIG(tooltip)
        self.btnCamera.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"CAMERAS", None))
#if QT_CONFIG(tooltip)
        self.btnFieldStations.setToolTip(QCoreApplication.translate("MainWindow", u"Field Stations", None))
#endif // QT_CONFIG(tooltip)
        self.btnFieldStations.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"FIELD STATIONS", None))
#if QT_CONFIG(tooltip)
        self.btnSchedule.setToolTip(QCoreApplication.translate("MainWindow", u"Schedule", None))
#endif // QT_CONFIG(tooltip)
        self.btnSchedule.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"SCHEDULE", None))
#if QT_CONFIG(tooltip)
        self.btnRecord.setToolTip(QCoreApplication.translate("MainWindow", u"Record", None))
#endif // QT_CONFIG(tooltip)
        self.btnRecord.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"RECORD", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Data Analysis", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.radioMic.setText(QCoreApplication.translate("MainWindow", u"Mic", None))
        self.radioRecorded.setText(QCoreApplication.translate("MainWindow", u"Recorded", None))
        self.labelZones.setText(QCoreApplication.translate("MainWindow", u"ZONES", None))
        self.lobbyLabel.setText(QCoreApplication.translate("MainWindow", u"Lobby Area", None))
        self.lobbyCheck.setText("")
        self.pantryLabel.setText(QCoreApplication.translate("MainWindow", u"PANTRY", None))
        self.pantryCheck.setText("")
        self.accountsLabel.setText(QCoreApplication.translate("MainWindow", u"Accounts Section", None))
        self.accountsCheck.setText("")
        self.mainOfficeLabel.setText(QCoreApplication.translate("MainWindow", u"Main Office", None))
        self.mainOfficeCheck.setText("")
        self.gate1Label.setText(QCoreApplication.translate("MainWindow", u"Gate 1", None))
        self.gate1Check.setText("")
        self.gate2Label.setText(QCoreApplication.translate("MainWindow", u"Gate 2", None))
        self.gate2Check.setText("")
        self.labelRecordedAudio.setText(QCoreApplication.translate("MainWindow", u"SELECT AUDIO", None))
        self.btnVolume.setText("")
        self.labelVolume.setText(QCoreApplication.translate("MainWindow", u"100", None))
#if QT_CONFIG(tooltip)
        self.btnStart.setToolTip(QCoreApplication.translate("MainWindow", u"Play audio", None))
#endif // QT_CONFIG(tooltip)
        self.btnStart.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.radioMicInField.setText(QCoreApplication.translate("MainWindow", u"Mic", None))
        self.radioRecordedInField.setText(QCoreApplication.translate("MainWindow", u"Recorded", None))
        self.labelFieldList.setText(QCoreApplication.translate("MainWindow", u"FIELD STATIONS/IP SPEAKERS ", None))
        self.label_ip_ext.setText(QCoreApplication.translate("MainWindow", u" IP Address                                            Extension", None))

        __sortingEnabled = self.listField.isSortingEnabled()
        self.listField.setSortingEnabled(False)
        ___qlistwidgetitem = self.listField.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"192.168.1.10                                2383", None));
        ___qlistwidgetitem1 = self.listField.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"192.168.34.10                              2545", None));
        ___qlistwidgetitem2 = self.listField.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"192.168.6.12                                3433", None));
        ___qlistwidgetitem3 = self.listField.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"192.168.61.1                                3443", None));
        self.listField.setSortingEnabled(__sortingEnabled)

        self.labelRecordedAudio_3.setText(QCoreApplication.translate("MainWindow", u"SELECT AUDIO", None))
        self.btnVolume_3.setText("")
        self.labelVolume_3.setText(QCoreApplication.translate("MainWindow", u"100", None))
#if QT_CONFIG(tooltip)
        self.btnStartInField.setToolTip(QCoreApplication.translate("MainWindow", u"Play audio", None))
#endif // QT_CONFIG(tooltip)
        self.btnStartInField.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.checkEveryday.setText(QCoreApplication.translate("MainWindow", u"Every day", None))
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"hh:mm AP", None))
        self.labelRecordedAudio_2.setText(QCoreApplication.translate("MainWindow", u"SELECT AUDIO", None))
        self.btnVolume_2.setText("")
        self.labelVolume_2.setText(QCoreApplication.translate("MainWindow", u"100", None))
#if QT_CONFIG(tooltip)
        self.btnAddToSchedule.setToolTip(QCoreApplication.translate("MainWindow", u"Play audio", None))
#endif // QT_CONFIG(tooltip)
        self.btnAddToSchedule.setText(QCoreApplication.translate("MainWindow", u"Add to SCHEDULE", None))
        self.labelListSchedule.setText(QCoreApplication.translate("MainWindow", u"List of schedules", None))
        self.rightMenuLabel.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
#if QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setText("")
        self.profile_content.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"More...", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.notification_content.setText(QCoreApplication.translate("MainWindow", u"There are no active alarms from the field", None))
#if QT_CONFIG(tooltip)
        self.closeNotificationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Notification", None))
#endif // QT_CONFIG(tooltip)
        self.closeNotificationBtn.setText("")
        self.dateShowLabel.setText(QCoreApplication.translate("MainWindow", u"xx/xx/xxxx", None))
        self.timeShowLabel.setText(QCoreApplication.translate("MainWindow", u"xx:xx xx", None))
        self.pushButton.setText("")
        self.logoLabel.setText("")
        self.commanderLabel.setText(QCoreApplication.translate("MainWindow", u"COMMANDER", None))
        self.firstStartBtn.setText("")
    # retranslateUi

