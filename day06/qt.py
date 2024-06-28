from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import RPi.GPIO as GPIO
import time

led_pin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

form_class = uic.loadUiType("./qt.ui") [0]

class WindowClass(QMainWindow, form_class):
        def __init__(self):
                super().__init__()
                self.setupUi(self)
        
        self.btn01.clicked(self.btn01)
        self.btn02.clicked(self.btn02)

        def btn01(self):
                GPIO.output(led_pin, False)
                print("LED ON Button Clicked")

        def btn02(self):
                GPIO.output(led_pin, True)
                print("LED OFF Button Clicked")

def closeEvent(self, event):
        GPIO.cleanup()
        event.accept()

if __name__ == "__main__":
        app = QApplication(sys.argv)
        myWindow = WindowClass()
        myWindow.show()
        app.exec_()
