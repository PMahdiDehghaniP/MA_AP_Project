from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
from PyQt5.QtWidgets import QWidget


class Cost_Form(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"Cost_Page\cost_page.ui", self)
        self.setFixedSize(370, 710)
        self.setWindowTitle("Cost Page")
        self.setWindowIcon(QIcon(r"Cost_Page\cost_icon.png"))
        self.lineedit_style = '''
            border : 1px solid grey;
            border-radius:6px;
            padding:0px 0px 0px 5px;
            color : #ffffff; '''
        self.btn_style = '''
            QPushButton{
                border-radius:6px;
                border : 1px solid grey;
                color:#ffffff;}
            QPushButton:hover {
                color : black;
            background: qlineargradient(
            spread:pad, x1:0, y1:0, x2:1, y2:0,
            stop:0 #833ab4,
            stop:0.5 #fd1d1d,
            stop:1 #fcb045
            );}'''
        self.style()

    def style(self):
        self.setStyleSheet(
            '''
            background: qlineargradient(
            spread:pad, x1:0, y1:0, x2:1, y2:0,
            stop:0 #141E30,
            stop:1 #243B55
        );''')
        self.cost_form_label.setStyleSheet(
            '''background: none;color:#ffffff;''')
        self.cost_amount.setStyleSheet(self.lineedit_style)
        self.cost_date.setStyleSheet(self.lineedit_style)
        self.cost_resource.setStyleSheet(self.lineedit_style)
        self.cost_type.setStyleSheet(self.lineedit_style)
        self.description_cost.setStyleSheet(self.lineedit_style)
        self.submit_cost_page_btn.setCursor(Qt.PointingHandCursor)
        self.submit_cost_page_btn.setStyleSheet(self.btn_style)
        self.exit_btn_cost.setCursor(Qt.PointingHandCursor)
        self.exit_btn_cost.setStyleSheet(self.btn_style)
