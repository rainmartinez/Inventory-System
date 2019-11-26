# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(758, 565)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnViewAllItems = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnViewAllItems.setFont(font)
        self.btnViewAllItems.setObjectName("btnViewAllItems")
        self.verticalLayout.addWidget(self.btnViewAllItems)
        self.btnAddItem = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnAddItem.setFont(font)
        self.btnAddItem.setObjectName("btnAddItem")
        self.verticalLayout.addWidget(self.btnAddItem)
        self.btnGenerate = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnGenerate.setFont(font)
        self.btnGenerate.setObjectName("btnGenerate")
        self.verticalLayout.addWidget(self.btnGenerate)
        self.btnViewAllRegistered = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnViewAllRegistered.setFont(font)
        self.btnViewAllRegistered.setObjectName("btnViewAllRegistered")
        self.verticalLayout.addWidget(self.btnViewAllRegistered)
        self.btnLogout = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnLogout.setFont(font)
        self.btnLogout.setObjectName("btnLogout")
        self.verticalLayout.addWidget(self.btnLogout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnViewAllItems.setText(_translate("MainWindow", "Manage Inventory"))
        self.btnAddItem.setText(_translate("MainWindow", "Add Item"))
        self.btnGenerate.setText(_translate("MainWindow", "Generate Inventory Report"))
        self.btnViewAllRegistered.setText(_translate("MainWindow", "Manage Registered Users"))
        self.btnLogout.setText(_translate("MainWindow", "LOGOUT"))

