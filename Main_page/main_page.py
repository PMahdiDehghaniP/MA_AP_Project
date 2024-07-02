from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Timer.timer import Timer_Calc
from PyQt5 import uic

timer_main = Timer_Calc()


class Main_Page(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"Main_page\mainwindow.ui", self)
        self.setWindowTitle("Main Page")
        self.setWindowIcon(QIcon(r"Main_page\main_icon.png"))
        self.style()
        self.first_time_login = ""
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)
        self.show_time()

    def style(self):
        self.setFixedSize(444, 621)
        self.time_label.setStyleSheet("background : none ;")
        self.welcome_text.setStyleSheet("""background : none ;""")
        self.btn_style = """
            QPushButton{
                border-radius:5px;
                border :1px solid #ffffff;
                background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #2980B9,
                stop: 1 #6DD5FA
            );
            }
            QPushButton:hover{
                color : yellow;
                background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #ee0979,
                stop: 1 #ff6a00);
            }"""
        self.setStyleSheet(
            """ background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #a8ff78,
                stop: 1 #78ffd6
            );"""
        )
        self.record_income_btn.setCursor(Qt.PointingHandCursor)
        self.record_income_btn.setStyleSheet(self.btn_style)
        self.record_cost_btn.setCursor(Qt.PointingHandCursor)
        self.record_cost_btn.setStyleSheet(self.btn_style)
        self.category_btn.setCursor(Qt.PointingHandCursor)
        self.category_btn.setStyleSheet(self.btn_style)
        self.search_btn.setCursor(Qt.PointingHandCursor)
        self.search_btn.setStyleSheet(self.btn_style)
        self.report_btn.setCursor(Qt.PointingHandCursor)
        self.report_btn.setStyleSheet(self.btn_style)
        self.setting_btn.setCursor(Qt.PointingHandCursor)
        self.setting_btn.setStyleSheet(self.btn_style)
        self.record_income_btn.setCursor(Qt.PointingHandCursor)
        self.record_income_btn.setStyleSheet(self.btn_style)
        self.exit_mainpage_btn.setCursor(Qt.PointingHandCursor)
        self.exit_mainpage_btn.setStyleSheet(self.btn_style)
        self.feedback_btn.setStyleSheet(self.btn_style)
        self.feedback_btn.setCursor(Qt.PointingHandCursor)
        self.aboutapp_btn.setStyleSheet(self.btn_style)
        self.aboutapp_btn.setCursor(Qt.PointingHandCursor)

    def set_user_info(self, emuser):
        self.userfullname.setText(f"User : {emuser}")

    def show_time(self):
        current_time = QTime.currentTime()
        time_display = current_time.toString("HH:mm:ss")
        self.time_label.setText(time_display)

    def set_first_login_time(self):
        self.first_time_login = timer_main.current_time()
