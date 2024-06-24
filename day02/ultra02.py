# 50cm이하로 거리가 측정되면 부저에 소리나게 하기
import RPi.GPIO as GPIO
import time

def measure():
	GPIO.output(triggerPin, True) # 10us동안 trigger 출력하여 초음파발생 준비
	time.sleep(0.00001)
	GPIO.output(triggerPin, False)
	start = time.time()				# 현재 시간 저장

	while GPIO.input(echoPin) == False: # echo가 없으면
		stop = time.time()								# 현재 시간을 start변수에 저장하고
	while GPIO.input(echoPin) == True:	# echo가 있으면
		stop = time.time()								# 현재 시간을 stop변수에 저장
	elasped = stop - start							# 걸린 시간을 구하고
	distance = (elasped * 19000) / 2		# 초음파 속도를 이용해서 거리 계산

	return distance											# 거리 반환


# 핀 설정
triggerPin = 13
echoPin = 26
piezoPin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(triggerPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(piezoPin, GPIO.OUT)

Buzz = GPIO.PWM(piezoPin, 440)

try:
	while True:
		distance = measure()
		print("Distance : %.2f cm" %distance)
		if distance <= 50:
			Buzz.start(50) # '50'은  듀티사이클
			delay = distance / 100
			time.sleep(delay)
			Buzz.stop()
			time.sleep(delay)
		else:
			Buzz.stop()
			time.sleep(0.1)
except KeyboardInterrupt:
	GPIO.cleanup()
