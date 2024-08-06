from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore
import sys
import RPi.GPIO as GPIO
import time
import adafruit_dht
import board

# GPIO Pin Definitions
red_pin = 21
blue_pin = 20
piezoPin = 26
sensor_pin = 22

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)
GPIO.setup(piezoPin, GPIO.OUT)
GPIO.setup(sensor_pin, GPIO.IN)

# PWM Initialization
Buzz = GPIO.PWM(piezoPin, 440)
red_pwm = GPIO.PWM(red_pin, 1000)  # PWM for red LED
red_pwm.start(0)  # Initial duty cycle

# Global Log Number
log_num = 0

# Load UI Files
form_class = uic.loadUiType("./qt.ui")[0]
form_class2 = uic.loadUiType("./MyClock.ui")[0]
form_class3 = uic.loadUiType("./SensorWidget.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Initial LED State
        self.set_initial_led_state()

        # LED Control
        self.Btn_1.clicked.connect(self.turn_on_red_led)
        self.Btn_2.clicked.connect(self.turn_off_red_led)
        self.horizontalSlider.valueChanged.connect(self.change_red_led_brightness)

        # Alarm Control
        self.Btn_5.clicked.connect(self.show_clock_widget)
        self.Btn_6.clicked.connect(self.turn_off_alarm)

        # Temperature and Humidity Control
        self.Btn_7.clicked.connect(self.show_sensor_widget)
        self.Btn_8.clicked.connect(self.close_sensor_widget)

        self.sensor_widget = None
        self.clock_widget = None 

    def set_initial_led_state(self):
        GPIO.output(red_pin, False)  # Red LED off initially
        GPIO.output(blue_pin, False)  # Blue LED off initially

    # LED Control
    def turn_on_red_led(self):
        red_pwm.ChangeDutyCycle(100)  # Maximum brightness
        print("Red LED ON")

    def turn_off_red_led(self):
        red_pwm.ChangeDutyCycle(0)  # LED off
        print("Red LED OFF")

    def change_red_led_brightness(self, value):
        reversed_value = 100 - value  # Reverse the slider value
        red_pwm.ChangeDutyCycle(reversed_value)
        print(f"Red LED Brightness: {value} (Reversed: {reversed_value})")

    # Alarm Control
    def show_clock_widget(self):
        if self.clock_widget is None:
            self.clock_widget = MyClock()
            self.clock_widget.show()
        GPIO.setup(sensor_pin, GPIO.IN)

    def turn_off_alarm(self):
        Buzz.stop()
        GPIO.output(blue_pin, False)  # Turn off blue LED
        print("Alarm OFF")
        QtCore.QTimer.singleShot(2000, self.reset_led_state)  # Restore LED state after 2 seconds

    def reset_led_state(self):
        self.set_initial_led_state()

    # Temperature and Humidity Control
    def show_sensor_widget(self):
        if self.sensor_widget is None:
            self.sensor_widget = SensorWidget()
            self.sensor_widget.show()
            self.increment_log_num()

    def close_sensor_widget(self):
        if self.sensor_widget is not None:
            self.sensor_widget.update_timer.stop()
            self.sensor_widget.close()
            self.sensor_widget = None
            GPIO.cleanup(sensor_pin)

    def increment_log_num(self):
        global log_num
        log_num += 1

class MyClock(QWidget, form_class2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(400, 500)
        
        self.CurrLcd = self.findChild(QLCDNumber, 'CurrLcd')
        self.dial = self.findChild(QDial, 'dial')
        self.MinLabel = self.findChild(QLabel, 'MinLabel')
        self.timeEdit = self.findChild(QTimeEdit, 'timeEdit')

        self.dial.setMinimum(1)
        self.dial.setMaximum(60)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)
        self.show_time()

        self.dial.valueChanged.connect(self.update_label)
        self.timeEdit.timeChanged.connect(self.update_timeedit)

    def show_time(self):
        current_time = QtCore.QTime.currentTime()
        self.currentTime = current_time.toString('HH:mm:ss')

        if self.CurrLcd is not None: 
            self.CurrLcd.display(self.currentTime)
            
        self.check_alarm()

    def update_label(self, value):
        self.MinLabel.setText(f"{value}")
        self.update_timeedit()

    def update_timeedit(self):
        dial_value = self.dial.value()
        current_time = QtCore.QTime.currentTime()
        alarm_time = current_time.addSecs(dial_value * 60)
        self.timeEdit.setTime(alarm_time)

    def check_alarm(self):
        current_time = QtCore.QTime.currentTime()
        alarm_time = self.timeEdit.time()
        
        if current_time.toString('HH:mm:ss') == alarm_time.toString('HH:mm:ss'):
            GPIO.output(blue_pin, True)  # Turn on blue LED
            Buzz.start(50)  # Start buzzer
            print("Alarm ON")

    def closeEvent(self, event):
        Buzz.stop()
        GPIO.output(blue_pin, False)  # Ensure blue LED is turned off
        GPIO.cleanup()
        event.accept()
        print("Alarm OFF")

class SensorWidget(QWidget, form_class3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        GPIO.setup(sensor_pin, GPIO.IN)
        self.lcdTemp = self.findChild(QLCDNumber, 'lcdTemp')
        self.lcdHumid = self.findChild(QLCDNumber, 'lcdHumid')
        self.dhtDevice = adafruit_dht.DHT11(board.D22)
        self.update_timer = QtCore.QTimer(self)
        self.update_timer.timeout.connect(self.update_sensor_values)
        self.update_timer.start(2000)
        
        GPIO.setup(sensor_pin, GPIO.IN)

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
        self.dhtDevice.exit()
        event.accept()  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
