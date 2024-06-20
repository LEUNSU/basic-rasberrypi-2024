import RPi.GPIO as GPIO
import time

led_pin = 20
piezoPin = 13
melody = [130, 147, 165, 175, 196, 220, 247, 262]

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(piezoPin, GPIO.OUT)

Buzz = GPIO.PWM(piezoPin, 440)

try:
    while True:
        a = input()

        if a == 'O':
            GPIO.output(led_pin, False)
        elif a == 'X':
            GPIO.output(led_pin, True)
        elif a.isdigit() and 1 <= int(a) <= 8:  
            index = int(a) - 1  
            Buzz.start(50)
            Buzz.ChangeFrequency(melody[index])
        elif a == 'Q':
        	Buzz.stop()

except KeyboardInterrupt:
	GPIO.cleanup()
