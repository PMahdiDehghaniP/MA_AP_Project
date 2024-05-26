from SignupPage.Signup_Gui import Signup
from Welcome_Page.welcomGui import Welcome
from Main_page.main_page import Main_Page
from Forgot_page.forgot import *
from Login_Page.login_form import Login
import user as uv
from Income_page.income_page import Income
from Cost_Page.cost_page import Cost_Form
from PyQt5.QtWidgets import *
import re

###############################################
users_list_objects = []
######################################
app = QApplication([])
login_page = Login()
signup_page = Signup()
forgot_page = forgot()


def show_warning(message):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText("Warning")
    msg.setInformativeText(message)
    msg.setWindowTitle("Warning")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


def show_message(message):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("Done!")
    msg.setInformativeText(message)
    msg.setWindowTitle("Message")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


def welcome_signup_btn_clicked():
    signup_page.show()
    welcome_window.close()


def welcome_login_btn_clicked():
    login_page.show()
    welcome_window.close()


def signup_btn_login_clicked():
    login_page.close()
    signup_page.show()


def pass_btn_login_clicked():
    login_page.close()
    forgot_page.show()


def submit_signup_clicked():
    is_user_valid = True
    password_text = signup_page.Password_signup.text()
    first_name_text = signup_page.fname_signup.text()
    last_name_text = signup_page.lname_signup.text()
    email_text = signup_page.email_signup.text()
    birthday_text = signup_page.date_signup.text()
    phone_number_text = signup_page.phone_signup.text()
    city_text = signup_page.city_signup.text()
    username_text = signup_page.username.text()
    repeat_password_text = signup_page.repeatpasswprd_signup.text()
    if uv.validate_name(first_name_text) == False:
        show_warning("You Entered Inavlid First Name!")
        signup_page.fname_signup.setText("")
        is_user_valid = False
    if uv.validate_name(last_name_text) == False:
        show_warning("You Entered Invalid Last Name!")
        signup_page.lname_signup.setText("")
        is_user_valid = False
    if uv.validate_username(username_text) == False:
        show_warning("You Entered Invalid Username\nOr Already Taken!")
        signup_page.username.setText("")
        is_user_valid = False
    if uv.validate_password(password_text) == False:
        show_warning("You Entered Invalid Value\nFor Password!")
        signup_page.Password_signup.setText("")
        is_user_valid = False
    if uv.validate_email(email_text) == False:
        show_warning("You Entered Invalid Email!")
        signup_page.email_signup.setText("")
        is_user_valid = False
    if uv.validite_birthday(birthday_text) == False:
        show_warning("You Entered Invalid Birthday Date!")
        signup_page.date_signup.setText("")
        is_user_valid = False
    if uv.validate_phone_number(phone_number_text) == False:
        show_warning("You Entered Invalid Phone Number!")
        signup_page.phone_signup.setText("")
        is_user_valid = False
    if uv.validate_city(city_text) == False:
        show_warning("You Entered Invalid City!")
        signup_page.city_signup.setText("")
        is_user_valid = False
    if repeat_password_text != password_text:
        show_warning("Repeat password does not match the password!")
        signup_page.repeatpasswprd_signup.setText("")
        is_user_valid = False
    if is_user_valid:
        new_user = uv.User(
            first_name_text,
            last_name_text,
            username_text,
            phone_number_text,
            password_text,
            email_text,
            city_text,
            birthday_text,
        )
        show_message("user successfully created.")
        signup_page.repeatpasswprd_signup.setText("")
        signup_page.city_signup.setText("")
        signup_page.phone_signup.setText("")
        signup_page.date_signup.setText("")
        signup_page.date_signup.setText("")
        signup_page.Password_signup.setText("")
        signup_page.username.setText("")
        signup_page.lname_signup.setText("")
        signup_page.fname_signup.setText("")


welcome_window = Welcome()
welcome_window.show()
welcome_window.signup_btn.clicked.connect(welcome_signup_btn_clicked)
welcome_window.login_btn.clicked.connect(welcome_login_btn_clicked)
login_page.pass_forgot_login.clicked.connect(pass_btn_login_clicked)
login_page.signup_btn_login.clicked.connect(signup_btn_login_clicked)
signup_page.Submit_signup.clicked.connect(submit_signup_clicked)
app.exec_()
