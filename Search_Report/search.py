from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import Qt
from validates.validate import *
from MessageBox.messagebox import *
from datacenter.projectdb import PDataBase


Valid = Validate()
Message = Message_Box()
dbcontroler = PDataBase()


class Search_Page(QMainWindow):
    def __init__(self):
        super().__init__()
        self.username = ""
        self.end_year = ""
        self.end_month = ""
        self.end_day = ""
        self.start_year = ""
        self.start_month = ""
        self.start_day = ""
        self.setFixedSize(813, 684)
        uic.loadUi(r"Search_Report\mainwindow_search.ui", self)
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
        self.Geometry_without_calender()
        self.setWindowTitle("Search Form")
        self.setWindowIcon(QIcon(r"Search_Report\Search_icon.png"))
        self.hide_lineedit()
        self.style()

    def getusername(self, user_input):
        self.username = user_input

    def show_lineedit(self):
        self.price_low.show()
        self.price_high.show()

    def hide_lineedit(self):
        self.price_low.hide()
        self.price_high.hide()

    def style(self):
        self.search_label.setStyleSheet("background:none")
        self.filter_label.setStyleSheet("background:none")
        self.price_checkbox.setStyleSheet("background:none")
        self.incomecheckbox.setStyleSheet("background:none")
        self.costcheckbox.setStyleSheet("background:none")
        self.custom_period_check.setStyleSheet("background:none")
        self.start_label.setStyleSheet("background:none")
        self.end_label.setStyleSheet("background:none")
        self.calender_start.setStyleSheet("background:none")
        self.calender_end.setStyleSheet("background:none")
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

    def Geometry_without_calender(self):
        self.setFixedSize(531, 415)
        self.start_label.hide()
        self.end_label.hide()
        self.calender_start.hide()
        self.calender_end.hide()
        self.price_checkbox.setGeometry(41, 213, 136, 23)
        self.price_high.setGeometry(370, 213, 151, 27)
        self.price_low.setGeometry(196, 213, 151, 27)
        self.incomecheckbox.setGeometry(41, 253, 261, 22)
        self.costcheckbox.setGeometry(41, 293, 261, 22)
        self.return_btn.setGeometry(210, 322, 111, 41)
        self.search_label.setGeometry(219, 12, 111, 41)

    def Geometry_with_calender(self):
        self.setFixedSize(813, 684)
        self.search_label.setGeometry(370, 12, 111, 41)
        self.end_label.setGeometry(577, 196, 55, 16)
        self.start_label.setGeometry(190, 197, 41, 16)
        self.search_label.setGeometry(370, 12, 111, 41)
        self.calender_start.setGeometry(40, 220, 344, 195)
        self.calender_end.setGeometry(431, 220, 344, 195)
        self.price_checkbox.setGeometry(46, 449, 131, 22)
        self.price_low.setGeometry(209, 446, 151, 27)
        self.price_high.setGeometry(386, 446, 151, 27)
        self.incomecheckbox.setGeometry(46, 505, 261, 22)
        self.costcheckbox.setGeometry(47, 572, 261, 22)
        self.return_btn.setGeometry(636, 564, 111, 31)
        self.start_label.show()
        self.end_label.show()
        self.calender_start.show()
        self.calender_end.show()

    def reset_form(self):
        self.Geometry_without_calender()
        self.price_checkbox.setChecked(False)
        self.incomecheckbox.setChecked(False)
        self.costcheckbox.setChecked(False)
        self.custom_period_check.setChecked(False)
        self.search_lineedit.setText("")
        self.price_low.setText("")
        self.price_high.setText("")

    def change_Geometry(self):
        if self.custom_period_check.isChecked():
            self.Geometry_with_calender()
        else:
            self.Geometry_without_calender()

    def price_status(self):
        if self.price_checkbox.isChecked():
            self.show_lineedit()
        else:
            self.hide_lineedit()

    def search_btn_clicked(self):
        checkstr = True
        if len(self.search_lineedit.text()) == 0:
            Message.show_warning("Please Enter something to search!")
            checkstr = False
            return checkstr
        if self.price_checkbox.isChecked():
            if Valid.valid_amount(self.price_low.text()) == False:
                Message.show_warning("Invalid input for lower price!")
                checkstr = False
                return False
            if Valid.valid_amount(self.price_high.text()) == False:
                Message.show_warning("Invalid input for higher price!")
                checkstr = False
                return checkstr
            if (
                Valid.validate_limit_price(
                    self.price_high.text(), self.price_low.text()
                )
                == False
            ):
                Message.show_warning("higher price must be grater than lower price!")
                checkstr = False
                return checkstr
        return checkstr

    def incomecheckbox_status(self):
        return self.incomecheckbox.isChecked()

    def costcheckbox_status(self):
        return self.costcheckbox.isChecked()

    def ischeckbox_file(self):
        if self.incomecheckbox_status() and self.costcheckbox_status():
            return "both"
        elif self.incomecheckbox_status():
            return "income"
        elif self.costcheckbox_status():
            return "cost"
        else:
            return "every"

    def ischecbox_price(self):
        if self.price_checkbox.isChecked():
            return self.price_low.text(), self.price_high.text()
        else:
            return "no_input", "no_input"

    def format_date_calender(self):
        if self.custom_period_check.isChecked():
            start_date = self.calender_start.selectedDate()
            end_date = self.calender_end.selectedDate()
            formatted_start_date = start_date.toString("yyyy/MM/dd")
            self.start_year, self.start_month, self.start_day = map(
                int, formatted_start_date.split("/")
            )
            formatted_end_date = end_date.toString("yyyy/MM/dd")
            self.end_year, self.end_month, self.end_day = map(
                int, formatted_end_date.split("/")
            )
        return (
            self.start_year,
            self.start_month,
            self.start_day,
            self.end_year,
            self.end_month,
            self.end_day,
        )

    def search_text(self, text):
        flag = self.search_btn_clicked()
        res = ""
        if flag:
            files = self.ischeckbox_file()
            lower_price, higher_price = self.ischecbox_price()
            if files == "income":
                res = dbcontroler.search_text(text, ["UserIncome"], self.username)
            elif files == "cost":
                res = dbcontroler.search_text(text, ["UserCost"], self.username)
            elif files == "both":
                res = dbcontroler.search_text(
                    text, ["UserIncome", "UserCost"], self.username
                )
            elif files == "every":
                res = dbcontroler.search_text(
                    text, ["UserIncome", "UserCost", "UserCategories"], self.username
                )
        return res


class Report_Page(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"Search_Report\mainwindow_report.ui", self)
        self.setFixedSize(872, 600)
        self.setWindowIcon(QIcon(r"Search\Search_icon.png"))
        self.setWindowTitle("Search Box")
