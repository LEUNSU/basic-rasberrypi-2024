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
sensor_pin = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)
GPIO.setup(piezoPin, GPIO.OUT)
GPIO.setup(sensor_pin, GPIO.IN)

Buzz = GPIO.PWM(piezoPin, 440)

log_num = 0

form_class = uic.loadUiType("./qt.ui") [0]
form_class2 = uic.loadUiType("./MyClock.ui") [0]
form_class3 = uic.loadUiType("./SensorWidget.ui") [0]

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

                self.sensor_widget = None 

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
                self.sensor_widget = SensorWidget()
                self.sensor_widget.show()
                self.increment_log_num()

        def increment_log_num(self):
                global log_num
                log_num += 1
        
        def btn08(self):
                if self.sensor_widget is not None:
                        self.sensor_widget.close()
                        self.sensor_widget = None
                        self.show_sensor_widget()

        def show_sensor_widget(self):
                if self.sensor_widget is None:
                        self.sensor_widget = SensorWidget()
                        self.sensor_widget.show()
                        self.increment_log_num()
                
class MyClock(QWidget, form_class2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(250, 100)

        self.lcd = QLCDNumber(self)
        self.lcd.setGeometry(10, 10, 230, 50)
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        self.lcd.setDigitCount(8)
        self.lcd.setFrameStyle(QFrame.NoFrame)

        self.dial = QDial(self)
        self.dial.setGeometry(10, 70, 100, 100)
        self.dial.setMinimum(1)
        self.dial.setMaximum(60)

        self.label = QLabel("Set minutes: 1", self)
        self.label.setGeometry(120, 70, 120, 30)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)
        self.show_time()

        self.dial.valueChanged.connect(self.update_label)

    def show_time(self):
        current_time = QtCore.QTime.currentTime()
        self.currentTime = current_time.toString('hh:mm:ss')
        self.lcd.display(self.currentTime)

        if current_time.minute() == self.dial.value() and current_time.second() == 0:
            self.activate_alarm()

    def update_label(self, value):
        self.label.setText(f"Set minutes: {value}")

    def activate_alarm(self):
        GPIO.output(blue_pin, True)
        Buzz.start(50)
        print("Alarm ON")

    def closeEvent(self, event):
        Buzz.stop()
        GPIO.output(blue_pin, False)
        GPIO.cleanup()
        event.accept()


class SensorWidget(QWidget, form_class3):
        def __init__(self):
              super().__init__()
              self.setupUi(self)
              self.lcdTemp = self.findChild(QLCDNumber, 'lcdTemp')
              self.lcdHumid = self.findChild(QLCDNumber, 'lcdHumid')
              self.dhtDevice = adafruit_dht.DHT11(board.D13)
              self.update_timer = QtCore.QTimer(self)
              self.update_timer.timeout.connect(self.update_sensor_values)
              self.update_timer.start(2000)
              
        def update_sensor_values(self):
                try:
                        temp = self.dhtDevice.temperature
                        humid = self.dhtDevice.humidity
                        if temp is not None and humid is not None:
                                self.lcdTemp.display(temp)
                                self.lcdHumid.display(humid)
                                print(f'{log_num} - Temp : {temp}C / Humid : {humid}%')
                        else:
                                self.lcdTemp.display(0)
                                self.lcdHumid.display(0)
                except RuntimeError as ex:
                        print(ex.args[0])

        def closeEvent(self, event):
                self.update_timer.stop()
                self.dhtDevice = None
                event.accept()

if __name__ == "__main__":
        app = QApplication(sys.argv)
        myWindow = WindowClass()
        myWindow.show()
        app.exec_()
