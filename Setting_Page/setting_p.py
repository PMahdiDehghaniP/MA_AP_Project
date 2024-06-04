from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QTimer, Qt
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class Setting_Page(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"Setting_Page\mainwindow.ui", self)
        self.setFixedSize(872, 465)
        self.setWindowIcon(QIcon(r"Setting_Page\setting_icon.png"))
        self.setWindowTitle("Setting")
        self.style()

    def style(self):
        self.btn_style = """
        QPushButton{
            background: qlineargradient(
            spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
            stop: 0 #74ebd5,
            stop: 1 #ACB6E5
            );
            border-radius:5px;
            border:0.01px solid grey;
            
        }
        QPushButton:hover{
            background: qlineargradient(
            spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
            stop: 0 #fe8c00,
            stop: 1 #f83600
            );
            color:#ffffff
        }
        """
        self.setStyleSheet(
            """
            background: qlineargradient(
            spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
            stop: 0 #EB3349,
            stop: 1 #F45C43
            );
            """
        )
        self.edit_profile_btn.setCursor(Qt.PointingHandCursor)
        self.delete_all_transaction.setCursor(Qt.PointingHandCursor)
        self.delete_user.setCursor(Qt.PointingHandCursor)
        self.return_setting_btn.setCursor(Qt.PointingHandCursor)
        self.delete_income_transaction.setCursor(Qt.PointingHandCursor)
        self.delete_cost_transaction.setCursor(Qt.PointingHandCursor)
        self.export_csv_btn.setCursor(Qt.PointingHandCursor)
        self.bg_off_radio.setCursor(Qt.PointingHandCursor)
        self.bg_on_radio.setCursor(Qt.PointingHandCursor)
        self.btn_radio_off.setCursor(Qt.PointingHandCursor)
        self.btn_radio_on.setCursor(Qt.PointingHandCursor)
        self.msg_radio_off.setCursor(Qt.PointingHandCursor)
        self.msg_radio_on.setCursor(Qt.PointingHandCursor)
        self.setting_label.setStyleSheet("background:none;")
        self.backgroundsound_label.setStyleSheet("background:none;")
        self.buttonsound_label.setStyleSheet("background:none;")
        self.msg_sound_label.setStyleSheet("background:none;")
        self.edit_profile_btn.setStyleSheet(self.btn_style)
        self.delete_all_transaction.setStyleSheet(self.btn_style)
        self.delete_user.setStyleSheet(self.btn_style)
        self.delete_income_transaction.setStyleSheet(self.btn_style)
        self.delete_cost_transaction.setStyleSheet(self.btn_style)
        self.return_setting_btn.setStyleSheet(self.btn_style)
        self.export_csv_btn.setStyleSheet(self.btn_style)
