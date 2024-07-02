from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from MessageBox.messagebox import Message_Box
from Sound.back_sound import Sound
from PyQt5 import uic
import smtplib
music = Sound()
Message = Message_Box()


class Opinion_PageV(QMainWindow):
    def init(self):
        super().init()
        uic.loadUi(r"Opinion_Page\mainwindow.ui", self)
        self.setFixedSize(551, 496)
        self.setWindowTitle("Send Feedback")
        self.setWindowIcon(QIcon(r"Opinion_Page\icon.png"))
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
            """
            background: qlineargradient(
            spread:pad, x1:0, y1:0, x2:1, y2:0, 
            stop:0 #654ea3, 
            stop:1 #f2fcfe
        );"""
        )
        self.style()

    def style(self):
        self.returnbtn.setStyleSheet(self.btn_style)
        self.returnbtn.setCursor(Qt.PointingHandCursor)
        self.submitbtn.setStyleSheet(self.btn_style)
        self.submitbtn.setCursor(Qt.PointingHandCursor)
        self.title.setStyleSheet("background:none;")
        self.feedbackbox.setStyleSheet("background:none;")

    def send_code(self, username):
        comment = self.feedbackbox.Text()
        my_email = "mahdi14dehghani@gmail.com"
        password = "yaxa icnh gtuf cxeg"
        smtp_port = 587
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            message = f"Message From {username}\nText:{comment}"
            connection.login(user=my_email, password=password)
            connection.sendmail(my_email, my_email, message)
            music.play_message_music()
            Message.show_message(
                "Your Feedback Has Been Sent To Our Admin ThankYou")
