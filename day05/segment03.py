import RPi.GPIO as GPIO
import time

segments = (21, 22, 23, 24, 25, 26, 27)
digits = (17, 18, 19, 20)

num = [
    (1,1,1,1,1,1,0),  # 0
    (0,1,1,0,0,0,0),  # 1
    (1,1,0,1,1,0,1),  # 2
    (1,1,1,1,0,0,1),  # 3
    (0,1,1,0,0,1,1),  # 4
    (1,0,1,1,0,1,1),  # 5
    (1,0,1,1,1,1,1),  # 6
    (1,1,1,0,0,0,0),  # 7
    (1,1,1,1,1,1,1),  # 8
    (1,1,1,1,0,1,1)   # 9
]

GPIO.setmode(GPIO.BCM)
for segment in segments:
	GPIO.setup(segment, GPIO.OUT)
for digit in digits:
	GPIO.setup(digit, GPIO.OUT)

def number(state):
	for i in range(4):
		digit_value = state % 10
		state //= 10
		for j in range(7):
			 GPIO.output(segments[j], num[digit_value][j])

		GPIO.output(digits[3-i], GPIO.LOW)
		time.sleep(0.001)
		GPIO.output(digits[3-i], GPIO.HIGH)

try:
	while True:
		number(1234)
except KeyboardInterrupt:
    GPIO.cleanup()
