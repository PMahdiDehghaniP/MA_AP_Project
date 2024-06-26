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

        spacer = QSpacerItem(300, 10, QSizePolicy.Minimum,
                             QSizePolicy.Expanding)
        layout = msg.layout()
        layout.addItem(spacer, layout.rowCount(), 0, 5, layout.columnCount())
        msg.setFixedSize(1000, 300)
        msg.exec_()

    def show_results(self, result):
        msg = QMessageBox()
        msg.setText("Results")
        msg.setInformativeText(result)
        msg.setWindowTitle("Results")
        msg.setStandardButtons(QMessageBox.Ok)
        window_icon = QIcon(r"MessageBox\verify_window_icon.png")
        msg.setWindowIcon(window_icon)
        msg.setStyleSheet(
            """
        QMessageBox {
            background: qlineargradient(
                spread: pad, x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #005AA7,
                stop: 1 #FFFDE4
            );
            color: white;
        }
    """
        )
        spacer = QSpacerItem(300, 10, QSizePolicy.Minimum,
                             QSizePolicy.Expanding)
        layout = msg.layout()
        layout.addItem(spacer, layout.rowCount(), 0, 5, layout.columnCount())
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

        spacer = QSpacerItem(300, 10, QSizePolicy.Minimum,
                             QSizePolicy.Expanding)
        layout = msg.layout()
        layout.addItem(spacer, layout.rowCount(), 0, 5, layout.columnCount())

        msg.setFixedSize(1000, 300)
        msg.exec_()

    def show_password(self, message):
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

        spacer = QSpacerItem(300, 10, QSizePolicy.Minimum,
                             QSizePolicy.Expanding)
        layout = msg.layout()
        layout.addItem(spacer, layout.rowCount(), 0, 5, layout.columnCount())

        msg.setFixedSize(1000, 300)
        msg.exec_()

    def areyou_sure_message(self, message):
        msg = QMessageBox()
        pixmap = QPixmap(r"MessageBox\are_you_icon.png")
        msg.setIconPixmap(pixmap.scaled(64, 64))
        msg.setWindowIcon(QIcon(r"MessageBox\are_you_window_icon.png"))
        msg.setWindowTitle("Confirm")
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        reply = msg.exec_()
        if reply == QMessageBox.Yes:
            return True
        else:
            return False
