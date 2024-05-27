from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

from PyQt5.QtWidgets import QWidget


class Income(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"Income_page\mainwindow.ui", self)
        self.setWindowTitle("Income Page")
        self.setWindowIcon(QIcon(r"Income_page\income-icon.jpg"))
        self.style()

    def style(self):
        self.setFixedSize(404,654)
        self.Income_title_label.setStyleSheet("background: none;")
        self.income_amount_linedit.setStyleSheet(
            """
                padding:0px 0px 0px 5px;
                background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #a8c0ff,
                stop: 1 #3f2b96);
                border-radius:6px;
            """
        )
        self.income_date_linedit.setStyleSheet(
            """
                padding:0px 0px 0px 5px;
                background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #a8c0ff,
                stop: 1 #3f2b96);
                border-radius:6px;
            """
        )
        self.income_resource_linedit.setStyleSheet(
            """
                padding:0px 0px 0px 5px;
                background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #a8c0ff,
                stop: 1 #3f2b96);
                border-radius:6px;
            """
        )
        self.income_type_linedit.setStyleSheet(
            """
                padding:0px 0px 0px 5px;
                background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #a8c0ff,
                stop: 1 #3f2b96);
                border-radius:6px;
            """
        )
        self.income_discription_linedit.setStyleSheet(
            """
                padding:0px 0px 0px 5px;
                background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #a8c0ff,
                stop: 1 #3f2b96);
                border-radius:6px;
            """
        )
        self.setStyleSheet(
            """
                background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #134E5E,
                stop: 1 #71B280);
            """
        )
        self.income_submit_btn.setCursor(Qt.PointingHandCursor)
        self.income_submit_btn.setStyleSheet(
            """
            QPushButton{
                border-radius:6px;
                background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #8360c3,
                stop: 1 #2ebf91);
                }
            QPushButton:hover{
                
                color : yellow;
                background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #3E5151,
                stop: 1 #DECBA4);
            }
        """
        )
