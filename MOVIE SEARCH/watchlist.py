# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'watchlist.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.lstWatchList = QtWidgets.QListWidget(Dialog)
        self.lstWatchList.setGeometry(QtCore.QRect(20, 71, 151, 221))
        self.lstWatchList.setObjectName("lstWatchList")
        self.btnGoBack = QtWidgets.QToolButton(Dialog)
        self.btnGoBack.setGeometry(QtCore.QRect(190, 230, 181, 51))
        self.btnGoBack.setObjectName("btnGoBack")
        self.btnWatch = QtWidgets.QPushButton(Dialog)
        self.btnWatch.setGeometry(QtCore.QRect(190, 170, 181, 51))
        self.btnWatch.setObjectName("btnWatch")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnGoBack.setText(_translate("Dialog", "Go Back"))
        self.btnWatch.setText(_translate("Dialog", "Watched!"))
        self.label.setText(_translate("Dialog", "Watch List"))

