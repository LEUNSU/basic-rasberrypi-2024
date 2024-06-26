import RPi.GPIO as GPIO
import time

switch = 13

segments = (21, 22, 23, 24, 25, 26, 27)

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
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

state = 0

def number(state):
	for i in range(7):
		GPIO.output(segments[i], num[number][i])

try:
    while True:
        if GPIO.input(switch) == GPIO.HIGH:
               state = (state + 1) % 10
               number(state)
               while GPIO.input(switch) == GPIO.HIGH:
                    time.sleep(0.1)
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
