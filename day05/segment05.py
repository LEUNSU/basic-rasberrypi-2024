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
                # 'number(state)' 함수를 50번 호출하여 현재 숫자를 디스플레이에 충분히 오래 표시
                # '_'는 루프 변수를 의미하지만, 여기서는 값이 사용되지 않기 때문에 관습적으로 표기
                state = (state + 1) % 10000
                for _ in range(50):
                        number(state)

except KeyboardInterrupt:
    GPIO.cleanup()
