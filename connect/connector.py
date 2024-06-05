from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit
from SignupPage.Signup_Gui import Signup
from Welcome_Page.welcomGui import Welcome
from Forgot_page.forgot import forgot
from Login_Page.login_form import Login
from Main_page.main_page import Main_Page
from Timer.timer import Timer_Calc
from Category.category import Category_Page
from Search_Report.search import Search_Page, Report_Page
from MessageBox.messagebox import Message_Box
from Income_page.income_page import Income
from Cost_Page.cost_page import Cost_Form
from datacenter.projectdb import PDataBase
from Sound.back_sound import Sound
from Setting_Page.setting_p import Setting_Page
from edit_profile.EditProfile import Edit_profile
from Chart.matpl import Matplot
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


#############################################################################


class Connector:
    def __init__(self):
        self.music = Sound()
        self.music.play_background_music()
        self.setting_page = Setting_Page()
        self.edit_form = Edit_profile()
        self.database = PDataBase()
        self.login_page = Login()
        self.main_page = Main_Page()
        self.search_page = Search_Page()
        self.signup_page = Signup()
        self.category_page = Category_Page()
        self.forgot_page = forgot()
        self.timer = Timer_Calc()
        self.income_page = Income()
        self.cost_page = Cost_Form()
        self.message = Message_Box()
        self.welcome_window = Welcome()
        self.report_page = Report_Page()
        self.matp = Matplot()
        self.connect_signals()

    #############################################################################
    # Signals

    def connect_signals(self):

        self.signup_page.Submit_signup.clicked.connect(self.music.play_click_music)
        self.signup_page.Submit_signup.clicked.connect(self.user_object_making)

        self.signup_page.return_signup.clicked.connect(self.return_signup_page)
        ###################

        self.cost_page.exit_btn_cost.clicked.connect(self.music.play_click_music)
        self.cost_page.exit_btn_cost.clicked.connect(self.exit_cost_btn_clicked)

        self.cost_page.submit_cost_page_btn.clicked.connect(self.music.play_click_music)
        self.cost_page.submit_cost_page_btn.clicked.connect(self.cost_submit_clicked)
        # ###################

        self.category_page.category_submit.clicked.connect(self.music.play_click_music)
        self.category_page.category_submit.clicked.connect(self.category_submit_clicked)

        self.category_page.category_exit.clicked.connect(self.music.play_click_music)
        self.category_page.category_exit.clicked.connect(self.category_exit_clicked)
        ###################

        self.main_page.category_btn.clicked.connect(self.music.play_click_music)
        self.main_page.category_btn.clicked.connect(self.show_category_page)

        self.main_page.exit_mainpage_btn.clicked.connect(self.music.play_click_music)
        self.main_page.exit_mainpage_btn.clicked.connect(self.exit_main_page)

        self.main_page.record_income_btn.clicked.connect(self.music.play_click_music)
        self.main_page.record_income_btn.clicked.connect(self.show_income_form)

        self.main_page.record_cost_btn.clicked.connect(self.music.play_click_music)
        self.main_page.record_cost_btn.clicked.connect(self.show_cost_form)

        self.main_page.search_btn.clicked.connect(self.music.play_click_music)
        self.main_page.search_btn.clicked.connect(self.show_search_page)

        self.main_page.report_btn.clicked.connect(self.music.play_click_music)
        self.main_page.report_btn.clicked.connect(self.show_report_page)

        self.main_page.setting_btn.clicked.connect(self.music.play_click_music)
        self.setting_page.bg_on_radio.setChecked(True)
        self.setting_page.btn_radio_on.setChecked(True)
        self.setting_page.msg_radio_on.setChecked(True)
        self.main_page.setting_btn.clicked.connect(self.show_setting_form)
        ###################

        self.income_page.exit_btn_income.clicked.connect(self.music.play_click_music)
        self.income_page.exit_btn_income.clicked.connect(self.exit_income_btn_clicked)

        self.income_page.income_submit_btn.clicked.connect(self.music.play_click_music)
        self.income_page.income_submit_btn.clicked.connect(self.income_submit_clikced)
        ###################

        self.forgot_page.forgot_password_btn.clicked.connect(
            self.music.play_click_music
        )
        self.forgot_page.forgot_password_btn.clicked.connect(self.my_pass_btn_clicked)

        self.forgot_page.send_code_email.clicked.connect(self.music.play_click_music)
        self.forgot_page.send_code_email.clicked.connect(self.send_code_clicked)
        ###################

        self.welcome_window.signup_btn.clicked.connect(self.music.play_click_music)
        self.welcome_window.signup_btn.clicked.connect(self.welcome_signup_btn_clicked)

        self.welcome_window.login_btn.clicked.connect(self.music.play_click_music)
        self.welcome_window.login_btn.clicked.connect(self.welcome_login_btn_clicked)
        ###################
        self.login_page.pass_forgot_login.clicked.connect(self.music.play_click_music)
        self.login_page.pass_forgot_login.clicked.connect(self.pass_btn_login_clicked)

        self.login_page.sign_in_login_btn.clicked.connect(self.music.play_click_music)
        self.login_page.sign_in_login_btn.clicked.connect(
            self.login_sign_in_btn_clicked
        )

        self.login_page.signup_btn_login.clicked.connect(self.music.play_click_music)
        self.login_page.signup_btn_login.clicked.connect(self.signup_btn_login_clicked)

        self.login_page.show_pass_login.stateChanged.connect(
            self.toggle_echo_mode_show_pass
        )
        ###################
        self.search_page.return_btn.clicked.connect(self.music.play_click_music)
        self.search_page.return_btn.clicked.connect(self.search_return_btn_clicked)

        self.search_page.price_checkbox.stateChanged.connect(self.price_checkbox_status)

        self.search_page.search_btn.clicked.connect(self.music.play_click_music)
        self.search_page.search_btn.clicked.connect(self.search_btn_clicked)

        self.search_page.custom_period_check.stateChanged.connect(
            self.search_page.change_Geometry
        )
        ###################
        self.report_page.custom_period_radio.toggled.connect(
            self.report_page.change_Geometry
        )

        self.report_page.price_checkbox.stateChanged.connect(
            self.report_page.price_status
        )

        self.report_page.type_checkbox.stateChanged.connect(
            self.report_page.type_status
        )

        self.report_page.resource_checkbox.stateChanged.connect(
            self.report_page.resource_status
        )

        self.report_page.return_btn.clicked.connect(self.music.play_click_music)
        self.report_page.return_btn.clicked.connect(self.report_return_btn_clicked)

        self.report_page.report_btn.clicked.connect(self.music.play_click_music)
        self.report_page.report_btn.clicked.connect(self.get_report_btn_clicked)
        self.report_page.report_btn.clicked.connect(self.show_chart_report)

        ################################

        self.setting_page.return_setting_btn.clicked.connect(
            self.music.play_click_music
        )
        self.setting_page.return_setting_btn.clicked.connect(
            self.return_setting_clicked
        )

        self.setting_page.delete_all_transaction.clicked.connect(
            self.music.play_click_music
        )

        self.setting_page.delete_user.clicked.connect(self.music.play_click_music)

        self.setting_page.delete_income_transaction.clicked.connect(
            self.music.play_click_music
        )

        self.setting_page.delete_cost_transaction.clicked.connect(
            self.music.play_click_music
        )

        self.setting_page.export_csv_btn.clicked.connect(self.music.play_click_music)

        self.setting_page.bg_off_radio.toggled.connect(self.music.stop_background_music)
        self.setting_page.bg_on_radio.toggled.connect(self.music.play_background_music)

        self.setting_page.btn_radio_on.toggled.connect(self.music.on_click_music)
        self.setting_page.btn_radio_off.toggled.connect(self.music.off_click_music)

        self.setting_page.msg_radio_off.toggled.connect(self.music.off_message_music)
        self.setting_page.msg_radio_on.toggled.connect(self.music.on_message_music)

        self.setting_page.edit_profile_btn.clicked.connect(self.music.play_click_music)
        self.setting_page.edit_profile_btn.clicked.connect(self.show_edit_form)

        self.setting_page.delete_all_transaction.clicked.connect(self.delete_trans)

        self.setting_page.delete_user.clicked.connect(self.delete_user)

        self.setting_page.delete_income_transaction.clicked.connect(self.delete_income)

        self.setting_page.delete_cost_transaction.clicked.connect(self.delete_cost)
        self.setting_page.export_csv_btn.clicked.connect(self.export_user_data)

        #############################################################################
        self.edit_form.fanme_checkbox.stateChanged.connect(self.edit_form.fname_status)
        self.edit_form.lastname_checkbox.stateChanged.connect(
            self.edit_form.lname_status
        )
        self.edit_form.city_checkbox.stateChanged.connect(self.edit_form.city_status)
        self.edit_form.password_checkbox.stateChanged.connect(
            self.edit_form.pass_status
        )
        self.edit_form.phonenumber_checkbox.stateChanged.connect(
            self.edit_form.phonenumber_status
        )
        self.edit_form.birthday_checkbox.stateChanged.connect(
            self.edit_form.birthday_status
        )
        self.edit_form.email_checkbox.stateChanged.connect(self.edit_form.email_status)

        self.edit_form.submit_btn.clicked.connect(self.music.play_click_music)
        self.edit_form.submit_btn.clicked.connect(
            self.submit_edit_form_btn_clciked
        )  # we'll completed later

        self.edit_form.return_btn_editform.clicked.connect(self.music.play_click_music)
        self.edit_form.return_btn_editform.clicked.connect(self.return_edit_form)

    #############################################################################

    def exit_main_page(self):
        self.timer.Calculation_until_present(self.main_page.first_time_login)
        self.music.play_message_music()
        self.message.show_message(
            f"""The spent time is {self.timer.hours} hours, {self.timer.minutes} minutes, and {self.timer.seconds} seconds.
Have fun."""
        )
        self.music.stop_background_music()
        self.main_page.close()

    #############################################################################
    # category

    def category_submit_clicked(self):
        if self.category_page.add_category(
            self.category_page.category_lineedit.text(), self.login_page.username
        ):
            self.music.play_message_music()
            self.message.show_message("Category Successfully Added!")
            self.category_page.reset_category()
        else:
            self.music.play_warn_music()
            self.message.show_warning("Invalid Category Or Its Already Added!")
            self.category_page.reset_category()

    def category_exit_clicked(self):
        self.category_page.close()
        self.main_page.show()

    def show_category_page(self):
        self.main_page.hide()
        self.category_page.show()

    #############################################################################
    # income

    def show_income_form(self):
        if self.category_page.check_exist_category(self.login_page.username):
            self.main_page.hide()
            self.income_page.income_combo_items(self.login_page.username)
            self.income_page.income_type_items()
            self.income_page.show()
        else:
            self.music.play_warn_music()
            self.message.show_warning(
                """You haven't added any category!
first add at least 1 category to open income form."""
            )

    def income_submit_clikced(self):
        valid_income_page = self.income_page.submit_income_clicked()
        if valid_income_page:
            self.income_page.add_record_income(
                self.login_page.username,
                self.income_page.income_amount_linedit.text(),
                self.income_page.income_date_linedit.text(),
                self.income_page.income_resource.currentText(),
                self.income_page.income_type_combo.currentText(),
                self.income_page.income_discription_linedit.toPlainText(),
            )
            self.music.play_message_music()
            self.message.show_message("Your Income has been recorded.")
            self.income_page.reset_income()
            self.income_page.income_combo_items(self.login_page.username)

    def exit_income_btn_clicked(self):
        self.income_page.close()
        self.income_page.reset_income()
        self.main_page.show()

    #############################################################################
    # cost

    def show_cost_form(self):
        if self.category_page.check_exist_category(self.login_page.username):
            self.main_page.hide()
            self.cost_page.cost_combo_items(self.login_page.username)
            self.cost_page.cost_type_items()
            self.cost_page.show()
        else:
            self.music.play_warn_music()
            self.message.show_warning(
                """You haven't added any category!
first add at least 1 category to open cost form."""
            )

    def exit_cost_btn_clicked(self):
        self.cost_page.close()
        self.cost_page.reset_cost()
        self.main_page.show()

    def cost_submit_clicked(self):
        valid_cost_page = self.cost_page.submit_cost_clicked()
        if valid_cost_page:
            self.cost_page.add_record_cost(
                self.login_page.username,
                self.cost_page.cost_amount.text(),
                self.cost_page.cost_date.text(),
                self.cost_page.cost_resource.currentText(),
                self.cost_page.cost_type_combo.currentText(),
                self.cost_page.description_cost.toPlainText(),
            )
            self.music.play_message_music()
            self.message.show_message("Your cost has been recorded.")
            self.cost_page.reset_cost()
            self.cost_page.cost_combo_items(self.login_page.username)

    #############################################################################
    # forgot

    def my_pass_btn_clicked(self):
        temp = self.forgot_page.show_password()
        if temp:
            self.forgot_page.close()
            self.login_page.show()

    def send_code_clicked(self):
        self.forgot_page.send_code()

    #############################################################################
    # welcome

    def welcome_signup_btn_clicked(self):
        self.signup_page.show()
        self.welcome_window.close()

    def welcome_login_btn_clicked(self):
        self.login_page.show()
        self.welcome_window.close()

    #############################################################################
    # login

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
            self.main_page.set_user_info(self.login_page.username)

    def toggle_echo_mode_show_pass(self, state):
        if state == Qt.Checked:
            self.login_page.password_login.setEchoMode(QLineEdit.Normal)
        else:
            self.login_page.password_login.setEchoMode(QLineEdit.Password)

    def signup_btn_login_clicked(self):
        self.login_page.close()
        self.signup_page.show()

    #############################################################################
    # Search

    def search_return_btn_clicked(self):
        self.search_page.close()
        self.search_page.reset_form()
        self.main_page.show()

    def show_search_page(self):
        self.main_page.hide()
        self.search_page.show()
        self.search_page.getusername(self.login_page.username)

    def price_checkbox_status(self):
        if self.search_page.price_checkbox.isChecked():
            self.search_page.show_lineedit()
        else:
            self.search_page.hide_lineedit()

    def search_btn_clicked(self):
        start_date, end_date = self.search_page.format_date_calender()
        lower_price, higher_price = self.search_page.ischecbox_price()
        if len(self.search_page.search_lineedit.text()) != 0:
            res = self.search_page.search_text(
                self.search_page.search_lineedit.text(),
                start_date,
                end_date,
                lower_price,
                higher_price,
            )
            if len(res) == 0:
                self.music.play_warn_music()
                self.message.show_warning(
                    f"We didn't find anything with word '{self.search_page.search_lineedit.text()}'"
                )
            else:
                self.music.play_message_music()
                self.message.show_results(res)
                self.search_page.price_high.setText("")
                self.search_page.price_low.setText("")
        else:
            self.music.play_warn_music()
            self.message.show_warning("Please Enter something to search!")
            return

    #############################################################################
    # Report
    def show_report_page(self):
        self.main_page.hide()
        self.report_page.yesterday_radio.setChecked(True)
        self.report_page.show()
        self.report_page.getusername(self.login_page.username)

    def get_report_btn_clicked(self):
        start_date, end_date = self.report_page.format_date_calender()
        lower_price, higher_price = self.report_page.ischecbox_price()
        item_type = self.report_page.ischecbox_type()
        source = self.report_page.ischecbox_resource()
        res = self.report_page.report_text(
            start_date, end_date, lower_price, higher_price, source, item_type
        )
        if len(res) == 0:
            self.music.play_warn_music()
            self.message.show_warning(f"We didn't find anything!")
        else:
            self.music.play_message_music()
            self.message.show_results(res)
            self.report_page.price_high.setText("")
            self.report_page.price_low.setText("")
            self.report_page.type_lineedit.setText("")
            self.report_page.type_lineedit.setText("")

    def show_chart_report(self):
        start_date, end_date = self.report_page.format_date_calender()
        lower_price, higher_price = self.report_page.ischecbox_price()
        item_type = self.report_page.ischecbox_type()
        source = self.report_page.ischecbox_resource()
        res = self.report_page.mat(
            start_date, end_date, lower_price, higher_price, source, item_type
        )
        self.matp.plot_pie_charts(res, self.login_page.username)

    def report_return_btn_clicked(self):
        self.report_page.close()
        self.report_page.reset_form()
        self.main_page.show()

    #############################################################################

    def run(self):
        self.welcome_window.show()

    def user_object_making(self):
        valid_inputs = self.signup_page.submit_signup_clicked()
        if valid_inputs:
            username = self.signup_page.username.text()
            fname = self.signup_page.fname_signup.text()
            lname = self.signup_page.lname_signup.text()
            phonenumber = self.signup_page.phone_signup.text()
            password = self.signup_page.Password_signup.text()
            email = self.signup_page.email_signup.text()
            city = self.signup_page.city_signup.text()
            date_birthday = self.signup_page.date_signup.text()
            self.music.play_message_music()
            self.message.show_message(
                "user successfully created.\nPlease Log in To Your Account"
            )
            self.database.add_new_user(
                fname,
                lname,
                phonenumber,
                username,
                password,
                city,
                email,
                date_birthday,
            )
            self.signup_page.reset_signup()
            self.signup_page.close()
            self.login_page.show()

    def return_signup_page(self):
        self.signup_page.close()
        self.signup_page.reset_signup()
        self.welcome_window.show()

    ########################################################################################
    # Setting

    def show_setting_form(self):
        self.main_page.hide()
        self.setting_page.show()

    def return_setting_clicked(self):
        self.setting_page.close()
        self.main_page.show()

    def show_edit_form(self):
        self.setting_page.hide()
        self.edit_form.show()

    def delete_trans(self):
        self.music.play_warn_music()
        flag = self.message.areyou_sure_message(
            "Are you sure you want to delete all of your transactions ?"
        )
        if flag:
            delete_flag = self.database.delete_user_data(
                ["UserIncome", "UserCost"], self.login_page.username
            )
            if not delete_flag:
                self.music.play_warn_music()
                self.message.show_warning(
                    "You Dont Have Any Data In Your Income Or Cost Info"
                )

    def delete_user(self):
        self.music.play_warn_music()
        flag = self.message.areyou_sure_message(
            "Are you sure you want to delete yourself ?"
        )
        if flag:
            self.database.delete_user_data(
                ["UserIncome", "UserCost", "UserInfo", "UserCategories"],
                self.login_page.username,
            )
            self.database.delete_all_csv_file(self.login_page.username)
            self.setting_page.close()
            self.main_page.close()
            self.login_page.show()

    def delete_income(self):
        self.music.play_warn_music()
        flag = self.message.areyou_sure_message(
            "Are you sure you want to delete all of your income transactions ?"
        )
        if flag:
            delete_flag = self.database.delete_user_data(
                ["UserIncome"], self.login_page.username
            )
            self.database.delete_csv_file(self.login_page.username, "UserIncome")
            if not delete_flag:
                self.music.play_warn_music()
                self.message.show_warning("You Dont Have Any Data In Your Income Info")

    def delete_cost(self):
        self.music.play_warn_music()
        flag = self.message.areyou_sure_message(
            "Are you sure you want to delete all of your cost transactions ?"
        )
        if flag:
            delete_flag = self.database.delete_user_data(
                ["UserCost"], self.login_page.username
            )
            self.database.delete_csv_file(self.login_page.username, "UserCost")
            if not delete_flag:
                self.music.play_warn_music()
                self.message.show_warning("You Dont Have Any Data In Your Cost Info ")

    def export_user_data(self):
        res = self.database.export_csv_file(self.login_page.username)
        if res:
            self.music.play_message_music()
            self.message.show_message("Your Data Has Been Saved To Csv File!")
        else:
            self.music.play_warn_music()
            self.message.show_warning("Cant Export Your Data To Csv!")

    #######################################################################################
    # edit form
    def return_edit_form(self):
        self.edit_form.reset_form()
        self.edit_form.hide()
        self.setting_page.show()

    def submit_edit_form_btn_clciked(self):
        flag = self.edit_form.sumbit_clicked(self.login_page.username)
        if flag:
            self.music.play_message_music()
            self.message.show_message("Your Informations Updated")
            self.edit_form.reset_form()
        else:
            self.music.play_warn_music()
            self.message.show_warning("Cant Update Anything")
            self.edit_form.reset_form()
