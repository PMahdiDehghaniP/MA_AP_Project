from PyQt5.QtCore import Qt, QTime
from PyQt5.QtWidgets import QLineEdit, QCheckBox
from SignupPage.Signup_Gui import Signup
from Welcome_Page.welcomGui import Welcome
from Forgot_page.forgot import forgot
from Login_Page.login_form import Login
from Main_page.main_page import Main_Page
from Timer.timer import Timer_Calc
from MessageBox.messagebox import Message_Box
from Income_page.income_page import Income
from Cost_Page.cost_page import Cost_Form
import user as uv
from JJson.jjson import CreateJson
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class Connector:
    def __init__(self):
        self.login_page = Login()
        self.main_page = Main_Page()
        self.signup_page = Signup()
        self.forgot_page = forgot()
        self.timer = Timer_Calc()
        self.income_page = Income()
        self.cost_page = Cost_Form()
        self.message = Message_Box()
        self.welcome_window = Welcome()
        self.connect_signals()

    def connect_signals(self):
        self.main_page.exit_mainpage_btn.clicked.connect(self.exit_main_page)
        self.main_page.record_income_btn.clicked.connect(self.show_income_form)
        self.income_page.exit_btn_income.clicked.connect(
            self.exit_income_btn_clicked)
        self.cost_page.exit_btn_cost.clicked.connect(
            self.exit_cost_btn_clicked)
        self.forgot_page.forgot_password_btn.clicked.connect(
            self.my_pass_btn_clicked)
        self.welcome_window.signup_btn.clicked.connect(
            self.welcome_signup_btn_clicked)
        self.welcome_window.login_btn.clicked.connect(
            self.welcome_login_btn_clicked)
        self.login_page.pass_forgot_login.clicked.connect(
            self.pass_btn_login_clicked)
        self.login_page.sign_in_login_btn.clicked.connect(
            self.login_sign_in_btn_clicked
        )
        self.login_page.signup_btn_login.clicked.connect(
            self.signup_btn_login_clicked)
        self.signup_page.Submit_signup.clicked.connect(self.user_object_making)
        self.login_page.show_pass_login.stateChanged.connect(
            self.toggle_echo_mode_show_pass
        )
        self.forgot_page.send_code_email.clicked.connect(
            self.send_code_clicked)

    def exit_main_page(self):
        self.timer.Calculation_until_present(self.main_page.first_time_login)
        self.message.show_message(
            f'''The spent time is {self.timer.hours} hours, {self.timer.minutes} minutes, and {self.timer.seconds} seconds.
Have fun.'''

        )
        self.main_page.close()

    def show_income_form(self):
        self.main_page.hide()
        self.income_page.show()

    def exit_income_btn_clicked(self):
        self.income_page.close()
        self.main_page.show()

    def exit_cost_btn_clicked(self):
        self.cost_page.close()
        self.main_page.show()

    def my_pass_btn_clicked(self):
        temp = self.forgot_page.show_password()
        if temp:
            self.forgot_page.close()
            self.login_page.show()

    def send_code_clicked(self):
        self.forgot_page.send_code()

    def welcome_signup_btn_clicked(self):
        self.signup_page.show()
        self.welcome_window.close()

    def toggle_echo_mode_show_pass(self, state):
        if state == Qt.Checked:
            self.login_page.password_login.setEchoMode(QLineEdit.Normal)
        else:
            self.login_page.password_login.setEchoMode(QLineEdit.Password)

    def welcome_login_btn_clicked(self):
        self.login_page.show()
        self.welcome_window.close()

    def signup_btn_login_clicked(self):
        self.login_page.close()
        self.signup_page.show()

    def pass_btn_login_clicked(self):
        self.login_page.reset_login()
        self.login_page.close()
        self.forgot_page.show()
        self.forgot_page.show_captcha()

    def login_sign_in_btn_clicked(self):
        if self.login_page.login_user() == "OK":
            self.login_page.close()
            self.main_page.show()
            self.main_page.set_first_login_time()
            self.main_page.set_user_info(self.login_page.email_login.text())

    def run(self):
        self.welcome_window.show()

    def user_object_making(self):
        handler = CreateJson("user.json")
        valid_inputs = self.signup_page.submit_signup_clicked()
        if valid_inputs:
            new_user = uv.User(
                self.signup_page.fname_signup.text(),
                self.signup_page.lname_signup.text(),
                self.signup_page.username.text(),
                self.signup_page.phone_signup.text(),
                self.signup_page.Password_signup.text(),
                self.signup_page.email_signup.text(),
                self.signup_page.city_signup.text(),
                self.signup_page.date_signup.text(),
            )
            self.message.show_message(
                "user successfully created.\nPlease Log in To Your Account"
            )
            self.signup_page.reset_signup()
            user_dict = {
                new_user.username: {
                    "email": new_user.email,
                    "password": new_user.password,
                    "fname": new_user.name,
                    "lname": new_user.lastname,
                    "phone": new_user.phone,
                    "birth": new_user.birthday,
                    "city": new_user.city,
                }
            }
            handler.add_dict_to_json(user_dict)
            self.signup_page.close()
            self.login_page.show()
