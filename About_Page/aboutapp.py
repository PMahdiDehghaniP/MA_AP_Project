from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic


class AboutApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"About_Page\mainwindow.ui", self)
        self.setFixedSize(551, 553)
        self.setWindowTitle("About Our App")
        self.setWindowIcon(QIcon(r"About_Page\icon.jpg"))
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
        self.return_about_btn.setStyleSheet(self.btn_style)
        self.return_about_btn.setCursor(Qt.PointingHandCursor)
        self.title.setStyleSheet("background:none;")
        self.developers_label.setStyleSheet("background:none;")
        self.features_label.setStyleSheet("background:none;")
        self.version.setStyleSheet("background:none;")
        self.discription.setStyleSheet("background:none;")
