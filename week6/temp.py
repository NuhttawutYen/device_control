import sys
import serial
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QFrame
)
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt, QTimer


ser = serial.Serial('COM3', 9600, timeout=1)

class SensorDisplay(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Temperature & Humidity Monitor")
        self.setFixedSize(600, 600)
        self.setStyleSheet("background-color: #f0f4f8;")

        # Layout หลัก
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 50, 50, 50)
        layout.setSpacing(30)

        # หัวข้อ
        self.title = QLabel("Sensor Data Monitor")
        self.title.setFont(QFont("Arial", 24, QFont.Bold))
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("color: #333;")

        # กรอบแสดงข้อมูล
        self.data_frame = QFrame()
        self.data_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 20px;
                padding: 30px;
                border: 2px solid #ccc;
            }
        """)
        frame_layout = QVBoxLayout()



# เริ่มต้นโปรแกรม
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SensorDisplay()
    window.show()
    sys.exit(app.exec_())