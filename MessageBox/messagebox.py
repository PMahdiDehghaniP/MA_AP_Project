from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon


class Message_Box(QMainWindow):
    def __init__(self):
        pass

    def show_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Done!")
        msg.setInformativeText(message)
        msg.setWindowTitle("Message")
        msg.setStandardButtons(QMessageBox.Ok)

        window_icon = QIcon(r"MessageBox\verify_window_icon.png")
        msg.setWindowIcon(window_icon)

        pixmap = QPixmap(r"MessageBox\verify_icon.png")
        msg.setIconPixmap(pixmap.scaled(64, 64))

        spacer = QSpacerItem(300, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout = msg.layout()
        layout.addItem(spacer, layout.rowCount(), 0, 5, layout.columnCount())
        msg.setFixedSize(1000, 300)
        msg.exec_()

    def show_warning(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Warning")
        msg.setInformativeText(message)
        msg.setWindowTitle("Warning")
        msg.setStandardButtons(QMessageBox.Ok)

        warning_window_icon = QIcon(r"MessageBox\warning_window_icon.png")
        msg.setWindowIcon(warning_window_icon)

        pixmap = QPixmap(r"MessageBox\warning_icon.png")
        msg.setIconPixmap(pixmap.scaled(64, 64))

        spacer = QSpacerItem(300, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout = msg.layout()
        layout.addItem(spacer, layout.rowCount(), 0, 5, layout.columnCount())

        msg.setFixedSize(1000, 300)
        msg.exec_()
    def show_password(self,message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Password")
        msg.setInformativeText(message)
        msg.setWindowTitle("Show Password")
        msg.setStandardButtons(QMessageBox.Ok)

        Password_window_icon = QIcon(r"MessageBox\pass_window_icon.png")
        msg.setWindowIcon(Password_window_icon)

        pixmap = QPixmap(r"MessageBox\pass_icon.png")
        msg.setIconPixmap(pixmap.scaled(64, 64))

        spacer = QSpacerItem(300, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout = msg.layout()
        layout.addItem(spacer, layout.rowCount(), 0, 5, layout.columnCount())

        msg.setFixedSize(1000, 300)
        msg.exec_()
