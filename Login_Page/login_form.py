import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from MessageBox.messagebox import *
from JJson.jjson import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

from PyQt5.QtWidgets import QWidget



check_tool = CreateJson("user.json")
show_message = Message_Box()


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"Login_Page\mainwindow.ui", self)
        self.setWindowTitle("Welcome Page")
        self.setFixedSize(422, 440)
        self.setWindowIcon(QIcon(r"Login_Page\login_icon.png"))
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
        self.sign_in_login_btn.setCursor(Qt.PointingHandCursor)
        self.sign_in_login_btn.setStyleSheet('''
            QPushButton{                              
            background: qlineargradient(
            spread:pad, x1:0, y1:0, x2:1, y2:0, 
            stop:0 #8EC5FC, 
            stop:1 #E0C3FC
            );
            border:none;
            border-radius:5px;
            font-size:14px;
            }
            QPushButton:hover{
            background: qlineargradient(
            spread:pad, x1:0, y1:0, x2:1, y2:0, 
            stop:0 #c31432, 
            stop:1 #240b36
            );
            color:yellow;
            }
            ''')
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
            }'''
                                            )

    def login_user(self):
        if check_tool.does_user_exist(self.email_login.text(), self.password_login.text()) == "invalid password":
            show_message.show_warning("Incorrect Password!\nTry Again!")
            self.password_login.setText("")
        elif check_tool.does_user_exist(self.email_login.text(), self.password_login.text()) == "not found":
            show_message.show_warning('''There is no such user registered in the system.\n
Please check the details again.\n
If you don't have an account, please sign up.''')
            self.email_login.setText("")
            self.password_login.setText("")
        elif check_tool.does_user_exist(self.email_login.text(), self.password_login.text()) == "Valid":
            show_message.show_message(
                "You have successfully logged in. Welcome!")
