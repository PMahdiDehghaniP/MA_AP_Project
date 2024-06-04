from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class Edit_profile(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(786, 544)
        uic.loadUi(r"edit_profile\mainwindow.ui", self)
        self.setWindowTitle("Edit Profile")
        self.setWindowIcon(QIcon(r"edit_profile\editprofile_icon.png"))
        self.style()
        self.hide_all()

    def hide_all(self):
        self.firstname.hide()
        self.lastname.hide()
        self.city.hide()
        self.password.hide()
        self.phonenumber.hide()
        self.birthday.hide()
        self.email.hide()

    def style(self):
        self.btn_style = """
        QPushButton{
            border-radius:4px;
        }
        QPushButton:hover{
        background: qlineargradient(
        spread:pad, x1:0, y1:0, x2:1, y2:0,
        stop:0 #D31027,
        stop:1 #EA384D
        );
        color:#ffffff;
        }
        """
        self.label_style = """background:none;"""
        self.lineedit_style = """
        padding-left:3px;
        border-radius:5px;
        background:#ffffff;
        """
        self.edit_profile_label.setStyleSheet(self.label_style)
        self.info_label.setStyleSheet(self.label_style)
        self.firstname.setStyleSheet(self.lineedit_style)
        self.lastname.setStyleSheet(self.lineedit_style)
        self.city.setStyleSheet(self.lineedit_style)
        self.password.setStyleSheet(self.lineedit_style)
        self.phonenumber.setStyleSheet(self.lineedit_style)
        self.birthday.setStyleSheet(self.lineedit_style)
        self.email.setStyleSheet(self.lineedit_style)
        self.fanme_checkbox.setStyleSheet(self.label_style)
        self.lastname_checkbox.setStyleSheet(self.label_style)
        self.city_checkbox.setStyleSheet(self.label_style)
        self.password_checkbox.setStyleSheet(self.label_style)
        self.phonenumber_checkbox.setStyleSheet(self.label_style)
        self.birthday_checkbox.setStyleSheet(self.label_style)
        self.email_checkbox.setStyleSheet(self.label_style)
        self.submit_btn.setStyleSheet(self.btn_style)
        self.submit_btn.setCursor(Qt.PointingHandCursor)
        self.return_btn_editform.setCursor(Qt.PointingHandCursor)
        self.return_btn_editform.setStyleSheet(self.btn_style)
        self.setStyleSheet(
            """
        background: qlineargradient(
        spread:pad, x1:0, y1:0, x2:1, y2:0,
        stop:0 #ffe259,
        stop:1 #ffa751
        );
        """
        )

    def reset_form(self):
        self.fanme_checkbox.setChecked(False)
        self.lastname_checkbox.setChecked(False)
        self.city_checkbox.setChecked(False)
        self.password_checkbox.setChecked(False)
        self.phonenumber_checkbox.setChecked(False)
        self.birthday_checkbox.setChecked(False)
        self.email_checkbox.setChecked(False)
        self.edit_profile_label.setText("")
        self.info_label.setText("")
        self.firstname.setText("")
        self.lastname.setText("")
        self.city.setText("")
        self.password.setText("")
        self.phonenumber.setText("")
        self.birthday.setText("")
        self.email.setText("")

    def show_lineedit(self, linedit_name):
        linedit_name.show()

    def hide_lineedit(self, linedit_name):
        linedit_name.hide()

    def fname_status(self):
        if self.fanme_checkbox.isChecked():
            self.show_lineedit(self.firstname)
        else:
            self.hide_lineedit(self.firstname)

    def lname_status(self):
        if self.lastname_checkbox.isChecked():
            self.show_lineedit(self.lastname)
        else:
            self.hide_lineedit(self.lastname)

    def city_status(self):
        if self.city_checkbox.isChecked():
            self.show_lineedit(self.city)
        else:
            self.hide_lineedit(self.city)

    def pass_status(self):
        if self.password_checkbox.isChecked():
            self.show_lineedit(self.password)
        else:
            self.hide_lineedit(self.password)

    def phonenumber_status(self):
        if self.phonenumber_checkbox.isChecked():
            self.show_lineedit(self.phonenumber)
        else:
            self.hide_lineedit(self.phonenumber)

    def birthday_status(self):
        if self.birthday_checkbox.isChecked():
            self.show_lineedit(self.birthday)
        else:
            self.hide_lineedit(self.birthday)

    def email_status(self):
        if self.email_checkbox.isChecked():
            self.show_lineedit(self.email)
        else:
            self.hide_lineedit(self.email)
