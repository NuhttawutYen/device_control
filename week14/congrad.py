import sys, os
import sqlite3
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

DB_PATH = os.path.join(os.path.dirname(__file__), "congrad.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS check_in (
                id INTEGER PRIMARY KEY NOT NULL,
                is_student TEXT,
                time_in TEXT
            )
        """)
        conn.commit()
    finally:
        conn.close()
    

class Congratuletion(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("congrad.ui", self)  
        init_db()

    def msg(self, title, text, icon=QMessageBox.Information):
        QMessageBox(icon, title, text, parent=self).exec_()

    def loadData(self):
        try:
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute("""
                        SELECT
                        tb1.* FROM student as tb1""")
            rows = cur.fetchall()
        except Exception as e:
            return self.msg("โหลดข้อมูลไม่ได้", f"เกิดข้อผิดพลาด: {e}", QMessageBox.Critical)
        finally:
            conn.close()

        self.tableWidget.clear()
        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["รหัส","คำนำหน้า","ชื่อ","นามสกุล"])
        
        for r, row in enumerate(rows):
            for c, val in enumerate(row):
                self.tableWidget.setItem(r, c, QTableWidgetItem(str(val)))
                
        self.tableWidget.resizeColumnsToContents()
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Congratuletion()
    window.setWindowTitle("Congratuletion")
    window.show()
    sys.exit(app.exec_())
