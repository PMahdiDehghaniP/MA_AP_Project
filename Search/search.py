from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import Qt
from validates.validate import *
from MessageBox.messagebox import *


Valid = Validate()
Message = Message_Box()


class Search_Page(QMainWindow):
    def __init__(self):
        super().__init__()
        self.day = ""
        self.month = ""
        self.year = ""
        self.upper_price = ""
        self.lower_price = ""
        self.setFixedSize(622, 496)
        self.setWindowIcon(QIcon(r"Search\Search_icon.png"))
        uic.loadUi(r"Search\mainwindow.ui", self)
        self.setWindowTitle("Search Box")
        self.lineedit_style = """
        border-bottom:1px solid black;
        border-radius:3px;
        padding-left:3px;
        background:none;
        """
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
        self.search_lineedit.setStyleSheet(self.lineedit_style)
        self.search_btn.setCursor(Qt.PointingHandCursor)
        self.return_btn.setCursor(Qt.PointingHandCursor)
        self.setStyleSheet(
            """
            background: qlineargradient(
            spread:pad, x1:0, y1:0, x2:1, y2:0, 
            stop:0 #654ea3, 
            stop:1 #eaafc8
        );"""
        )
        self.search_btn.setStyleSheet(self.btn_style)
        self.return_btn.setStyleSheet(self.btn_style)

    def hide_all_lineedits(self):
        self.day_lineedit.hide()
        self.month_lineedit.hide()
        self.year_lineedit.hide()
        self.price_low.hide()
        self.price_high.hide()

    def hide_line_edit(self, lineedit_name):
        lineedit_name.hide()

    def show_line_edit(self, lineedit_name):
        lineedit_name.show()

    def reset_form(self):
        self.day_lineedit.setText("")
        self.month_lineedit.setText("")
        self.year_lineedit.setText("")
        self.price_low.setText("")
        self.price_high.setText("")
        self.search_lineedit.setText("")
        self.hide_all_lineedits()
        self.daycheckbox.setChecked(False)
        self.monthcheckbox.setChecked(False)
        self.yearcheckbox.setChecked(False)
        self.price_checkbox.setChecked(False)
        self.incomecheckbox.setChecked(False)
        self.costcheckbox.setChecked(False)

    def serach_btn_clicked(self):
        checkstr = True
        if len(self.search_lineedit.text()) == 0:
            Message.show_warning("Please Enter somthing in search box!")
            self.search_lineedit.setText("")
            checkstr = False
            return checkstr
        if (
            self.daycheckbox.isChecked()
            and Valid.validate_day(self.day_lineedit.text()) == False
        ):
            Message.show_warning("You Entered invalid day!")
            self.day_lineedit.setText("")
            checkstr = False
            return checkstr
        if (
            self.monthcheckbox.isChecked()
            and Valid.validate_month(self.month_lineedit.text()) == False
        ):
            Message.show_warning("You Entered invalid month!")
            self.month_lineedit.setText("")
            checkstr = False
            return checkstr
        if (
            self.yearcheckbox.isChecked()
            and Valid.validate_yaer(self.year_lineedit.text()) == False
        ):
            Message.show_warning("You Entered invalid year!")
            self.year_lineedit.setText("")
            checkstr = False
            return checkstr
        if self.price_checkbox.isChecked():
            if Valid.valid_amount(self.price_low.text()) == False:
                Message.show_warning("You Entered invalid amount for lower price!")
                self.price_low.setText("")
                checkstr = False
                return checkstr
            if Valid.valid_amount(self.price_high.text()) == False:
                Message.show_warning("You Entered invalid amount for higher price!")
                self.price_high.setText("")
                checkstr = False
                return checkstr
            if (
                Validate.validate_limit_price(
                    self.price_high.text(), self.price_low.text()
                )
                == False
            ):
                Message.show_warning("Upper Price Must be greater than Lower Price")
                self.price_high.setText("")
                self.price_low.setText("")
                checkstr = False
                return checkstr
        return checkstr
