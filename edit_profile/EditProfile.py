from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from validates.validate import Validate
from MessageBox.messagebox import Message_Box
from Sound.back_sound import Sound
from datacenter.projectdb import PDataBase
checker = Validate()
show_message = Message_Box()
media_player = Sound()
db_controler = PDataBase()


class Edit_profile(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(786, 544)
        uic.loadUi(r"edit_profile\mainwindow.ui", self)
        self.setWindowTitle("Edit Profile")
        self.setWindowIcon(QIcon(r"edit_profile\editprofile_icon.png"))
        self.style()
        self.hide_all()
        self.cityOpthoin = [
            "yazd",
            "tehran",
            "shiraz",
            """mash'had""",
            "Gheshm",
            "kermanshah",
            "bushehr",
            "ahvaz",
            "kordestan",
            "isfahan",
        ]
        completer = QCompleter(self.cityOpthoin, self.city)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.city.setCompleter(completer)

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

    def sumbit_clicked(self, username):
        flag_check = False
        fname = lname = city = password = phonenumber = birthday = email = ""
        if self.firstname.text():
            if checker.validate_name(self.firstname.text()):
                fname = self.firstname.text()
                flag_check = True
            else:
                media_player.play_warn_music()
                show_message.show_warning("Invalid Firstname")
                return
        if self.lastname.text():
            if checker.validate_name(self.lastname.text()):
                lname = self.lastname.text()
                flag_check = True
            else:
                media_player.play_warn_music()
                show_message.show_warning("Invalid Lastname")
                return
        if self.city.text():
            if checker.validate_city(self.city.text()):
                city = self.city.text()
                flag_check = True
            else:
                media_player.play_warn_music()
                show_message.show_warning("Invalid City Name")
                return
        if self.password.text():
            if checker.validate_password(self.password.text()):
                password = self.password.text()
                flag_check = True
            else:
                media_player.play_warn_music()
                show_message.show_warning("Invalid Password")
                return
        if self.phonenumber.text():
            if checker.validate_phone_number(self.phonenumber.text()):
                phonenumber = self.phonenumber.text()
                flag_check = True
            else:
                media_player.play_warn_music()
                show_message.show_warning("Invalid Phonenumber")
                return
        if self.birthday.text():
            if checker.validite_birthday(self.birthday.text()):
                birthday = self.birthday.text()
                flag_check = True
            else:
                media_player.play_warn_music()
                show_message.show_warning("Invalid birthday Date")
                return
        if self.email.text():
            if checker.validate_email(self.email.text()):
                email = self.email.text()
                flag_check = True
            else:
                media_player.play_warn_music()
                show_message.show_warning("Invalid email")
                return
        if flag_check:
            db_controler.update_user_data(
                username, fname, lname, email, phonenumber, password, city, birthday)
            return True
        return False
