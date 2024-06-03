from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from validates.validate import *
from MessageBox.messagebox import *
from datacenter.projectdb import PDataBase
import re
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


###################################################
Message = Message_Box()
Valid = Validate()
db_controler = PDataBase()


class Signup(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"SignupPage\mainwindow.ui", self)
        self.setWindowTitle("Sign UP")
        self.lineedit_style = """border:1px solid #898989;
        border-radius:6px;
            background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #eef2f3,
                stop: 1 #8e9eab
            );
        font-size:16px;
        padding:0px 0px 0px 5px;"""
        self.setFixedSize(479, 640)
        self.setWindowIcon(QIcon(r"SignupPage\icon_signup.png"))
        self.setStyleSheet(
            """
background : url('SignupPage/bg_signup.jpg');
background-repeat:no-repeat;                  """
        )
        self.line.setStyleSheet("background:none;")
        self.line_2.setStyleSheet("background:none;")
        self.register_label.setStyleSheet("background:none;")
        self.fname_signup.setStyleSheet(self.lineedit_style)
        self.lname_signup.setStyleSheet(self.lineedit_style)
        self.phone_signup.setStyleSheet(self.lineedit_style)
        self.username.setStyleSheet(self.lineedit_style)
        self.Password_signup.setStyleSheet(self.lineedit_style)
        self.repeatpasswprd_signup.setStyleSheet(self.lineedit_style)
        self.city_signup.setStyleSheet(self.lineedit_style)
        self.email_signup.setStyleSheet(self.lineedit_style)
        self.date_signup.setStyleSheet(self.lineedit_style)
        self.Submit_signup.setCursor(Qt.PointingHandCursor)
        self.Submit_signup.setStyleSheet(
            """
            QPushButton { 
            border-radius:5px;
            font-size:16px;
            border:0.5px solid #38ef7d;
            background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #38ef7d,
                stop: 1 #11998e
            );
            }
            QPushButton:hover {
            background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #8E0E00,
                stop: 1 #1F1C18);
                border:none;
                color:Yellow;
                }
                """
        )
        self.cityOpthoin = [
            "yazd",
            "tehran",
            "shiraz",
            """mash'had""",
            "abadan",
            "kermanshah",
            "bushehr",
            "ahvaz",
            "kordestan",
            "isfahan",
        ]
        completer = QCompleter(self.cityOpthoin, self.city_signup)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.city_signup.setCompleter(completer)

    def submit_signup_clicked(self):
        user_uniqe = db_controler.isunique_username(self.username.text())
        phone_uniqe = db_controler.isunique_phonenumber(
            self.phone_signup.text())
        email_uniqe = db_controler.isunique_email(
            self.email_signup.text())
        is_user_valid = True
        if Valid.validate_name(self.fname_signup.text()) == False:
            Message.show_warning("You Entered Inavlid First Name!")
            self.fname_signup.setText("")
            is_user_valid = False
            return is_user_valid
        if Valid.validate_name(self.lname_signup.text()) == False:
            Message.show_warning("You Entered Invalid Last Name!")
            self.lname_signup.setText("")
            is_user_valid = False
            return is_user_valid
        if Valid.validate_phone_number(self.phone_signup.text()) == False:
            Message.show_warning("You Entered Invalid Phone Number!")
            self.phone_signup.setText("")
            is_user_valid = False
            return is_user_valid
        if Valid.validate_username(self.username.text()) == False:
            Message.show_warning(
                "You Entered Invalid Username\nOr Already Taken!")
            self.username.setText("")
            is_user_valid = False
            return is_user_valid
        if Valid.validate_password(self.Password_signup.text()) == False:
            Message.show_warning("You Entered Invalid Value\nFor Password!")
            self.Password_signup.setText("")
            is_user_valid = False
            return is_user_valid
        if self.repeatpasswprd_signup.text() != self.Password_signup.text():
            Message.show_warning(
                "Repeat password does not match the password!")
            self.repeatpasswprd_signup.setText("")
            is_user_valid = False
            return is_user_valid
        if Valid.validate_city(self.city_signup.text()) == False:
            Message.show_warning("You Entered Invalid City!")
            self.city_signup.setText("")
            is_user_valid = False
            return is_user_valid
        if Valid.validate_email(self.email_signup.text()) == False:
            Message.show_warning("You Entered Invalid Email!")
            self.email_signup.setText("")
            is_user_valid = False
            return is_user_valid
        if Valid.validite_birthday(self.date_signup.text()) == False:
            Message.show_warning("You Entered Invalid Birthday Date!")
            self.date_signup.setText("")
            is_user_valid = False
            return is_user_valid
        if phone_uniqe == False:
            Message.show_warning(
                "This mobile number has already been used.")
            self.phone_signup.setText("")
            is_user_valid = False
            return is_user_valid
        if email_uniqe == False:
            Message.show_warning("This Email has already been used.")
            self.email_signup.setText("")
            is_user_valid = False
            return is_user_valid
        if user_uniqe == False:
            Message.show_warning("This Username has already been used.")
            self.username.setText("")
            is_user_valid = False
            return is_user_valid
        return is_user_valid

    def reset_signup(self):
        self.fname_signup.setText("")
        self.lname_signup.setText("")
        self.phone_signup.setText("")
        self.username.setText("")
        self.Password_signup.setText("")
        self.repeatpasswprd_signup.setText("")
        self.city_signup.setText("")
        self.email_signup.setText("")
        self.date_signup.setText("")
