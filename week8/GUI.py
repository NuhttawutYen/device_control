import sys
import serial
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox

try:
    arduino = serial.Serial('COM5', 9600, timeout=1)
except Exception as e:
    arduino = None
    print("เชื่อมต่อไม่ได้:", e)

class ArduinoControl(QWidget):
    while (serial) {
    char select_mode = Serial.read();
    user_input =  select_mode;

  if (user_input == '0') {
    Serial.println("Servo Motor => 15");
    myservo.write(90);
    delay(1000);
  }
  else if (user_input == '1') {
    Serial.println("Servo Motor => 30");
    myservo.write(45);
    delay(1000);
  }
  else if (user_input == '3'){
    Serial.println("Servo Motor => 45");
    myservo.write(0);
    delay(1000);
  }
  else if (user_input == '4'){
    Serial.println("Servo Motor => ");
    myservo.write(180);
    delay(1000);
    }
  }