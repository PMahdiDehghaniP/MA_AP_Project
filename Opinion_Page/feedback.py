from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from Login_Page.login_form import Login
from MessageBox.messagebox import Message_Box
from Sound.back_sound import Sound



class Feedback(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"Opinion_Page\mainwindow.ui", self)
        self.setFixedSize(551, 469)
        self.setWindowTitle("YourFeedback")
        self.setWindowIcon(QIcon(r"Opinion_Page\icon.png"))
        self.btn_style = """
        QPushButton{
        background: qlineargradient(
        spread:pad, x1:0, y1:0, x2:1, y2:0,
        stop:0 #f12711,
        stop:1 #f5af19
        );
        border:none;
        border-radius:5px;
        color:#ffffff
        }
        QPushButton:hover{
        background: qlineargradient(
        spread:pad, x1:0, y1:0, x2:1, y2:0,
        stop:0 #200122,
        stop:1 #6f0000
        );
        }
        """
        self.setStyleSheet(
            """
            background: qlineargradient(
            spread:pad, x1:0, y1:0, x2:1, y2:0, 
            stop:0 #654ea3, 
            stop:1 #f2fcfe
        );"""
        )
        self.style()

    def style(self):
        self.submitbtn.setStyleSheet(self.btn_style)
        self.submitbtn.setCursor(Qt.PointingHandCursor)
        self.returnbtn.setStyleSheet(self.btn_style)
        self.returnbtn.setCursor(Qt.PointingHandCursor)
        self.title.setStyleSheet("background:none;")
        self.feedbackbox.setStyleSheet("background:none;")

