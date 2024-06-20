import RPi.GPIO as GPIO
import time

switch = 6
red_pin = 21
green_pin = 25
blue_pin = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN)
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

state = 0

def change_color(state):
    if state == 0:
        GPIO.output(red_pin, False)
        GPIO.output(green_pin, True)
        GPIO.output(blue_pin, True)
    elif state == 1:
        GPIO.output(red_pin, True)
        GPIO.output(green_pin, False)
        GPIO.output(blue_pin, True)
    elif state == 2:
        GPIO.output(red_pin, True)
        GPIO.output(green_pin, True)
        GPIO.output(blue_pin, False)

try:
    while True:
        if GPIO.input(switch) == GPIO.HIGH:
            state = (state + 1) % 3
            change_color(state)
   			    # 스위치 디바운싱 처리 -> 스위치가 눌릴 때 접점에서 일어나는 진동 현상 방지. 스위치를 한 번 누르는 동안 여러 번 눌린 것으로 인식
            while GPIO.input(switch) == GPIO.HIGH:
                time.sleep(0.1)
        time.sleep(0.1)

except KeyboardInterrupt:
  GPIO.cleanup()
