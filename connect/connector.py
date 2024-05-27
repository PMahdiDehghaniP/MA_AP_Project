from JJson.jjson import CreateJson
import user as uv
from MessageBox.messagebox import Message_Box
from Login_Page.login_form import Login
from Forgot_page.forgot import forgot
from Welcome_Page.welcomGui import Welcome
from SignupPage.Signup_Gui import Signup
from PyQt5.QtWidgets import QApplication
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class Connector:
    def __init__(self):
        self.login_page = Login()
        self.signup_page = Signup()
        self.forgot_page = forgot()
        self.message = Message_Box()
        self.welcome_window = Welcome()
        self.connect_signals()

    def connect_signals(self):
        self.welcome_window.signup_btn.clicked.connect(
            self.welcome_signup_btn_clicked)
        self.welcome_window.login_btn.clicked.connect(
            self.welcome_login_btn_clicked)
        self.login_page.pass_forgot_login.clicked.connect(
            self.pass_btn_login_clicked)
        self.login_page.signup_btn_login.clicked.connect(
            self.signup_btn_login_clicked)
        self.signup_page.Submit_signup.clicked.connect(self.user_object_making)

    def welcome_signup_btn_clicked(self):
        self.signup_page.show()
        self.welcome_window.close()

    def welcome_login_btn_clicked(self):
        self.login_page.show()
        self.welcome_window.close()

    def signup_btn_login_clicked(self):
        self.login_page.close()
        self.signup_page.show()

    def pass_btn_login_clicked(self):
        self.login_page.close()
        self.forgot_page.show()

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
            self.message.show_message("user successfully created.")
            self.signup_page.repeatpasswprd_signup.setText("")
            self.signup_page.city_signup.setText("")
            self.signup_page.phone_signup.setText("")
            self.signup_page.date_signup.setText("")
            self.signup_page.date_signup.setText("")
            self.signup_page.Password_signup.setText("")
            self.signup_page.username.setText("")
            self.signup_page.lname_signup.setText("")
            self.signup_page.fname_signup.setText("")
            self.signup_page.email_signup.setText("")
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
