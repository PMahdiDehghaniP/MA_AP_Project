from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QTimer, Qt
from datacenter.projectdb import PDataBase
from MessageBox.messagebox import *
from Sound.back_sound import Sound
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


show_message = Message_Box()
db_controler = PDataBase()
music = Sound()


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.counter_try_login = 0
        self.username = ""
        uic.loadUi(r"Login_Page\mainwindow.ui", self)
        self.setWindowTitle("Login Page")
        self.setFixedSize(422, 440)
        self.setWindowIcon(QIcon(r"Login_Page\login_icon.png"))
        self.lineedit_style = """
            background:#DFDFDF;
            border:none;
            border-radius:5px;
            padding:0px 0px 0px 5px;
            font-size:14px;"""
        self.hotkey_style = """
            QPushButton{
            background:none;
            border:none;
            border-radius:5px;
            font-size:18px;
            }
            QPushButton:hover{
                color:#800004;
                border:1px solid #800004;
            }"""
        self.login_label.setStyleSheet("background:none;")
        self.forgot_login.setStyleSheet("background:none;")
        self.question.setStyleSheet("background:none;font-size:18px;")
        self.dont_acc_login.setStyleSheet("background:none;")
        self.time_rem_label.setStyleSheet("background:none;")
        self.time_rem_label.setText("")
        self.setStyleSheet(
            """
            background: qlineargradient(
            spread:pad, x1:0, y1:0, x2:1, y2:0,
            stop:0 #0093E9,
            stop:1 #80D0C7
        );"""
        )
        self.email_login.setStyleSheet(self.lineedit_style)
        self.password_login.setStyleSheet(self.lineedit_style)
        self.show_pass_login.setStyleSheet(
            """
            background:none;"""
        )
        self.sign_in_login_btn.setCursor(Qt.PointingHandCursor)
        self.sign_in_login_btn.setStyleSheet(
            """
            QPushButton{
            background: qlineargradient(
            spread:pad, x1:0, y1:0, x2:1, y2:0,
            stop:0 #8EC5FC,
            stop:1 #E0C3FC
            );
            border:none;
            border-radius:5px;
            font-size:14px;
            }
            QPushButton:hover{
            background: qlineargradient(
            spread:pad, x1:0, y1:0, x2:1, y2:0,
            stop:0 #c31432,
            stop:1 #240b36
            );
            color:yellow;
            }
            """
        )
        self.pass_forgot_login.setCursor(Qt.PointingHandCursor)
        self.pass_forgot_login.setStyleSheet(self.hotkey_style)
        self.signup_btn_login.setCursor(Qt.PointingHandCursor)
        self.signup_btn_login.setStyleSheet(self.hotkey_style)

    def login_user(self):
        flag_user = False
        flag_pass = False
        input_user = self.email_login.text()
        if self.counter_try_login < 3:
            if db_controler.return_username(input_user) == False:
                self.counter_try_login += 1
                music.play_warn_music()
                show_message.show_warning(
                    """There is no such user registered in the system.\n
    Please check the details again.\n
    If you don't have an account, please sign up."""
                )
                self.email_login.setText("")
                self.password_login.setText("")
                return
            else:
                flag_user = True

            if db_controler.get_password(input_user) == None:
                self.counter_try_login += 1
                music.play_warn_music()
                show_message.show_warning("Incorrect Password!\nTry Again!")
                self.password_login.setText("")
                return
            if self.password_login.text() == db_controler.get_password(input_user):
                flag_pass = True
            else:
                self.counter_try_login += 1
                music.play_warn_music()
                show_message.show_warning("Incorrect Password!\nTry Again!")
                self.password_login.setText("")
                return
            if flag_user == True and flag_pass == True:
                self.counter_try_login = 0
                music.play_message_music()
                show_message.show_message(
                    "You have successfully logged in. Welcome!")
                self.username = db_controler.return_username(input_user)
                return "OK"
        else:
            self.block_login_button()

    def reset_login(self):
        self.email_login.setText("")
        self.password_login.setText("")
        self.show_pass_login.setChecked(False)

    def block_login_button(self):
        self.reset_login()
        self.email_login.setEnabled(False)
        self.password_login.setEnabled(False)
        self.show_pass_login.setEnabled(False)
        self.sign_in_login_btn.setEnabled(False)
        QTimer.singleShot(60999, self.enable_login_elems)
        self.counter_try_login = 0
        music.play_warn_music()
        show_message.show_warning(
            "You have exceeded the maximum number of attempts. You are blocked for 1 minute."
        )
        self.start_timer()

    def start_timer(self):
        self.remaining_time = 60
        self.time_rem_label.setText(
            f"Remaining Time: {self.remaining_time} seconds")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(900)

    def update_timer(self):
        self.remaining_time -= 1
        self.time_rem_label.setText(
            f"Remaining Time: {self.remaining_time} seconds")
        if self.remaining_time == 0:
            self.timer.stop()
            self.enable_login_elems()

    def enable_login_elems(self):
        self.time_rem_label.setText("")
        self.sign_in_login_btn.setEnabled(True)
        self.email_login.setEnabled(True)
        self.password_login.setEnabled(True)
        self.show_pass_login.setEnabled(True)
