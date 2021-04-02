from ui.ui_helper import PageWindow, Slider
from PyQt5 import QtCore, QtWidgets

class MainPage(PageWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle('Ranking Generator')

        self.slider_label = QtWidgets.QLabel(self)
        self.slider_label.setGeometry(QtCore.QRect(50, 20, 829, 16))
        self.slider_label.setText('Specify number of alternatives')

        self.slider = Slider(self)
        self.slider.setGeometry(QtCore.QRect(50, 50, 411, 22))
        self.slider.setMinimum(2)
        self.slider.setMaximum(10)
        self.slider.setOrientation(QtCore.Qt.Horizontal)

        self.slider_value = QtWidgets.QLabel(self)
        self.slider_value.setText(str(self.slider.value()))
        self.slider_value.setGeometry(QtCore.QRect(490, 50, 55, 16))

        self.slider.valueChanged.connect(self.change_slider_value)

    def change_slider_value(self, value):
        self.slider_value.setText(str(value))
