from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal


class PageWindow(QMainWindow):
    gotoSignal = pyqtSignal(object, str)
    usedSignal = pyqtSignal(object)

    def goto(self, name):
        self.gotoSignal.emit(self, name)


def load_qss(path):
    with open(path) as qss_file:
        return qss_file.read()
