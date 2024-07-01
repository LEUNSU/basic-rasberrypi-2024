# basic-rasberrypi-2024
IoT 개발자 라즈베리파이 학습 리포지토리

# 1일차
- Python
    - 들여쓰기 무조건 'Tab', Spacebar X
    - 복사 : Ctrl + 6
    - 범위 복사 : 범위지정시작(Ctrl + 6), 범위지정끝(Alt + 6)
    - 붙여넣기 : Ctrl + u

- GPIO
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

- LED 모듈
    - VCC -> 5V 연결
    - RGB -> GPIO 핀 설정 연결

- 스위치 모듈

- 피에조 부저 모듈

# 2일차
- 가상환경 
    - 설치 
        - python -m venv env (독립적인 환경이 필요할 때)
        - python -m venv env --system-site-packages env (전역 패키지를 재사용하고 싶을 때)
    - 접속 방법 : source ./env/bin/activate
    - 종료 방법 : deactivate
- pip install RPi.GPIO
- sudo git clone https://github.com/WiringPi/WiringPi : gpio readall을 사용하기 위해 설치하는 방법
- WiringPi > sudo ./build > gpio -v > gpio readall

- 적외선 PIR(인체감지)센서

- 초음파 모듈

## 3일차
- 릴레이 모듈
    - S -> GPIO 핀 설정
    - (+) -> 5V 연결 (스위치 전류 공급)
    - (-) -> GND 연결
    - NC (Normally Close): 평상시에 닫혀있다는 뜻으로, 릴레이에 전류가 흐르면 Open 되므로 평상시에 전원을 on 상태로 유지하다가 신호를 주어 off 할 때 사용 
    - NO (Normally Open): 반대로 평상시에 열려있다는 뜻으로, 릴레이에 전류가 흐르면 Close 되므로 평상시에 전원을 off 상태로 유지하다가 신호를 주어 on 할 때 사용 -> GND 연결
    - COM (Common port): 공통 단자로 전력 또는 외부기기의 한쪽 선을 항상 연결해야 하는 단자 -> 5V 연결 (모듈에 전류 공급)

- GET방식
    - 클라이언트가 서버에 요청을 할 때, 클라이언트의 데이터를 URL뒤에 붙여서 전송 
    - URL 뒤에 "?" 마크를 통해 URL의 끝을 알리면서, 데이터 표현의 시작점을 알림. 데이터는 key와 value쌍으로 넣어야 함
    
    ``` 
    http://192.168.5.3:10011/?이름=이은수&주소=서울 
    ```
## 4일차
- FND 모듈

    ![FND 7세그먼트](https://raw.githubusercontent.com/LEUNSU/basic-rasberrypi-2024/main/images/001.png)

## 5일차

## 6일차
- 라즈베리파이 linenumber : Alt + Shift + 3