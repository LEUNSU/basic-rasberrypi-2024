from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore
import sys
import RPi.GPIO as GPIO
import time
import adafruit_dht
import board

red_pin = 21
blue_pin = 20
piezoPin = 26
sensor_pin = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)
GPIO.setup(piezoPin, GPIO.OUT)
GPIO.setup(sensor_pin, GPIO.OUT)

Buzz = GPIO.PWM(piezoPin, 440)

dhtDevice = adafruit_dht.DHT11(board.D5)

log_num = 0

form_class = uic.loadUiType("./qt.ui") [0]
form_class2 = uic.loadUiType("./MyClock.ui") [0]

class WindowClass(QMainWindow, form_class):
        def __init__(self):
                super().__init__()
                self.setupUi(self)

		#LED
                self.Btn_1.clicked.connect(self.btn01)
                self.Btn_2.clicked.connect(self.btn02)

		#ALARM
                self.Btn_5.clicked.connect(self.btn05)
                self.Btn_6.clicked.connect(self.btn06)


		#Temperature,Humidity
                self.Btn_7.clicked.connect(self.btn07)
                self.Btn_8.clicked.connect(self.btn08)

	#LED
        def btn01(self):
                GPIO.output(red_pin, False)
                print("LED ON")
        def btn02(self):
                GPIO.output(red_pin, True)
                print("LED OFF")

	#ALARM
        def btn05(self):
                GPIO.output(blue_pin, True)
                Buzz.start(50)
                print("Alarm ON")

		# MyClock 위젯을 생성하고 표시
                self.clock = MyClock()
                self.clock.show()

        def btn06(self):
                Buzz.stop()
                GPIO.output(blue_pin, False)
                print("Alarm OFF")

	#Temperature,Humidity
        def btn07(self):
                global log_num
                temp = dhtDevice.temperature
                humid = dhtDevice.humidity
                print(f'{log_num} - Temp : {temp}C / Humid : {humid}%')
                log_num += 1

#        def btn08(self):
#                dhtDevice.exit()

class MyClock(QWidget, form_class2):
        def __init__(self):
                super().__init__()
                self.setupUi(self)
                self.setWindowTitle("시계")
                self.setFixedSize(250, 100)


                self.layout = QVBoxLayout()
                self.lcd = QLCDNumber()
                self.lcd.setSegmentStyle(QLCDNumber.Flat)
                self.lcd.setDigitCount(8)
                self.lcd.setFrameStyle(QFrame.NoFrame)
                self.layout.addWidget(self.lcd)
                self.setLayout(self.layout)

                self.timer = QtCore.QTimer()
                self.timer.timeout.connect(self.show_time)
                self.timer.start(1000)
                self.show_time()

        def show_time(self):
                current_time = QtCore.QTime.currentTime()
                self.currentTime = current_time.toString('hh:mm:ss')
                self.lcd.display(self.currentTime)

#class 

def closeEvent(self, event):
        GPIO.cleanup()
        event.accept()

if __name__ == "__main__":
        app = QApplication(sys.argv)
        myWindow = WindowClass()
        myWindow.show()
        app.exec_()
