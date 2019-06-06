

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(588, 426)
        self.label = QtWidgets.QLabel(MainForm)
        self.label.setGeometry(QtCore.QRect(100, 10, 421, 81))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnMovie = QtWidgets.QPushButton(MainForm)
        self.btnMovie.setGeometry(QtCore.QRect(300, 250, 221, 121))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.btnMovie.setFont(font)
        self.btnMovie.setObjectName("pushButton_2")
        self.btnTv = QtWidgets.QPushButton(MainForm)
        self.btnTv.setGeometry(QtCore.QRect(30, 250, 221, 121))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.btnTv.setFont(font)
        self.btnTv.setObjectName("pushButton_3")

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Dialog"))
        self.label.setText(_translate("MainForm", "Movie/Tv Show Searcher"))
        self.btnMovie.setText(_translate("MainForm", "Movie Search"))
        self.btnTv.setText(_translate("MainForm", "Tv Search"))

