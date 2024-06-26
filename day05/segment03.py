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
	GPIO.output(segment, GPIO.LOW)
for digit in digits:
    	GPIO.setup(digit, GPIO.OUT)
	GPIO.output(segment, GPIO.LOW)
def number(state):
	str_number = str(number).zfill(4)
	for i in range(4):
		for j in range(7):
			GPIO.output(segments[j],num[int(str_number[i])][j])
	GPIO.output(digits[i], GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(digits[i], GPIO.LOW)

state = 1234

number(state)

try:
	while True:
		number(state)
		time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
