from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from MessageBox.messagebox import Message_Box
from validates.validate import Validate
import sys
from PyQt5.QtWidgets import QWidget


income_message = Message_Box()
income_validation = Validate()


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
        pass
        # if self.income_resource.count() == 0:
        #     category_list = category_adder.return_list_of_category(username)
        #     for item in category_list:
        #         self.income_resource.addItem(item)

    def income_type_items(self):
        if self.income_type_combo.count() == 0:
            income_types = ["Cryptocurrency", "Check", "Cash"]
            for item in income_types:
                self.income_type_combo.addItem(item)

    def submit_income_clicked(self):
        amount_income = income_validation.valid_amount(
            self.income_amount_linedit.text())
        date_income = income_validation.validate_date_income_cost(
            self.income_date_linedit.text())
        discription_income = income_validation.valid_description(
            self.income_discription_linedit.toPlainText())
        is_valid_income = True
        if amount_income == False:
            income_message.show_warning("Invalid income amount.")
            self.income_amount_linedit.setText("")
            is_valid_income = False
            return is_valid_income
        if date_income == False:
            income_message.show_warning("Invalid income date.")
            self.income_date_linedit.setText("")
            is_valid_income = False
            return is_valid_income
        if discription_income == False:
            income_message.show_warning(
                "The text here cannot be more than 100 characters.")
            is_valid_income = False
            return is_valid_income
        return is_valid_income

    def add_record_income(self, user, amount, date, resource, ttype, discription):
        # recent_income_data = income_json.return_records(user)
        # recent_income_data["amount"].append(amount)
        # recent_income_data["date"].append(date)
        # recent_income_data["resource"].append(resource)
        # recent_income_data["type"].append(ttype)
        # recent_income_data["description"].append(discription)
        # data = {user: recent_income_data}
        # income_json.add_dict_to_json(data)
        return True

    def reset_income(self):
        self.income_amount_linedit.setText("")
        self.income_date_linedit.setText("")
        self.income_discription_linedit.setText("")
        self.income_resource.clear()
