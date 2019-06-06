# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tvform.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 646)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 20, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.lstEpi = QtWidgets.QListWidget(self.centralwidget)
        self.lstEpi.setGeometry(QtCore.QRect(320, 350, 181, 241))
        self.lstEpi.setObjectName("lstEpi")
        self.lblPoster = QtWidgets.QLabel(self.centralwidget)
        self.lblPoster.setGeometry(QtCore.QRect(10, 220, 281, 381))
        self.lblPoster.setObjectName("lblPoster")
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(40, 80, 721, 81))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.lblTitle.setFont(font)
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.btnGo = QtWidgets.QPushButton(self.centralwidget)
        self.btnGo.setGeometry(QtCore.QRect(510, 340, 75, 41))
        self.btnGo.setObjectName("btnGo")
        self.lblEpi = QtWidgets.QLabel(self.centralwidget)
        self.lblEpi.setGeometry(QtCore.QRect(330, 310, 161, 21))
        self.lblEpi.setObjectName("lblEpi")
        self.btnExtra = QtWidgets.QPushButton(self.centralwidget)
        self.btnExtra.setGeometry(QtCore.QRect(590, 500, 181, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnExtra.setFont(font)
        self.btnExtra.setObjectName("btnExtra")
        self.txtSearch = QtWidgets.QTextEdit(self.centralwidget)
        self.txtSearch.setGeometry(QtCore.QRect(250, 160, 271, 41))
        self.txtSearch.setObjectName("txtSearch")
        self.btnSearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnSearch.setGeometry(QtCore.QRect(530, 160, 131, 41))
        self.btnSearch.setObjectName("btnSearch")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionGo_Back = QtWidgets.QAction(MainWindow)
        self.actionGo_Back.setObjectName("actionGo_Back")
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addAction(self.actionGo_Back)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TV Show Search"))
        self.lblPoster.setText(_translate("MainWindow", "TextLabel"))
        self.lblTitle.setText(_translate("MainWindow", "Title"))
        self.btnGo.setText(_translate("MainWindow", "Search"))
        self.lblEpi.setText(_translate("MainWindow", "Seasons/Episode"))
        self.btnExtra.setText(_translate("MainWindow", "Extra Information"))
        self.btnSearch.setText(_translate("MainWindow", "Search"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionGo_Back.setText(_translate("MainWindow", "Go Back"))

