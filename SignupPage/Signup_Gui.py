from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import re
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from MessageBox.messagebox import *
###################################################
Message = Message_Box()


class Signup(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"SignupPage\mainwindow.ui", self)
        self.setWindowTitle("Sign UP")
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
        self.fname_signup.setStyleSheet(
            """border:1px solid #898989;
        border-radius:6px;
            background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #eef2f3,
                stop: 1 #8e9eab
            );
        font-size:16px;
        padding:0px 0px 0px 5px;
                                        """
        )
        self.lname_signup.setStyleSheet(
            """border:1px solid #898989;
        border-radius:6px;
            background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #eef2f3,
                stop: 1 #8e9eab
            );
        font-size:16px;
        padding:0px 0px 0px 5px;
                                        """
        )
        self.phone_signup.setStyleSheet(
            """border:1px solid #898989;
        border-radius:6px;
            background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #eef2f3,
                stop: 1 #8e9eab
            );
        font-size:16px;
        padding:0px 0px 0px 5px;
                                        """
        )
        self.username.setStyleSheet(
            """border:1px solid #898989;
        border-radius:6px;
            background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #eef2f3,
                stop: 1 #8e9eab
            );
        font-size:16px;
        padding:0px 0px 0px 5px;
                                        """
        )
        self.Password_signup.setStyleSheet(
            """border:1px solid #898989;
        border-radius:6px;
            background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #eef2f3,
                stop: 1 #8e9eab
            );
        font-size:16px;
        padding:0px 0px 0px 5px;
                                        """
        )
        self.repeatpasswprd_signup.setStyleSheet(
            """border:1px solid #898989;
        border-radius:6px;
            background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #eef2f3,
                stop: 1 #8e9eab
            );
        font-size:16px;
        padding:0px 0px 0px 5px;
                                        """
        )
        self.city_signup.setStyleSheet(
            """border:1px solid #898989;
        border-radius:6px;
            background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #eef2f3,
                stop: 1 #8e9eab
            );
        font-size:16px;
        padding:0px 0px 0px 5px;
                                        """
        )
        self.email_signup.setStyleSheet(
            """border:1px solid #898989;
        border-radius:6px;
            background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #eef2f3,
                stop: 1 #8e9eab
            );
        font-size:16px;
        padding:0px 0px 0px 5px;
                                        """
        )
        self.date_signup.setStyleSheet(
            """border:1px solid #898989;
        border-radius:6px;
            background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #eef2f3,
                stop: 1 #8e9eab
            );
        font-size:16px;
        padding:0px 0px 0px 5px;
                                        """
        )
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

    def validate_password(self, string):
        checkStr = ""
        lowercase_reg = re.compile(r"[a-z]")
        uppercase_reg = re.compile(r"[A-Z]")
        digit_reg = re.compile(r"[0-9]")
        symbol_reg = re.compile(r"[^(\w\d\s)]")
        if string == "":
            checkStr = False
        if not lowercase_reg.search(string):
            checkStr = False
        elif not uppercase_reg.search(string):
            checkStr = False
        elif not digit_reg.search(string):
            checkStr = False
        elif not symbol_reg.search(string):
            checkStr = False
        elif len(string) < 6:
            checkStr = False
        else:
            checkStr = True
        return checkStr

    def validate_name(self, name):
        checkuser = True
        if name.isalpha() and 3 < len(name) <= 15:
            checkuser = True
        elif len(name) == 0:
            checkuser = False
        else:
            checkuser = False
        return checkuser

    def validate_email(self, email):
        pattern = r"^[a-z]+\w*@gmail\.com"
        pattern2 = r"^[a-z]+\w*@yahoo\.com"
        checkEmail = (
            True if re.search(pattern, email) or re.search(pattern2, email) else False
        )
        if email == "":
            checkEmail = False
        return checkEmail

    def validite_birthday(self, date_string):
        pattern = r"^(19[2-9]\d|200[0-5])/(0[1-9]|1[0-2])/(0[1-9]|[12]\d|3[01])$"
        if re.match(pattern, date_string):
            return True
        else:
            return False

    def validate_phone_number(self, mobile_number):
        regex = r"^09\d{9}$"
        if re.match(regex, mobile_number):
            return True
        else:
            return False

    def validate_city(self, city):
        checkCity = False
        cityOpthoin = [
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
        for i in range(len(cityOpthoin)):
            if city == cityOpthoin[i]:
                checkCity = True
        return checkCity

    def validate_username(self, username):
        pattern = r"^(?=[a-zA-Z])[a-zA-Z0-9_]{5,}(?=.*\d)[a-zA-Z0-9_]*$"
        if re.match(pattern, username):
            return True
        else:
            return False

    def submit_signup_clicked(self):
        is_user_valid = True
        if self.validate_name(self.fname_signup.text()) == False:
            Message.show_warning("You Entered Inavlid First Name!")
            self.fname_signup.setText("")
            is_user_valid = False
        if self.validate_name(self.lname_signup.text()) == False:
            Message.show_warning("You Entered Invalid Last Name!")
            self.lname_signup.setText("")
            is_user_valid = False
        if self.validate_username(self.username.text()) == False:
            Message.show_warning("You Entered Invalid Username\nOr Already Taken!")
            self.username.setText("")
            is_user_valid = False
        if self.validate_password(self.Password_signup.text()) == False:
            Message.show_warning("You Entered Invalid Value\nFor Password!")
            self.Password_signup.setText("")
            is_user_valid = False
        if self.validate_email(self.email_signup.text()) == False:
            Message.show_warning("You Entered Invalid Email!")
            self.email_signup.setText("")
            is_user_valid = False
        if self.validite_birthday(self.date_signup.text()) == False:
            Message.show_warning("You Entered Invalid Birthday Date!")
            self.date_signup.setText("")
            is_user_valid = False
        if self.validate_phone_number(self.phone_signup.text()) == False:
            Message.show_warning("You Entered Invalid Phone Number!")
            self.phone_signup.setText("")
            is_user_valid = False
        if self.validate_city(self.city_signup.text()) == False:
            Message.show_warning("You Entered Invalid City!")
            self.city_signup.setText("")
            is_user_valid = False
        if self.repeatpasswprd_signup.text() != self.Password_signup.text():
            Message.show_warning("Repeat password does not match the password!")
            self.repeatpasswprd_signup.setText("")
            is_user_valid = False
        return is_user_valid
