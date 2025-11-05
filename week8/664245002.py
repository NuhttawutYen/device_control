import sys
import serial

from  PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout,QMessageBox

try :
  arduino = serial.Serial('COM3',9600, timeout=1)
except Exception as e:
  arduino = None
  print("เชื่อต่อไม่ได้: ",e)

class ServoControl(QWidget):
    def __init__(self):
      super().__init__()
      self.setWindowTitle("Servo Controller") #ชื่อโปรแกรมที่กำหนด
      self.setGeometry(200,200,300,150) #ขนาด

      #เปิด
      layout = QVBoxLayout()
      self.btn_15 = QPushButton("15")
      self.btn_15.clicked.connect(lambda:self.send_command("15"))
      layout.addWidget(self.btn_15)



      self.btn_30 = QPushButton("30")
      self.btn_30.clicked.connect(lambda:self.send_command("30"))
      layout.addWidget(self.btn_30)


      self.btn_45 = QPushButton("45")
      self.btn_45.clicked.connect(lambda:self.send_command("45"))
      layout.addWidget(self.btn_45)


      self.btn_90 = QPushButton("90")
      self.btn_90.clicked.connect(lambda:self.send_command("90"))
      layout.addWidget(self.btn_90)


      self.btn_125 = QPushButton("125")
      self.btn_125.clicked.connect(lambda:self.send_command("125"))
      layout.addWidget(self.btn_125)


      self.btn_135 = QPushButton("135")
      self.btn_135.clicked.connect(lambda:self.send_command("135"))
      layout.addWidget(self.btn_135)

      self.btn_150 = QPushButton("150")
      self.btn_150.clicked.connect(lambda:self.send_command("150"))
      layout.addWidget(self.btn_150)

      self.btn_stop = QPushButton("stop")
      self.btn_stop.clicked.connect(lambda:self.send_command("stop"))
      layout.addWidget(self.btn_stop)
      self.setLayout(layout)



    def send_command(self,command):
      if(arduino):
        arduino.write((command + '\n').encode())
      else:
        QMessageBox.critical(self, "Error","ไม่พบการเชือ่มต่อ Aruino")

#การสร้าง Gui output

if __name__== "__main__":
  app = QApplication(sys.argv)
  window = ServoControl()
  window.show()
  sys.exit(app.exec_())