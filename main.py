from PyQt5.QtWidgets import *
from connect.connector import Connector
app = QApplication([])

if __name__ == "__main__":
    connector = Connector()
    connector.run()
    app.exec_()
