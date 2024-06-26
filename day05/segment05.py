# 0~9999까지의 숫자가 1씩 증가하며 순환하도록 만들기
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

state = 0

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
                state = (state + 1) % 10000
                for _ in range(50):
                        number(state)
                # state = (state + 1) % 10000
except KeyboardInterrupt:
    GPIO.cleanup()
