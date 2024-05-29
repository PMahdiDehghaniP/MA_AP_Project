from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
from PyQt5.QtWidgets import QWidget


class category_page(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"Category\mainwindow.ui", self)
        self.setFixedSize(421, 213)
        self.setWindowTitle("Categories")

        self.setWindowIcon(QIcon(r"Category\icon_category.jpg"))
        self.style()

    def style(self):
        self.setStyleSheet(
            """
            background: qlineargradient(
            spread:pad, x1:0, y1:0, x2:1, y2:0,
            stop:0 #7b4397,
            stop:1 #dc2430
            );"""
        )
        self.category_lablel.setStyleSheet("background:none;")
        self.category_lineedit.setStyleSheet(
            """
        border : 1px solid black;
            border-radius:6px;
            padding:0px 0px 0px 5px;
            color : #ffffff; """
        )
        self.category_submit.setCursor(Qt.PointingHandCursor)
        self.category_submit.setStyleSheet(
            """
            QPushButton{
            background: qlineargradient(
            spread:pad, x1:0, y1:0, x2:1, y2:0,
            stop:0 #ff00cc,
            stop:1 #333399
            );
            border-radius:6px;
            border : 1px solid grey;
            color:#ffffff;
            }
            QPushButton:hover {
            color : black;
            background: qlineargradient(
            spread:pad, x1:0, y1:0, x2:1, y2:0,
            stop:0 #CC95C0,
            stop:0.5 #DBD4B4,
            stop:1 #7AA1D2
            );
            }"""
        )


app = QApplication([])
w = category_page()
w.show()
app.exec_()
