import sys
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from serial_manager
import SerialManager
from workers import FaceScanWorker 

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Main_window.ui", self) 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
