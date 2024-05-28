from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys


class Main_Page(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"Main_page\mainwindow.ui", self)
        self.setWindowTitle("Main Page")
        self.setWindowIcon(QIcon(r"Main_page\main_icon.png"))
        self.style()

    def style(self):
        self.setFixedSize(444, 508)
        self.time_label.setStyleSheet("background : none ;")
        self.welcome_text.setStyleSheet("""background : none ;""")
        self.setStyleSheet(
            """ background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #2980B9,
                stop: 1 #6DD5FA
            );"""
        )
        self.record_income_btn.setCursor(Qt.PointingHandCursor)
        self.record_income_btn.setStyleSheet(
            """
            QPushButton{
                border-radius:5px;
                border :1px solid #ffffff;
            }
            QPushButton:hover{
                color : yellow;
                background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #ee0979,
                stop: 1 #ff6a00);
            }"""
        )
        self.record_cost_btn.setCursor(Qt.PointingHandCursor)
        self.record_cost_btn.setStyleSheet(
            """
            QPushButton{
                border-radius:5px;
                border :1px solid #ffffff;
            }
            QPushButton:hover{
                color : yellow;
                background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #ee0979,
                stop: 1 #ff6a00);
            }"""
        )
        self.category_btn.setCursor(Qt.PointingHandCursor)
        self.category_btn.setStyleSheet(
            """
            QPushButton{
                border-radius:5px;
                border :1px solid #ffffff;
            }
            QPushButton:hover{
                color : yellow;
                background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #ee0979,
                stop: 1 #ff6a00);
            }"""
        )
        self.search_btn.setCursor(Qt.PointingHandCursor)
        self.search_btn.setStyleSheet(
            """
            QPushButton{
                border-radius:5px;
                border :1px solid #ffffff;
            }
            QPushButton:hover{
                color : yellow;
                background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #ee0979,
                stop: 1 #ff6a00);
            }"""
        )
        self.report_btn.setCursor(Qt.PointingHandCursor)
        self.report_btn.setStyleSheet(
            """
            QPushButton{
                border-radius:5px;
                border :1px solid #ffffff;
            }
            QPushButton:hover{
                color : yellow;
                background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #ee0979,
                stop: 1 #ff6a00);
            }"""
        )
        self.setting_btn.setCursor(Qt.PointingHandCursor)
        self.setting_btn.setStyleSheet(
            """
            QPushButton{
                border-radius:5px;
                border :1px solid #ffffff;
            }
            QPushButton:hover{
                color : yellow;
                background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #ee0979,
                stop: 1 #ff6a00);
            }"""
        )
        self.record_income_btn.setCursor(Qt.PointingHandCursor)
        self.record_income_btn.setStyleSheet(
            """
            QPushButton{
                border-radius:5px;
                border :1px solid #ffffff;
            }
            QPushButton:hover{
                color : yellow;
                background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #ee0979,
                stop: 1 #ff6a00);
            }"""
        )
        self.exit_mainpage_btn.setCursor(Qt.PointingHandCursor)
        self.exit_mainpage_btn.setStyleSheet(
            """
            QPushButton{
                border-radius:5px;
                border :1px solid #ffffff;
            }
            QPushButton:hover{
                color : yellow;
                background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #ee0979,
                stop: 1 #ff6a00);
            }"""
        )

    def set_user_info(self, emuser):
        self.userfullname.setText(f"User : {emuser}")
