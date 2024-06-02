from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import Qt


class Search_Page(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(622, 496)
        uic.loadUi("Search\mainwindow.ui", self)
        self.lineedit_style = '''
        border-bottom:1px solid black;
        border-radius:3px;
        padding-left:3px;
        background:none;
        '''
        self.style()
        self.hide_all_lineedits()

    def style(self):
        self.search_label.setStyleSheet("background:none")
        self.filter_label.setStyleSheet("background:none")
        self.daycheckbox.setStyleSheet("background:none")
        self.monthcheckbox.setStyleSheet("background:none")
        self.yearcheckbox.setStyleSheet("background:none")
        self.price_checkbox.setStyleSheet("background:none")
        self.incomecheckbox.setStyleSheet("background:none")
        self.costcheckbox.setStyleSheet("background:none")
        self.day_lineedit.setStyleSheet(self.lineedit_style)
        self.month_lineedit.setStyleSheet(self.lineedit_style)
        self.year_lineedit.setStyleSheet(self.lineedit_style)
        self.price_low.setStyleSheet(self.lineedit_style)
        self.price_high.setStyleSheet(self.lineedit_style)
        self.income_lineedit.setStyleSheet(self.lineedit_style)
        self.cost_lineedit.setStyleSheet(self.lineedit_style)
        self.search_lineedit.setStyleSheet(self.lineedit_style)
        self.search_btn.setCursor(Qt.PointingHandCursor)
        self.setStyleSheet('''
            background: qlineargradient(
            spread:pad, x1:0, y1:0, x2:1, y2:0, 
            stop:0 #654ea3, 
            stop:1 #eaafc8
        );''')
        self.search_btn.setStyleSheet('''
        QPushButton{
        background: qlineargradient(
        spread:pad, x1:0, y1:0, x2:1, y2:0, 
        stop:0 #f12711, 
        stop:1 #f5af19
        );
        border:none;
        border-radius:5px;
        }
        QPushButton:hover{
        background: qlineargradient(
        spread:pad, x1:0, y1:0, x2:1, y2:0, 
        stop:0 #200122, 
        stop:1 #6f0000
        );
        }
                                      ''')

    def hide_all_lineedits(self):
        self.day_lineedit.hide()
        self.month_lineedit.hide()
        self.year_lineedit.hide()
        self.price_low.hide()
        self.price_high.hide()
        self.income_lineedit.hide()
        self.cost_lineedit.hide()

    def hide_line_edit(self, lineedit_name):
        lineedit_name.hide()

    def show_line_edit(self, lineedit_name):
        lineedit_name.show()
