from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import Qt
from validates.validate import *
from MessageBox.messagebox import *
from datacenter.projectdb import PDataBase
from datetime import datetime, timedelta
from Sound.back_sound import Sound

Valid = Validate()
Message = Message_Box()
dbcontroler = PDataBase()
music = Sound()


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
            music.play_warn_music()
            Message.show_warning("Please Enter something to search!")
            checkstr = False
            return
        if self.price_checkbox.isChecked():
            if Valid.valid_amount(self.price_low.text()) == False:
                music.play_warn_music()
                Message.show_warning("Invalid input for lower price!")
                checkstr = False
                return
            if Valid.valid_amount(self.price_high.text()) == False:
                music.play_warn_music()
                Message.show_warning("Invalid input for higher price!")
                checkstr = False
                return
            if (
                Valid.validate_limit_price(
                    self.price_high.text(), self.price_low.text()
                )
                == False
            ):
                music.play_warn_music()
                Message.show_warning("higher price must be grater than lower price!")
                checkstr = False
                return
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
            return None, None

    def format_date_calender(self):
        if self.custom_period_check.isChecked():
            start_date = self.calender_start.selectedDate()
            end_date = self.calender_end.selectedDate()
            formatted_start_date = start_date.toString("yyyy/MM/dd")
            formatted_end_date = end_date.toString("yyyy/MM/dd")
            return formatted_start_date, formatted_end_date
        else:
            return None, None

    def search_text(
        self, text, start_date=None, end_date=None, lower_price=None, higher_price=None
    ):
        flag = self.search_btn_clicked()
        res = ""
        if flag:
            files = self.ischeckbox_file()
            if files == "income":
                res = dbcontroler.search_text(
                    text=text,
                    tables=["UserIncome"],
                    username=self.username,
                    start_date=start_date,
                    end_date=end_date,
                    lower_price=lower_price,
                    higher_price=higher_price,
                )
            elif files == "cost":
                res = dbcontroler.search_text(
                    text=text,
                    tables=["UserCost"],
                    username=self.username,
                    start_date=start_date,
                    end_date=end_date,
                    lower_price=lower_price,
                    higher_price=higher_price,
                )
            elif files == "both":
                res = dbcontroler.search_text(
                    text=text,
                    tables=["UserIncome", "UserCost"],
                    username=self.username,
                    start_date=start_date,
                    end_date=end_date,
                    lower_price=lower_price,
                    higher_price=higher_price,
                )
            elif files == "every":
                res = dbcontroler.search_text(
                    text=text,
                    tables=["UserIncome", "UserCost", "UserCategories"],
                    username=self.username,
                    start_date=start_date,
                    end_date=end_date,
                    lower_price=lower_price,
                    higher_price=higher_price,
                )
        return res


class Report_Page(QMainWindow):
    def __init__(self):
        super().__init__()
        self.username = ""
        self.setFixedSize(849, 660)
        uic.loadUi(r"Search_Report\mainwindow_report.ui", self)
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
        self.setWindowTitle("Report Form")
        self.setWindowIcon(QIcon(r"Search_Report\report_icon.png"))
        self.hide_price_lineedit()
        self.hide_resource_lineedit()
        self.hide_type_lineedit()
        self.style()

    def style(self):
        self.yesterday_radio.setStyleSheet("background:none")
        self.lastweek_radio.setStyleSheet("background:none")
        self.lastmonth_radio.setStyleSheet("background:none")
        self.last3month_radio.setStyleSheet("background:none")
        self.custom_period_radio.setStyleSheet("background:none")
        self.filter_label.setStyleSheet("background:none")
        self.report_label.setStyleSheet("background:none")
        self.cost_checkbox.setStyleSheet("background:none")
        self.income_checkbox.setStyleSheet("background:none")
        self.price_checkbox.setStyleSheet("background:none")
        self.type_checkbox.setStyleSheet("background:none")
        self.resource_checkbox.setStyleSheet("background:none")
        self.start_label.setStyleSheet("background:none")
        self.end_label.setStyleSheet("background:none")
        self.calender_start.setStyleSheet("background:none")
        self.calender_end.setStyleSheet("background:none")
        self.price_low.setStyleSheet(self.lineedit_style)
        self.price_high.setStyleSheet(self.lineedit_style)
        self.resource_lineedit.setStyleSheet(self.lineedit_style)
        self.type_lineedit.setStyleSheet(self.lineedit_style)
        self.return_btn.setCursor(Qt.PointingHandCursor)
        self.report_btn.setCursor(Qt.PointingHandCursor)
        self.setStyleSheet(
            """
            background: qlineargradient(
            spread:pad, x1:0, y1:0, x2:1, y2:0,
            stop:0 #00B4DB,
            stop:1 #0083B0
        );"""
        )
        self.report_btn.setStyleSheet(self.btn_style)
        self.return_btn.setStyleSheet(self.btn_style)

    def getusername(self, user_input):
        self.username = user_input

    def Geometry_without_calender(self):
        self.setFixedSize(849, 415)
        self.start_label.hide()
        self.end_label.hide()
        self.calender_start.hide()
        self.calender_end.hide()
        self.price_checkbox.setGeometry(40, 170, 131, 22)
        self.price_high.setGeometry(350, 170, 151, 27)
        self.price_low.setGeometry(190, 170, 151, 27)
        self.type_checkbox.setGeometry(43, 261, 151, 27)
        self.type_lineedit.setGeometry(189, 259, 151, 27)
        self.resource_checkbox.setGeometry(360, 262, 131, 22)
        self.resource_lineedit.setGeometry(490, 258, 181, 27)
        self.return_btn.setGeometry(699, 256, 111, 31)
        self.report_btn.setGeometry(270, 310, 321, 51)

    def Geometry_with_calender(self):
        self.setFixedSize(813, 684)
        self.report_label.setGeometry(370, 12, 111, 41)
        self.calender_start.setGeometry(40, 220, 344, 195)
        self.calender_end.setGeometry(431, 220, 344, 195)
        self.income_checkbox.setGeometry(39, 62, 83, 22)
        self.cost_checkbox.setGeometry(144, 62, 83, 22)
        self.end_label.setGeometry(577, 196, 55, 16)
        self.start_label.setGeometry(190, 197, 41, 16)
        self.price_checkbox.setGeometry(46, 449, 131, 22)
        self.price_low.setGeometry(209, 446, 151, 27)
        self.price_high.setGeometry(386, 446, 151, 27)
        self.return_btn.setGeometry(622, 444, 111, 31)
        self.type_checkbox.setGeometry(49, 508, 111, 22)
        self.resource_checkbox.setGeometry(389, 505, 131, 22)
        self.type_lineedit.setGeometry(208, 502, 151, 27)
        self.resource_lineedit.setGeometry(528, 502, 181, 27)
        self.report_btn.setGeometry(270, 559, 321, 51)
        self.start_label.show()
        self.end_label.show()
        self.calender_start.show()
        self.calender_end.show()

    def reset_form(self):
        self.Geometry_without_calender()
        self.yesterday_radio.setChecked(True)
        self.lastweek_radio.setChecked(False)
        self.lastmonth_radio.setChecked(False)
        self.last3month_radio.setChecked(False)
        self.custom_period_radio.setChecked(False)
        self.price_checkbox.setChecked(False)
        self.income_checkbox.setChecked(False)
        self.cost_checkbox.setChecked(False)
        self.type_checkbox.setChecked(False)
        self.resource_checkbox.setChecked(False)
        self.price_low.setText("")
        self.price_high.setText("")
        self.type_lineedit.setText("")
        self.resource_lineedit.setText("")

    def change_Geometry(self):
        if self.custom_period_radio.isChecked():
            self.Geometry_with_calender()
        else:
            self.Geometry_without_calender()

    def price_status(self):
        if self.price_checkbox.isChecked():
            self.show_price_lineedit()
        else:
            self.hide_price_lineedit()

    def show_price_lineedit(self):
        self.price_low.show()
        self.price_high.show()

    def hide_price_lineedit(self):
        self.price_low.hide()
        self.price_high.hide()

    def type_status(self):
        if self.type_checkbox.isChecked():
            self.show_type_lineedit()
        else:
            self.hide_type_lineedit()

    def show_type_lineedit(self):
        self.type_lineedit.show()

    def hide_type_lineedit(self):
        self.type_lineedit.hide()

    def resource_status(self):
        if self.resource_checkbox.isChecked():
            self.show_resource_lineedit()
        else:
            self.hide_resource_lineedit()

    def show_resource_lineedit(self):
        self.resource_lineedit.show()

    def hide_resource_lineedit(self):
        self.resource_lineedit.hide()

    def format_date_calender(self):
        end_date = datetime.today()
        start_date = ""
        if self.yesterday_radio.isChecked():
            start_date = end_date - timedelta(days=1)
        elif self.lastweek_radio.isChecked():
            start_date = end_date - timedelta(weeks=1)
        elif self.lastmonth_radio.isChecked():
            start_date = end_date - timedelta(days=30)
        elif self.last3month_radio.isChecked():
            start_date = end_date - timedelta(days=90)
        elif self.custom_period_radio.isChecked():
            start_date = self.calender_start.selectedDate().toPyDate()
            end_date = self.calender_end.selectedDate().toPyDate()
        if start_date and end_date:
            formatted_start_date = start_date.strftime("%Y/%m/%d")
            formatted_end_date = end_date.strftime("%Y/%m/%d")
            return formatted_start_date, formatted_end_date
        else:
            return None, None

    def income_checkbox_status(self):
        return self.income_checkbox.isChecked()

    def cost_checkbox_status(self):
        return self.cost_checkbox.isChecked()

    def ischeckbox_file(self):
        if self.income_checkbox_status() and self.cost_checkbox_status():
            return "both"
        elif self.income_checkbox_status():
            return "income"
        elif self.cost_checkbox_status():
            return "cost"
        else:
            return "every"

    def ischecbox_price(self):
        if self.price_checkbox.isChecked():
            return self.price_low.text(), self.price_high.text()
        else:
            return None, None

    def ischecbox_type(self):
        if self.type_checkbox.isChecked():
            return self.type_lineedit.text()
        else:
            return None

    def ischecbox_resource(self):
        if self.resource_checkbox.isChecked():
            return self.resource_lineedit.text()
        else:
            return None

    def get_report_clicked(self):
        check_flag = True
        if self.price_checkbox.isChecked():
            if Valid.valid_amount(self.price_low.text()) == False:
                music.play_warn_music()
                Message.show_warning("Invalid input for lower price!")
                check_flag = False
                return check_flag
            if Valid.valid_amount(self.price_high.text()) == False:
                music.play_warn_music()
                Message.show_warning("Invalid input for higher price!")
                check_flag = False
                return check_flag
            if (
                Valid.validate_limit_price(
                    self.price_high.text(), self.price_low.text()
                )
                == False
            ):
                music.play_warn_music()
                Message.show_warning("higher price must be grater than lower price!")
                check_flag = False
                return check_flag
        return check_flag

    def report_text(
        self,
        start_date=None,
        end_date=None,
        lower_price=None,
        higher_price=None,
        resource=None,
        item_type=None,
    ):
        flag = self.get_report_clicked()
        res = ""
        if flag:
            files = self.ischeckbox_file()
            if files == "income":
                res = dbcontroler.search_text(
                    tables=["UserIncome"],
                    username=self.username,
                    start_date=start_date,
                    end_date=end_date,
                    lower_price=lower_price,
                    higher_price=higher_price,
                    resource=resource,
                    item_type=item_type,
                )
            elif files == "cost":
                res = dbcontroler.search_text(
                    tables=["UserCost"],
                    username=self.username,
                    start_date=start_date,
                    end_date=end_date,
                    lower_price=lower_price,
                    higher_price=higher_price,
                    resource=resource,
                    item_type=item_type,
                )
            elif files == "both" or files == "every":
                res = dbcontroler.search_text(
                    tables=["UserIncome", "UserCost"],
                    username=self.username,
                    start_date=start_date,
                    end_date=end_date,
                    lower_price=lower_price,
                    higher_price=higher_price,
                    resource=resource,
                    item_type=item_type,
                )
        return res
