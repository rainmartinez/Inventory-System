# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ViewAllItemsPage.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 544)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnSelect_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnSelect_2.setGeometry(QtCore.QRect(110, 300, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btnSelect_2.setFont(font)
        self.btnSelect_2.setObjectName("btnSelect_2")
        self.btnSelect = QtWidgets.QPushButton(self.centralwidget)
        self.btnSelect.setGeometry(QtCore.QRect(110, 190, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btnSelect.setFont(font)
        self.btnSelect.setObjectName("btnSelect")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(360, 50, 181, 361))
        self.listWidget.setObjectName("listWidget")
        self.textSearch = QtWidgets.QTextEdit(self.centralwidget)
        self.textSearch.setGeometry(QtCore.QRect(100, 60, 191, 31))
        self.textSearch.setObjectName("textSearch")
        self.btnSearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnSearch.setGeometry(QtCore.QRect(120, 110, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btnSearch.setFont(font)
        self.btnSearch.setObjectName("btnSearch")
        self.btnBack = QtWidgets.QPushButton(self.centralwidget)
        self.btnBack.setGeometry(QtCore.QRect(130, 400, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btnBack.setFont(font)
        self.btnBack.setObjectName("btnBack")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnSelect_2.setText(_translate("MainWindow", "Remove Item"))
        self.btnSelect.setText(_translate("MainWindow", "Select Item"))
        self.btnSearch.setText(_translate("MainWindow", "Search "))
        self.btnBack.setText(_translate("MainWindow", "Back"))

