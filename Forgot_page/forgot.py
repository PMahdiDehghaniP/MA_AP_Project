from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

from PyQt5.QtWidgets import QWidget


class forgot(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"Forgot_page\mainwindow.ui", self)
        self.setWindowTitle("Forgot Password Page")
        self.setFixedSize(499, 448)
        self.style()

    def style(self):
        self.setWindowIcon(QIcon(r"Forgot_page\forgot_icon.jpg"))
        self.setStyleSheet("background: #2173FF;")
        self.groupBox_forgot.setStyleSheet(
            """
                    background: white;
                    border-radius: 7px;
                                        """
        )
        self.em_us_forgot_linedit.setStyleSheet(
            "border: 0.5px solid black;padding-left: 5px;"
        )
        self.forgot_title.setStyleSheet("color: #000099;")
        self.kapcha.setStyleSheet("background: #E0E0E0;padding-left: 5px;")
        self.input_kapch_lineedit.setStyleSheet(
            "background: #E0E0E0;padding-left: 5px;"
        )
        self.forgot_password_btn.setStyleSheet(
            """
            QPushButton { 
            border-radius:5px;
            font-size:16px;
            border:0.5px solid #38ef7d;
            background: #3399ff;
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

