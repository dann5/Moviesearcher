# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Search.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SearchForm(object):
    def setupUi(self, SearchForm):
        SearchForm.setObjectName("SearchForm")
        SearchForm.resize(386, 147)
        self.formLayout = QtWidgets.QFormLayout(SearchForm)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(SearchForm)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.btnSearch = QtWidgets.QPushButton(SearchForm)
        self.btnSearch.setObjectName("btnSearch")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.btnSearch)
        self.btnGoback = QtWidgets.QPushButton(SearchForm)
        self.btnGoback.setObjectName("btnGoback")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.btnGoback)
        self.txtSearch = QtWidgets.QTextEdit(SearchForm)
        self.txtSearch.setObjectName("txtSearch")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.txtSearch)

        self.retranslateUi(SearchForm)
        QtCore.QMetaObject.connectSlotsByName(SearchForm)
    def retranslateUi(self, SearchForm):
        _translate = QtCore.QCoreApplication.translate
        SearchForm.setWindowTitle(_translate("SearchForm", "Search Movie"))
        self.label.setText(_translate("SearchForm", "Search a movie!"))
        self.btnSearch.setText(_translate("SearchForm", "Search"))
        self.btnGoback.setText(_translate("SearchForm", "Go Back"))
        self.txtSearch.setHtml(_translate("SearchForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


