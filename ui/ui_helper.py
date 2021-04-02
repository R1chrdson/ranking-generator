from PyQt5.QtWidgets import QMainWindow, QSlider
from PyQt5.QtCore import Qt, pyqtSignal


class PageWindow(QMainWindow):
    gotoSignal = pyqtSignal(object, str)
    usedSignal = pyqtSignal(object)

    def goto(self, name):
        self.gotoSignal.emit(self, name)


def load_qss(path):
    with open(path) as qss_file:
        return qss_file.read()


class Slider(QSlider):
    def mousePressEvent(self, e):
        super().mousePressEvent(e)
        if e.button() == Qt.LeftButton:
            e.accept()
            x = e.pos().x()
            value = (self.maximum() - self.minimum()) * x / self.width() + self.minimum()
            self.setValue(round(value))
