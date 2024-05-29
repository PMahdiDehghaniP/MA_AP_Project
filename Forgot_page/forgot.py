
from MessageBox.messagebox import Message_Box
from JJson.jjson import CreateJson
import random
import smtplib
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


Message = Message_Box()
Json_forgot = CreateJson("user.json")


class forgot(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"Forgot_page\mainwindow.ui", self)
        self.verification_code = 0
        self.setWindowTitle("Forgot Password Page")
        self.setFixedSize(499, 448)
        self.style()

    def style(self):
        self.setWindowIcon(QIcon(r"Forgot_page\forgot_icon.jpg"))
        self.setStyleSheet("background: #2173FF;")
        self.groupBox_forgot.setStyleSheet(
            """
                    background: white;
                    border-radius: 7px;
                                        """
        )
        self.em_us_forgot_linedit.setStyleSheet(
            "border: 0.5px solid black;padding-left: 5px;"
        )
        self.forgot_title.setStyleSheet("color: #000099;")
        self.kapcha.setStyleSheet("background: #E0E0E0;padding-left: 5px;")
        self.input_kapch_lineedit.setStyleSheet(
            "background: #E0E0E0;padding-left: 5px;"
        )
        self.forgot_password_btn.setCursor(Qt.PointingHandCursor)
        self.forgot_password_btn.setStyleSheet(
            """
            QPushButton { 
            border-radius:5px;
            font-size:16px;
            border:0.5px solid #38ef7d;
            background: #3399ff;
            }
            QPushButton:hover {
            background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #8E0E00,
                stop: 1 #1F1C18);
                border:none;
                color:Yellow;
                }
                """
        )
        self.code_email_lineedit.setStyleSheet(
            "background: #E0E0E0;padding-left: 5px;")
        self.send_code_email.setCursor(Qt.PointingHandCursor)
        self.send_code_email.setStyleSheet('''
            QPushButton { 
            border-radius:5px;
            font-size:16px;
            border:0.5px solid #38ef7d;
            background: #3399ff;
            }
            QPushButton:hover {
            background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #8E0E00,
                stop: 1 #1F1C18);
                border:none;
                color:Yellow;
                }
                                           
''')

    def show_captcha(self):
        captcha = self.make_captcha()
        self.kapcha.setText(captcha)

    def make_captcha(self):
        my_list = (
            list(chr(i) for i in range(65, 91))
            + list(chr(j) for j in range(97, 123))
            + list(x for x in range(0, 10))
        )
        temp_captcha = ""
        for i in range(6):
            temp_captcha += str(random.choice(my_list))
        return temp_captcha

    def check_captcha(self):
        captcha = self.kapcha.text()
        input_captcha = self.input_kapch_lineedit.text()
        if len(input_captcha) == 0:
            return "no_input_captcha"
        elif captcha == input_captcha:
            return "Valid_captcha"
        elif captcha != input_captcha:
            return "incorrect_captcha"

    def show_password(self):
        flag_captcha = self.check_captcha()
        if flag_captcha == "Valid_captcha":
            if Json_forgot.does_user_exist_for_forgotpage(self.em_us_forgot_linedit.text()) == "Valid":
                if str(self.verification_code) == self.code_email_lineedit.text():
                    data = Json_forgot.load_json_file()
                    for each_user in list(data.keys()):
                        if (
                            each_user == self.em_us_forgot_linedit.text()
                            or data[each_user]["email"] == self.em_us_forgot_linedit.text()
                        ):
                            Message.show_password(
                                f"Your Password is {data[each_user]['password']}")
                            self.em_us_forgot_linedit.setText("")
                            self.input_kapch_lineedit.setText("")
                            return True
                else:
                    Message.show_warning("You Entered Invalid Code Try Again")
                    self.em_us_forgot_linedit.setText("")
                    self.em_us_forgot_linedit.setText("")
                    self.code_email_lineedit.setText("")
                    return 

            elif Json_forgot.does_user_exist_for_forgotpage(self.em_us_forgot_linedit.text()) == "not found":
                Message.show_warning("There is no such person either.")
                self.show_captcha()
                return
        if flag_captcha == "no_input_captcha":
            Message.show_warning("You Didn't Entered Captcha!")
            self.show_captcha()
            self.em_us_forgot_linedit.setText("")
            return
        if flag_captcha == "incorrect_captcha":
            Message.show_warning("You Entered Incorroct Captcha!")
            self.show_captcha()
            self.em_us_forgot_linedit.setText("")
            self.input_kapch_lineedit.setText("")
            return

    def send_code(self):
        my_email = "mahdi14dehghani@gmail.com"
        self.verification_code = random.randint(100000, 999999)
        password = "yaxa icnh gtuf cxeg"
        smtp_port = 587
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            message = f"Subject: Verification Code\n\nYour verification code is: {self.verification_code}"
            connection.login(user=my_email, password=password)
            connection.sendmail(
                my_email, self.em_us_forgot_linedit.text(), message)
        Message.show_message("Code Has Been Sent To Your Email Please Check")
