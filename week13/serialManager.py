import time
import serial

class SerialManager:
    def __init__(self, port='COM5', baud=9600):
        self.port = port
        self.baud = baud
        self.ser = None
        self._connect()

    def _connect(self):
        try:
            self.ser = serial.Serial(self.port, self.baud, timeout=1)
            time.sleep(2) 
            print(f"[Serial] Connected to {self.port} @ {self.baud}")
        except Exception as e:
            print(f"[Serial] Could not open {self.port} : {e}")
            self.ser = None

    def is_open(self):
        return self.ser is not None and self.ser.is_open

    def send_angle(self, angle: int):
        msg = f"{angle}\n".encode('utf-8')
        try:
            if not self.is_open():
                self._connect()
            if self.is_open():
                self.ser.write(msg)
                print(f"[Serial] Sent: {angle}")
        except Exception as e:
            print(f"[Serial] Write failed: {e}")

    def close(self):
        try:
            if self.ser and self.ser.is_open:
                self.ser.close()
                print("[Serial] Closed")
        except Exception:
            pass 
