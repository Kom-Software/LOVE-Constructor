# ·············································································
# : _________  ___  _____ ______   ________  ________    _____  ___   ___     :
# :|\___   ___\\  \|\   _ \  _   \|\   __  \|\   __  \  / __  \|\  \ |\  \    :
# :\|___ \  \_\ \  \ \  \\\__\ \  \ \  \|\  \ \  \|\  \|\/_|\  \ \  \\_\  \   :
# :     \ \  \ \ \  \ \  \\|__| \  \ \   ____\ \  \\\  \|/ \ \  \ \______  \  :
# :      \ \  \ \ \  \ \  \    \ \  \ \  \___|\ \  \\\  \   \ \  \|_____|\  \ :
# :       \ \__\ \ \__\ \__\    \ \__\ \__\    \ \_______\   \ \__\     \ \__\:
# :        \|__|  \|__|\|__|     \|__|\|__|     \|_______|    \|__|      \|__|:
# ·············································································
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os, sys
with open(os.path.dirname(__file__) + "\\Settings.json", 'r') as Settings:
    SettingsRead = Settings
    class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
            MainWindow.setObjectName("MainWindow")
            MainWindow.setwindowTitle("LOVE Constructor")
            MainWindow.resize(1280, 720)
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(12)
            MainWindow.setFont(font)
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            MainWindow.setCentralWidget(self.centralwidget)
            self.menubar = QtWidgets.QMenuBar(MainWindow)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 24))
            self.menubar.setObjectName("menubar")
            self.menuFile = QtWidgets.QMenu(self.menubar)
            self.menuFile.setObjectName("menuFile")
            self.menuOpen_Project = QtWidgets.QMenu(self.menuFile)
            self.menuOpen_Project.setObjectName("menuOpen_Project")
            self.menuSettings = QtWidgets.QMenu(self.menubar)
            self.menuSettings.setObjectName("menuSettings")
            MainWindow.setMenuBar(self.menubar)
            self.statusbar = QtWidgets.QStatusBar(MainWindow)
            self.statusbar.setObjectName("statusbar")
            MainWindow.setStatusBar(self.statusbar)
            self.actionNew_Project = QtWidgets.QAction(MainWindow)
            self.actionNew_Project.setObjectName("actionNew_Project")
            self.actionExit = QtWidgets.QAction(MainWindow)
            self.actionExit.setMenuRole(QtWidgets.QAction.QuitRole)
            self.actionExit.setObjectName("actionExit")
            self.actionGeneral = QtWidgets.QAction(MainWindow)
            self.actionGeneral.setObjectName("actionGeneral")
            self.actionTheme = QtWidgets.QAction(MainWindow)
            self.actionTheme.setObjectName("actionTheme")
            self.actionSave_Project = QtWidgets.QAction(MainWindow)
            self.actionSave_Project.setObjectName("actionSave_Project")
            self.actionIn_menu = QtWidgets.QAction(MainWindow)
            self.actionIn_menu.setObjectName("actionIn_menu")
            self.actionTestProject = QtWidgets.QAction(MainWindow)
            self.actionTestProject.setObjectName("actionTestProject")
            self.menuOpen_Project.addAction(self.actionTestProject)
            self.menuFile.addAction(self.actionNew_Project)
            self.menuFile.addAction(self.menuOpen_Project.menuAction())
            self.menuFile.addAction(self.actionSave_Project)
            self.menuFile.addAction(self.actionIn_menu)
            self.menuFile.addSeparator()
            self.menuFile.addAction(self.actionExit)
            self.menuSettings.addAction(self.actionGeneral)
            self.menuSettings.addAction(self.actionTheme)
            self.menubar.addAction(self.menuFile.menuAction())
            self.menubar.addAction(self.menuSettings.menuAction())

            self.retranslateUi(MainWindow)
            self.actionExit.triggered.connect(MainWindow.close) # type: ignore
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
            self.menuFile.setTitle(_translate("MainWindow", "File"))
            self.menuOpen_Project.setTitle(_translate("MainWindow", "Open Project"))
            self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
            self.actionNew_Project.setText(_translate("MainWindow", "New Project"))
            self.actionNew_Project.setShortcut(_translate("MainWindow", "Ctrl++"))
            self.actionExit.setText(_translate("MainWindow", "Exit"))
            self.actionExit.setShortcut(_translate("MainWindow", "Shift+Esc"))
            self.actionGeneral.setText(_translate("MainWindow", "General"))
            self.actionGeneral.setShortcut(_translate("MainWindow", "Ctrl+P"))
            self.actionTheme.setText(_translate("MainWindow", "Theme"))
            self.actionTheme.setShortcut(_translate("MainWindow", "Ctrl+T"))
            self.actionSave_Project.setText(_translate("MainWindow", "Save Project"))
            self.actionSave_Project.setShortcut(_translate("MainWindow", "Ctrl+S"))
            self.actionIn_menu.setText(_translate("MainWindow", "In menu"))
            self.actionIn_menu.setShortcut(_translate("MainWindow", "Ctrl+M"))
            self.actionTestProject.setText(_translate("MainWindow", "TestProject"))
