from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from JJson.jjson import CreateJson
from validates.validate import Validate
import sys
from PyQt5.QtWidgets import QWidget

category_json = CreateJson("category.json")
category_validatation = Validate()


class Category_Page(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"Category\mainwindow.ui", self)
        self.setFixedSize(421, 273)
        self.setWindowTitle("Categories")
        self.setWindowIcon(QIcon(r"Category\icon_category.jpg"))
        self.btn_style = '''
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
            }
        '''
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
        self.category_exit.setCursor(Qt.PointingHandCursor)
        self.category_submit.setStyleSheet(self.btn_style)
        self.category_exit.setStyleSheet(self.btn_style)

    def add_category(self, category, user):
        if category_validatation.validate_categoty(category) == True and category_json.is_uniqe_category(category) == True:
            recent_category_list = category_json.return_list_of_category(user)
            recent_category_list.append(category)
            data = {user: recent_category_list}
            category_json.add_dict_to_json(data)
            return True
        return False

    def reset_category(self):
        self.category_lineedit.setText("")
        
    def check_exist_category(self,user):
        data = category_json.load_json_file()
        if user in data:
            return True
        else:
            return False
