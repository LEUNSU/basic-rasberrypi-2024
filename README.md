# basic-rasberrypi-2024
IoT 개발자 라즈베리파이 학습 리포지토리

- Python
- GPIO 설정함수
    - GPIO.setmode(GPIO.BOARD) - wPi
    - GPIO.setmode(GPIO.BCM) - BCM
    - GPIO.setup(channel, GPIO.mode) 
        - channel : 핀번호, mode : IN/OUT
    - GPIO.cleanup()
- GPIO 출력함수
    - GPIO.output(channel, state)
        - channel : 핀번호, state : HIGH/LOW or 1/0 or True/False
- GPIO 입력함수
    - GPIO.input(channel)
        - channel : 핀번호, 반환값 : H/L or 1/0 or T/F
- 시간지연함수
    - time.sleep(secs)