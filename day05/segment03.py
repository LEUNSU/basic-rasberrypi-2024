import RPi.GPIO as GPIO
import time

segments = (21, 22, 23, 24, 25, 26, 27)
digits = (12, 16, 18, 5)

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
		for j in range(7):
			GPIO.output(segments[j],num[[state][i]][j])
	GPIO.output(digits[i], GPIO.HIGH)
	time.sleep(0.1)

try:
	while True:
	number(1,2,3,4)
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
