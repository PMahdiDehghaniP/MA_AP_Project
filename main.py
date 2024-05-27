from PyQt5.QtWidgets import *
from SignupPage.Signup_Gui import Signup
from Welcome_Page.welcomGui import Welcome
from Main_page.main_page import Main_Page
from Forgot_page.forgot import *
from Login_Page.login_form import Login
import user as uv
from Income_page.income_page import Income
from Cost_Page.cost_page import Cost_Form
import re
from MessageBox.messagebox import *
from JJson.jjson import *

###############################################
users_list_objects = []
######################################
app = QApplication([])
login_page = Login()
signup_page = Signup()
forgot_page = forgot()
message = Message_Box()


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


def user_object_making():
    flag = signup_page.submit_signup_clicked()
    if flag:
        new_user = uv.User(
            signup_page.fname_signup.text(),
            signup_page.lname_signup.text(),
            signup_page.username.text(),
            signup_page.phone_signup.text(),
            signup_page.Password_signup.text(),
            signup_page.email_signup.text(),
            signup_page.city_signup.text(),
            signup_page.date_signup.text(),
        )
        message.show_message("user successfully created.")
        signup_page.repeatpasswprd_signup.setText("")
        signup_page.city_signup.setText("")
        signup_page.phone_signup.setText("")
        signup_page.date_signup.setText("")
        signup_page.date_signup.setText("")
        signup_page.Password_signup.setText("")
        signup_page.username.setText("")
        signup_page.lname_signup.setText("")
        signup_page.fname_signup.setText("")
        signup_page.email_signup.setText("")
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
        handler = CreateJson("user.json")
        handler.add_dict_to_json(user_dict)


welcome_window = Welcome()
welcome_window.show()
welcome_window.signup_btn.clicked.connect(welcome_signup_btn_clicked)
welcome_window.login_btn.clicked.connect(welcome_login_btn_clicked)
login_page.pass_forgot_login.clicked.connect(pass_btn_login_clicked)
login_page.signup_btn_login.clicked.connect(signup_btn_login_clicked)
signup_page.Submit_signup.clicked.connect(user_object_making)
app.exec_()
