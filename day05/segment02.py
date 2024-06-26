 # 스위치 누르면 0~9까지의 숫자가 증가하며 순환하도록 만들기
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
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

state = 0

def number(state):
	for i in range(7):
		GPIO.output(segments[i], num[state][i]) # 각 세그먼트에 대해 ON/OFF 설정

try:
    while True:
        if GPIO.input(switch) == GPIO.HIGH:
               state = (state + 1) % 10  # 숫자를 1 증가시키고 9에서 다시 0으로 순환
               number(state)
               while GPIO.input(switch) == GPIO.HIGH:
                    time.sleep(0.1)
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
