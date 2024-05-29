from PyQt5.QtCore import QTimer, QTime


class Timer_Calc(QTime):
    def __init__(self):
        super().__init__()
        self.hours = ""
        self.minutes = ""
        self.seconds = ""

    def current_time(self):
        return QTime.currentTime()

    def Calculation_until_present(self, time):
        current_time = QTime.currentTime()
        spent_time = time.secsTo(current_time)
        self.hours, remainder = divmod(spent_time, 3600)
        self.minutes, self.seconds = divmod(remainder, 60)
