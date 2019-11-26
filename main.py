from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QAction, qApp, QMenuBar, QListWidget, QMessageBox
import HelperClass
import sys
import mysql.connector
from datetime import date, datetime, timedelta
import design
import ViewAllMembersPage
import MemberDetailsPage
import ModifyDetailsPage
import RegisterPage
import ReportListPage
import WelcomePage
import LoginPage
import AddItemPage
import ViewAllItemsPage
import ViewItemDetailsPage
import ModifyItemDetailsPage

class Welcome(QtWidgets.QMainWindow, WelcomePage.Ui_MainWindow):

    def __init__(self):
        super(Welcome, self).__init__()
        self.setupUi(self)
        self.btnRegister.clicked.connect(self.pushButtonRegister_clicked)
        self.dialog = Register()
        self.btnLogin.clicked.connect(self.pushButtonLogin_clicked)
        self.dialog2 = Login()
    def pushButtonRegister_clicked(self):
        self.close()
        self.dialog.show()
    def pushButtonLogin_clicked(self):
        self.close()
        self.dialog2.show()

class Design(QtWidgets.QMainWindow, design.Ui_MainWindow):

    def __init__(self):
        super(Design, self).__init__()
        self.setupUi(self)
        self.btnViewAllRegistered.clicked.connect(self.pushButtonViewAllRegistered_clicked)
        self.dialog = ViewAllMembers()

        self.btnLogout.clicked.connect(self.pushButtonLogout_clicked)
        

        self.btnGenerate.clicked.connect(self.pushButtonGenerate_clicked)
        self.dialog2 = ReportList()

        self.btnAddItem.clicked.connect(self.pushButtonAddItem_clicked)
        self.dialog3 = AddItem()

        self.btnViewAllItems.clicked.connect(self.pushButtonViewAllItems_clicked)
        self.dialog4 = ViewAllItems()

    def pushButtonLogout_clicked(self):
        self.dialogBack = Welcome()
        self.dialogBack.show()
        self.close()

    def pushButtonViewAllRegistered_clicked(self):
        self.close()
        self.dialog.show()

    def pushButtonGenerate_clicked(self):
        self.close()
        self.dialog = ReportList()
        self.dialog.show()

    def pushButtonAddItem_clicked(self):
        self.close()
        self.dialog3.show()

    def pushButtonViewAllItems_clicked(self):
        self.close()
        self.dialog4.show()

class ViewAllMembers(QtWidgets.QMainWindow, ViewAllMembersPage.Ui_MainWindow):
    def __init__(self):
        super(ViewAllMembers, self).__init__()
        self.setupUi(self)
        self.selectedFaculty_ID = 0
        self.btnSelect.clicked.connect(self.pushButtonSelect_clicked)
        self.btnBack.clicked.connect(self.pushButtonBack_clicked)
        self.btnRemove.clicked.connect(self.pushButtonRemove_clicked)
        self.PopulateList()

    def pushButtonRemove_clicked(self):
        if self.listWidget.currentRow() == -1:
            QMessageBox.question(self, 'No Member Selected!', "Please select a member!", QMessageBox.Ok)
        selectedItem =  self.listWidget.currentItem().text()
        self.selectedFaculty_ID = selectedItem.split('\t')[0]
        cnx = mysql.connector.connect(user='sa', password='kappa123',
                                  host='localhost',
                                  database='inventory_system')
        cursor = cnx.cursor()
        query = ("DELETE FROM faculty "
                    "WHERE faculty_id = %s")
        cursor.execute(query, (self.selectedFaculty_ID, ))
        QMessageBox.question(self, 'Success!', "Faculty Member Deleted!", QMessageBox.Ok)
        cnx.commit()
        cursor.close()
        cnx.close()
        self.PopulateList()
        
    def pushButtonBack_clicked(self):
        self.dialogBack = Design()
        self.dialogBack.show()
        self.close()

    def pushButtonSelect_clicked(self):
        if self.listWidget.currentRow() == -1:
            QMessageBox.question(self, 'No Member Selected!', "Please select a member!", QMessageBox.Ok)
        selectedItem =  self.listWidget.currentItem().text()
        self.selectedFaculty_ID = selectedItem.split('\t')[0]
        self.dialog = MemberDetails(self.selectedFaculty_ID)
        self.dialog.show()
        self.close()

    def PopulateList(self):
        self.listWidget.clear()
        cnx = mysql.connector.connect(user='sa', password='kappa123',
                                  host='localhost',
                                  database='inventory_system')
        cursor = cnx.cursor()
        query = ("SELECT faculty_id, first_name, last_name FROM faculty;")
        cursor.execute(query)
        for (faculty_id, first_name, last_name) in cursor:
          self.listWidget.addItem(str(faculty_id) + '\t' + first_name + '\t' + last_name)
        cursor.close()
        cnx.close()


class MemberDetails(QtWidgets.QMainWindow, MemberDetailsPage.Ui_MainWindow):
    def __init__(self, faculty_ID):
        super(MemberDetails, self).__init__()
        self.setupUi(self)
        self.faculty_ID = faculty_ID
        self.btnModify.clicked.connect(self.pushButtonModify_clicked)
        self.dialog = ModifyMemberDetails(self.faculty_ID)
        self.btnBack.clicked.connect(self.pushButtonBack_clicked)
        self.PopulateForm()
        
    def PopulateForm(self):
        cnx = mysql.connector.connect(user='sa', password='kappa123',
                                  host='localhost',
                                  database='inventory_system')
        cursor = cnx.cursor()
        query = ("SELECT first_name, middle_name, last_name FROM faculty WHERE faculty_id = %s;")
        cursor.execute(query, (self.faculty_ID,))
        self.textBrowser_5.setText(str(self.faculty_ID))
        for (first_name, middle_name, last_name) in cursor:
          self.textBrowser.setText(first_name)
          self.textBrowser_2.setText(middle_name)
          self.textBrowser_3.setText(last_name)
        cursor.close()
        cnx.close()

    def pushButtonModify_clicked(self):
        self.close()
        self.dialog.show()

    
    def pushButtonBack_clicked(self):
        self.dialogBack = ViewAllMembers()
        self.dialogBack.show()
        self.close()


class ModifyMemberDetails(QtWidgets.QMainWindow, ModifyDetailsPage.Ui_MainWindow):
    def __init__(self, faculty_ID):
        super(ModifyMemberDetails, self).__init__()
        self.faculty_ID = faculty_ID
        self.setupUi(self)
        self.btnDone.clicked.connect(self.pushButtonDone_clicked)
        self.PopulateForm()

    def pushButtonDone_clicked(self):
        if HelperClass.IsFaculty_IDTaken(self.editID.toPlainText()) and self.editID.toPlainText() != str(self.faculty_ID):
            QMessageBox.question(self, 'Faculty ID Taken!', "Faculty ID is already taken!", QMessageBox.Ok)
        else:
            cnx = mysql.connector.connect(user='sa', password='kappa123',
                                  host='localhost',
                                  database='inventory_system')
            cursor = cnx.cursor()
            query = ("UPDATE faculty "
                     "SET faculty_id = %s, first_name = %s, middle_name = %s, last_name = %s "
                     "WHERE faculty_id = %s")
            employeeDetails = (self.editID.toPlainText(), self.editFirst.toPlainText(), self.editMiddle.toPlainText(), self.editLast.toPlainText(), self.faculty_ID)
            cursor.execute(query, employeeDetails)
            QMessageBox.question(self, 'Success!', "Faculty Details Edited!", QMessageBox.Ok)
            cnx.commit()
            cursor.close()
            cnx.close()
            self.dialogBack = MemberDetails(self.faculty_ID)
            self.dialogBack.show()
            self.close()

    def PopulateForm(self):
        cnx = mysql.connector.connect(user='sa', password='kappa123',
                                  host='localhost',
                                  database='inventory_system')
        cursor = cnx.cursor()
        query = ("SELECT first_name, middle_name, last_name FROM faculty WHERE faculty_id = %s;")
        cursor.execute(query, (self.faculty_ID,))
        self.editID.setText(str(self.faculty_ID))
        for (first_name, middle_name, last_name) in cursor:
          self.editFirst.setText(first_name)
          self.editMiddle.setText(middle_name)
          self.editLast.setText(last_name)
        cursor.close()
        cnx.close()




class Register(QtWidgets.QMainWindow, RegisterPage.Ui_MainWindow):
    def __init__(self):
        super(Register, self).__init__()
        self.setupUi(self)
        self.btnBack.clicked.connect(self.pushButtonBack_clicked)
        self.btnRegister.clicked.connect(self.pushButtonRegister_clicked)

    def pushButtonBack_clicked(self):
        self.dialogBack = Welcome()
        self.dialogBack.show()
        self.close()

    def pushButtonRegister_clicked(self):
        if HelperClass.IsFaculty_IDTaken(self.textEdit.toPlainText()):
            QMessageBox.question(self, 'Faculty ID Taken!', "Faculty ID is already taken!", QMessageBox.Ok)
        else:
            cnx = mysql.connector.connect(user='sa', password='kappa123',
                                  host='localhost',
                                  database='inventory_system')
            cursor = cnx.cursor()
            query = ("INSERT INTO faculty "
                     "(faculty_id, first_name, last_name, middle_name, birthdate, username, password, gender_id, position_id, inventory_id) "
                     "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
            employeeDetails = (self.textEdit.toPlainText(), self.textEdit_2.toPlainText(), self.textEdit_3.toPlainText(), self.textEdit_4.toPlainText(), date(1969, 6, 12), 'facultyDefault', 'password123', 0, 0, 0)
            cursor.execute(query, employeeDetails)
            QMessageBox.question(self, 'Success!', "Faculty Registered!", QMessageBox.Ok)
            cnx.commit()
            cursor.close()
            cnx.close()
            self.pushButtonBack_clicked()


class ReportList(QtWidgets.QMainWindow, ReportListPage.Ui_MainWindow):
    def __init__(self):
        super(ReportList, self).__init__()
        self.setupUi(self)
        self.btnBack.clicked.connect(self.pushButtonBack_clicked)
    def pushButtonBack_clicked(self):
        self.dialogBack = Design()
        self.dialogBack.show()
        self.close()

class Login(QtWidgets.QMainWindow, LoginPage.Ui_MainWindow):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.btnLogin.clicked.connect(self.pushButtonLogin_clicked)
        self.btnBack.clicked.connect(self.pushButtonBack_clicked)
        self.dialog = Design()
    def pushButtonLogin_clicked(self):
        loginSuccess = HelperClass.CheckLoginCredentials(self.textUsername.toPlainText(), self.textPassword.text())
        if loginSuccess:
            self.close()
            self.dialog.show()
        else:
            QMessageBox.question(self, 'Login Failed!', "Incorrect login credentials!", QMessageBox.Ok)
    def pushButtonBack_clicked(self):
        self.dialogBack = Welcome()
        self.dialogBack.show()
        self.close()

class AddItem(QtWidgets.QMainWindow, AddItemPage.Ui_MainWindow):
    def __init__(self):
        super(AddItem, self).__init__()
        self.setupUi(self)
        self.btnBack.clicked.connect(self.pushButtonBack_clicked)
    def pushButtonBack_clicked(self):
        self.dialogBack = Design()
        self.dialogBack.show()
        self.close()

class ViewAllItems(QtWidgets.QMainWindow, ViewAllItemsPage.Ui_MainWindow):
    def __init__(self):
        super(ViewAllItems, self).__init__()
        self.setupUi(self)
        self.btnSelect.clicked.connect(self.pushButtonSelect_clicked)
        self.dialog = ViewItemDetails()
        self.btnBack.clicked.connect(self.pushButtonBack_clicked)
    def pushButtonSelect_clicked(self):
        self.close()
        self.dialog.show()
    def pushButtonBack_clicked(self):
        self.dialogBack = Design()
        self.dialogBack.show()
        self.close()

class ViewItemDetails(QtWidgets.QMainWindow, ViewItemDetailsPage.Ui_MainWindow):
    def __init__(self):
        super(ViewItemDetails, self).__init__()
        self.setupUi(self)
        self.btnModify.clicked.connect(self.pushButtonModify_clicked)
        self.dialog = ModifyItemDetails()
        self.btnBack.clicked.connect(self.pushButtonBack_clicked)

    def pushButtonBack_clicked(self):
        self.dialogBack = ViewAllItems()
        self.dialogBack.show()
        self.close()

    def pushButtonModify_clicked(self):
        self.close()
        self.dialog.show()

class ModifyItemDetails(QtWidgets.QMainWindow, ModifyItemDetailsPage.Ui_MainWindow):
        def __init__(self):
            super(ModifyItemDetails, self).__init__()
            self.setupUi(self)
            self.btnDone.clicked.connect(self.pushButtonDone_clicked)
            self.btnLogout.clicked.connect(self.pushButtonLogout_clicked)

        def pushButtonDone_clicked(self):
            self.dialogBack = ViewItemDetails()
            self.dialogBack.show()
            self.close()

        def pushButtonLogout_clicked(self):
            self.dialogBack = Welcome()
            self.dialogBack.show()
            self.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = Welcome()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
