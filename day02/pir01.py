#pir
import RPi.GPIO as GPIO
import time

pirpin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(pirpin, GPIO.IN)

try:
	while True:
		if GPIO.input(pirpin) == True:
			print("Detected")
			time.sleep(0.5)

except KeyboardInterrupt:
	GPIO.cleanup()
