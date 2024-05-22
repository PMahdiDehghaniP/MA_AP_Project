from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
from PyQt5.QtWidgets import QWidget


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Login_Page\\mainwindow.ui", self)
        self.setWindowTitle("Welcome Page")
        self.setFixedSize(422, 440)
        self.setWindowIcon(QIcon("Login_Page\\login_icon.png"))
        self.login_label.setStyleSheet("background:none;")
        self.forgot_login.setStyleSheet("background:none;")
        self.question.setStyleSheet("background:none;font-size:18px;")
        self.dont_acc_login.setStyleSheet("background:none;")
        self.setStyleSheet('''
            background: qlineargradient(
            spread:pad, x1:0, y1:0, x2:1, y2:0, 
            stop:0 #0093E9, 
            stop:1 #80D0C7
        );''')
        self.email_login.setStyleSheet('''
            background:#DFDFDF;
            border:none;
            border-radius:5px;
            padding:0px 0px 0px 5px;
            font-size:14px;''')
        self.password_login.setStyleSheet('''
            background:#DFDFDF;
            border:none;
            border-radius:5px;
            padding:0px 0px 0px 5px;
            font-size:14px;''')
        self.show_pass_login.setStyleSheet('''
            background:none;''')
        self.sign_in_login_btn.setStyleSheet('''
            background: qlineargradient(
            spread:pad, x1:0, y1:0, x2:1, y2:0, 
            stop:0 #8EC5FC, 
            stop:1 #E0C3FC
            );
            border:none;
            border-radius:5px;
            font-size:14px;''')
        self.pass_forgot_login.setCursor(Qt.PointingHandCursor)
        self.pass_forgot_login.setStyleSheet('''
            QPushButton{
            background:none;
            border:none;
            border-radius:5px;
            font-size:18px;
            }
            QPushButton:hover{
                color:#800004;
                border:1px solid #800004;
            }''')
        self.signup_btn_login.setCursor(Qt.PointingHandCursor)
        self.signup_btn_login.setStyleSheet('''
            QPushButton{
            background:none;
            border:none;
            border-radius:5px;
            font-size:18px;
            }
            QPushButton:hover{
                color:#800004;
                border:1px solid #800004;
            }''')


app = QApplication([])
w = Login()
w.show()
app.exec_()
