# basic-rasberrypi-2024
IoT 개발자 라즈베리파이 학습 리포지토리

# 1일차
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

# 2일차
- 가상환경 설치 : python -m venv env
- 가상환경 접속 방법 : source ./env/bin/activate
- 가상환경 종료 방법 : deactivate
-  pip install RPi.GPIO

- sudo git clone https://github.com/WiringPi/WiringPi
- WiringPi > sudo ./build > gpio -v > gpio readall

## 3일차
- NC (Normally Close): 평상시에 닫혀있다는 뜻으로, 릴레이에 전류가 흐르면 Open 되므로 평상시에 전원을 on 상태로 유지하다가 신호를 주어 off 할 때 사용
- NO (Normally Open): 반대로 평상시에 열려있다는 뜻으로, 릴레이에 전류가 흐르면 Close 되므로 평상시에 전원을 off 상태로 유지하다가 신호를 주어 on 할 때 사용
- COM (Common port): 공통 단자로 전력 또는 외부기기의 한쪽 선을 항상 연결해야 하는 단자