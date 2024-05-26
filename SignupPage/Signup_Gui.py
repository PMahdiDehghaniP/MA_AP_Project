from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
import sys


class Signup(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"SignupPage\mainwindow.ui", self)
        self.setWindowTitle("Sign UP")
        self.setFixedSize(479,640)
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