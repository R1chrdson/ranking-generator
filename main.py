import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.resize(900, 600)
    window.show()
    sys.exit(app.exec_())
