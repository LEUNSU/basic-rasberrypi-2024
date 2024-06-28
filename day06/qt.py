from PyQt5.QtWidgets import *
from PyQt5 import uic
#from picamera2 import PiCamera
import sys
import RPi.GPIO as GPIO
import time

red_pin = 21
blue_pin = 20

piezoPin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)
GPIO.setup(piezoPin, GPIO.OUT)

Buzz = GPIO.PWM(piezoPin, 440)

form_class = uic.loadUiType("./qt.ui") [0]

class WindowClass(QMainWindow, form_class):
        def __init__(self):
                super().__init__()
                self.setupUi(self)

		#picam2 = Picamera2()

		#LED
                self.Btn_1.clicked.connect(self.btn01)
                self.Btn_2.clicked.connect(self.btn02)

		#CAM


		#ALARM
                self.Btn_5.clicked.connect(self.btn05)
                self.Btn_6.clicked.connect(self.btn06)

	#LED
        def btn01(self):
                GPIO.output(red_pin, False)
                print("LED ON")
        def btn02(self):
                GPIO.output(red_pin, True)
                print("LED OFF")

	#CAM
	#def btn03(self):

	#def btn04(self):

	#ALARM
        def btn05(self):
		GPIO.output(blue_pin, True)
                Buzz.start(50)
                print("Alarm ON")
        def btn06(self):
                Buzz.stop()
                GPIO.output(blue_pin, False)
                print("Alarm OFF")

def closeEvent(self, event):
        GPIO.cleanup()
        event.accept()

if __name__ == "__main__":
        app = QApplication(sys.argv)
        myWindow = WindowClass()
        myWindow.show()
        app.exec_()
