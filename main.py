import sys, os
from numpy import random
from PyQt5 import QtCore
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow, QVBoxLayout, QLineEdit, QLabel, QDialog, QTableView
import sqlite3



Login = uic.loadUiType(os.path.join(os.getcwd(), 'login.ui'))[0]
Register = uic.loadUiType(os.path.join(os.getcwd(), 'register.ui'))[0]
Unvalid = uic.loadUiType(os.path.join(os.getcwd(), 'unvalid.ui'))[0]
Location = uic.loadUiType(os.path.join(os.getcwd(), 'location.ui'))[0]


class LocationWindow(Location, QMainWindow):
    def __init__(self):
        Location.__init__(self)
        QMainWindow.__init__(self)
        self.setupUi(self)


class UnvalidWindow(Unvalid, QMainWindow):
    def __init__(self):
        Unvalid.__init__(self)
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.pushButton_unvalid.clicked.connect(self.exit_window)

    def exit_window(self):
        # sys.exit(self)
        self.close()

class RegisterWindow(Register, QMainWindow):
    def __init__(self):
        Register.__init__(self)
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.signUpButton.clicked.connect(self.sign_up)

    def sign_up(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        email = self.lineEdit_3.text()

        connection = sqlite3.connect("login.db")

        result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ?", (username, ))

        flag = False
        for user in result:
            if user[0] == username:
                flag = True

        if not flag:
            connection.execute("INSERT INTO USERS VALUES(?,?,?)", (username, email, password))
            connection.commit()
        else:
            self.w_unvalid = UnvalidWindow()
            self.w_unvalid.show()
        connection.close()
        self.close()

class LoginWindow(Login, QMainWindow):
    def __init__(self):
        Login.__init__(self)
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.loginPushButton.clicked.connect(self.login_check)
        self.registerPushButton.clicked.connect(self.register_layout)

    def register_layout(self):
        print("AAA")
        self.w_register = RegisterWindow()
        self.w_register.show()

    def login_check(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        connection = sqlite3.connect("login.db")
        result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?", (username, password))
        if len(result.fetchall()) > 0:
            print("USER IS VALID")
            self.w_location = LocationWindow()
            self.w_location.show()
        else:
            print("USER NOT VALID")
            self.w_unvalid = UnvalidWindow()
            self.w_unvalid.show()


app = QApplication(sys.argv)
w_login = LoginWindow()
w_login.show()
sys.exit(app.exec())

