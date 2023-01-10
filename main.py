from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import random
import time
import sys

def application():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("Простая программа")
    window.setGeometry(300, 250, 350, 200)
    while True:
        x = random.randint(0,350)
        y = random.randint(0,200)
        qp = QtGui.QPainter()
        qp.begin(window)
        qp.setPen(QtCore.Qt.red)
        qp.drawEllipse(e.pos().x(), e.pos().y(), 10, 10)
        time.sleep(1)
        window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    application()