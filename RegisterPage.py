# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegisterPage.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 463)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(320, 80, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(320, 150, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(320, 220, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(320, 290, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textEdit_4.setFont(font)
        self.textEdit_4.setObjectName("textEdit_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 0, 431, 71))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnRegister = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegister.setGeometry(QtCore.QRect(310, 360, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btnRegister.setFont(font)
        self.btnRegister.setObjectName("btnRegister")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(640, 370, 47, 13))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(80, 80, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 150, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 230, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 300, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.btnBack = QtWidgets.QPushButton(self.centralwidget)
        self.btnBack.setGeometry(QtCore.QRect(560, 360, 221, 51))
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
        self.label.setText(_translate("MainWindow", "                                  REGISTER"))
        self.btnRegister.setText(_translate("MainWindow", "CLICK TO REGISTER"))
        self.label_7.setText(_translate("MainWindow", "           Faculty ID"))
        self.label_2.setText(_translate("MainWindow", "          First Name"))
        self.label_3.setText(_translate("MainWindow", "          Middle Name"))
        self.label_4.setText(_translate("MainWindow", "           Last Name"))
        self.btnBack.setText(_translate("MainWindow", "BACK"))
