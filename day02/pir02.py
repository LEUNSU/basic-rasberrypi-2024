import RPi.GPIO as GPIO
import time

pir_pin = 24
led_pin = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(led_pin, GPIO.OUT)

try:
	while True:
		if GPIO.input(pir_pin) == True:
			GPIO.output(led_pin, False)
			print("Detacted")
			time.sleep(0.3)
		else:
			GPIO.output(led_pin, True)
			time.sleep(0.3)
except KeyboardInterrupt:
    GPIO.cleanup()

