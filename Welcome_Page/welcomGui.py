from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

from PyQt5.QtWidgets import QWidget


class Welcome(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"Welcome_Page\mainwindow.ui", self)
        self.setWindowTitle("Welcome Page")
        self.setFixedSize(462, 265)
        self.setWindowIcon(QIcon(r"Welcome_Page\welcome_icon.jpg"))
        self.setStyleSheet(
            """background:url(Welcome_Page/welcome.webp);
        """
        )
        self.welcome_page_label.setStyleSheet(
            """color:white;
                                            background:none;
                                            text-align:center;
                                            font-size:20px"""
        )
        self.login_btn.setCursor(Qt.PointingHandCursor)
        self.login_btn.setStyleSheet(
            """
    QPushButton {
        border-radius: 6px;
        color: white;
        font-size:14px;
        background: qlineargradient(
            spread:pad, x1:0, y1:0, x2:1, y2:0, 
            stop:0 #480048, 
            stop:1 #c04848
        );
    }
    QPushButton:hover {
        font-size:18px;
        font-weight:900;
        color: yellow;
        border-radius: 6px;
        font-size: 14px;
        background: qlineargradient(
            spread:pad, x1:0, y1:0, x2:1, y2:0, 
            stop:0.36 rgba(22, 90, 157, 255), 
            stop:0.62 rgba(80, 208, 232, 255)
        );
    }
        """
        )
        self.signup_btn.setCursor(Qt.PointingHandCursor)
        self.signup_btn.setStyleSheet(
            """
    QPushButton {
        border-radius: 6px;
        font-size:14px;
        color: white;
        background: qlineargradient(
            spread:pad, x1:0, y1:0, x2:1, y2:0, 
            stop:0 #480048, 
            stop:1 #c04848
        );
        }
        QPushButton:hover {
        border-radius: 6px;
        font-size:18px;
        font-weight:900;
        color: yellow;
        font-size: 14px;
        background: qlineargradient(
            spread:pad, x1:0, y1:0, x2:1, y2:0, 
            stop:0.36 rgba(22, 90, 157, 255), 
            stop:0.62 rgba(80, 208, 232, 255)
        );
        
    }
        """
        )

app=QApplication([])
w=Welcome()
w.show()
app.exec_()