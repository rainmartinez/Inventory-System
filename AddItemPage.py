# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddItemPage.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 60, 321, 71))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(240, 230, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.btnItemAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnItemAdd.setGeometry(QtCore.QRect(300, 340, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btnItemAdd.setFont(font)
        self.btnItemAdd.setObjectName("btnItemAdd")
        self.btnBack = QtWidgets.QPushButton(self.centralwidget)
        self.btnBack.setGeometry(QtCore.QRect(550, 340, 151, 61))
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
        self.label.setText(_translate("MainWindow", "ITEM TO BE ADDED"))
        self.btnItemAdd.setText(_translate("MainWindow", "Add Item"))
        self.btnBack.setText(_translate("MainWindow", "Back"))

