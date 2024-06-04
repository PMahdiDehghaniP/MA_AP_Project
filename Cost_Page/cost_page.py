from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from datacenter.projectdb import PDataBase
import sys
from PyQt5.QtWidgets import QWidget
from validates.validate import *
from MessageBox.messagebox import *
from Sound.back_sound import Sound

Valid = Validate()
Message = Message_Box()
db_controler = PDataBase()
music = Sound()


class Cost_Form(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"Cost_Page\cost_page.ui", self)
        self.setFixedSize(370, 710)
        self.setWindowTitle("Cost Page")
        self.setWindowIcon(QIcon(r"Cost_Page\cost_icon.png"))
        self.lineedit_style = """
            border : 1px solid grey;
            border-radius:6px;
            padding:0px 0px 0px 5px;
            color : #ffffff; """
        self.btn_style = """
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
            );}"""
        self.style()

    def style(self):
        self.setStyleSheet(
            """
            background: qlineargradient(
            spread:pad, x1:0, y1:0, x2:1, y2:0,
            stop:0 #44A08D,
            stop:1 #093637
        );"""
        )
        self.cost_form_label.setStyleSheet("""background: none;color:#ffffff;""")
        self.cost_amount.setStyleSheet(self.lineedit_style)
        self.cost_type_combo.setStyleSheet(self.lineedit_style)
        self.cost_date.setStyleSheet(self.lineedit_style)
        self.cost_resource.setStyleSheet(self.lineedit_style)
        self.description_cost.setStyleSheet(self.lineedit_style)
        self.submit_cost_page_btn.setCursor(Qt.PointingHandCursor)
        self.submit_cost_page_btn.setStyleSheet(self.btn_style)
        self.exit_btn_cost.setCursor(Qt.PointingHandCursor)
        self.exit_btn_cost.setStyleSheet(self.btn_style)

    def cost_combo_items(self, username):
        category_list = db_controler.return_list_of_category(username)
        for item in category_list:
            self.cost_resource.addItem(item)

    def cost_type_items(self):
        if self.cost_type_combo.count() == 0:
            cost_types = ["Cryptocurrency", "Check", "Cash"]
            for item in cost_types:
                self.cost_type_combo.addItem(item)

    def submit_cost_clicked(self):
        amount_cost = Valid.valid_amount(self.cost_amount.text())
        date_cost = Valid.validate_date_income_cost(self.cost_date.text())
        discription_cost = Valid.valid_description(self.description_cost.toPlainText())
        is_valid_cost = True
        if amount_cost == False:
            music.play_warn_music()
            Message.show_warning("Invalid cost amount.")
            self.cost_amount.setText("")
            is_valid_cost = False
            return is_valid_cost
        if date_cost == False:
            music.play_warn_music()
            Message.show_warning("Invalid cost date.")
            self.cost_date.setText("")
            is_valid_cost = False
            return is_valid_cost
        if discription_cost == False:
            music.play_warn_music()
            Message.show_warning("The text here cannot be more than 100 characters.")
            is_valid_cost = False
            return is_valid_cost
        return is_valid_cost

    def add_record_cost(self, user, amount, date, resource, ttype, discription):
        db_controler.add_new_IC(
            "UserCost", user, amount, date, resource, ttype, discription
        )
        return True

    def reset_cost(self):
        self.cost_amount.setText("")
        self.cost_date.setText("")
        self.description_cost.setText("")
        self.cost_resource.clear()
