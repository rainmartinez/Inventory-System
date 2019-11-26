

# Form implementation generated from reading ui file 'ViewAllMembersPage.ui'
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
        self.btnSearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnSearch.setGeometry(QtCore.QRect(80, 90, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btnSearch.setFont(font)
        self.btnSearch.setObjectName("btnSearch")
        self.btnSelect = QtWidgets.QPushButton(self.centralwidget)
        self.btnSelect.setGeometry(QtCore.QRect(70, 170, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btnSelect.setFont(font)
        self.btnSelect.setObjectName("btnSelect")
        self.textSearch = QtWidgets.QTextEdit(self.centralwidget)
        self.textSearch.setGeometry(QtCore.QRect(60, 40, 191, 31))
        self.textSearch.setObjectName("textSearch")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(320, 30, 181, 361))
        self.listWidget.setObjectName("listWidget")
        self.btnRemove = QtWidgets.QPushButton(self.centralwidget)
        self.btnRemove.setGeometry(QtCore.QRect(70, 280, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btnRemove.setFont(font)
        self.btnRemove.setObjectName("btnSelect_2")
        self.btnBack = QtWidgets.QPushButton(self.centralwidget)
        self.btnBack.setGeometry(QtCore.QRect(90, 380, 151, 51))
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
        self.btnSearch.setText(_translate("MainWindow", "Search "))
        self.btnSelect.setText(_translate("MainWindow", "Select Member"))
        self.btnRemove.setText(_translate("MainWindow", "Remove Member"))
        self.btnBack.setText(_translate("MainWindow", "Back"))

