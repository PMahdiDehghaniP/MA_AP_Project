from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
from JJson.jjson import CreateJson
from PyQt5.QtWidgets import QWidget

category_adder = CreateJson("category.json")


class Income(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"Income_page\mainwindow.ui", self)
        self.setWindowTitle("Income Page")
        self.setWindowIcon(QIcon(r"Income_page\income-icon.jpg"))
        self.lineedit_style = """
                padding:0px 0px 0px 5px;
                background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #a8c0ff,
                stop: 1 #3f2b96);
                border-radius:6px;"""
        self.btn_style = """
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
            }"""
        self.style()

    def style(self):
        self.setFixedSize(404, 719)
        self.Income_title_label.setStyleSheet("background: none;")
        self.income_amount_linedit.setStyleSheet(self.lineedit_style)
        self.income_date_linedit.setStyleSheet(self.lineedit_style)
        self.income_resource.setStyleSheet(self.lineedit_style)
        self.income_type_combo.setStyleSheet(self.lineedit_style)
        self.income_discription_linedit.setStyleSheet(self.lineedit_style)
        self.setStyleSheet(
            """
                background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #134E5E,
                stop: 1 #71B280);
            """
        )
        self.income_submit_btn.setCursor(Qt.PointingHandCursor)
        self.exit_btn_income.setCursor(Qt.PointingHandCursor)
        self.income_submit_btn.setStyleSheet(self.btn_style)
        self.exit_btn_income.setStyleSheet(self.btn_style)

    def income_combo_items(self, username):
        if self.income_resource.count() == 0:
            category_list = category_adder.return_list_of_category(username)
            for item in category_list:
                self.income_resource.addItem(item)

    def income_type_items(self):
        if self.income_type_combo.count() == 0:
            income_types = ["Cryptocurrency", "Check", "Cash"]
            for item in income_types:
                self.income_type_combo.addItem(item)
