import RPi.GPIO as GPIO
import time

red_pin = 21
green_pin = 25
blue_pin = 16

#GPIO를 BCM모드로 설정
GPIO.setmode(GPIO.BCM)
#GPIO핀 설정 (입력/출력)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)


try:
	while True:
		GPIO.output(red_pin, False)
		GPIO.output(green_pin, True)
		GPIO.output(blue_pin, True)
		time.sleep(1)
		GPIO.output(red_pin, True)
		GPIO.output(green_pin, False)
		GPIO.output(blue_pin, True)
		time.sleep(1)
		GPIO.output(red_pin, True)
		GPIO.output(green_pin, True)
		GPIO.output(blue_pin, True)00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
		time.sleep(1)


except KeyboardInterrupt:	#Ctrl + c
	GPIO.cleanup()
