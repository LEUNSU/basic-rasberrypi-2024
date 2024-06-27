# 0~9999까지의 숫자가 1씩 증가하면 순환하도록 만들기
import RPi.GPIO as GPIO
import time

# 0~9까지의 1byte hex값
fndData = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x27, 0x7f, 0x6f]
fndSegs = [21, 22, 23, 24, 25, 26, 27] #a~g led pin
fndSels = [20, 19, 18, 17]

#GPIO 설정
GPIO.setmode(GPIO.BCM)
for fndSeg in fndSegs:
	GPIO.setup(fndSeg, GPIO.OUT)
	GPIO.output(fndSeg, 0)

for fndSel in fndSels:
	GPIO.setup(fndSel, GPIO.OUT)
	GPIO.output(fndSel, 1)

def fndOut(data, sel): 	# 표현할 숫자를 입력으로 받아 segment에 표시하는 함수
	for h in range(0, 50):
		for i in range(0, 7):	# a~f까지 on되는 led를 켠다
			GPIO.output(fndSegs[i], fndData[data] & (0x01 << i))
			for j in range(0, 4):	# 표시할 자리수의 fnd만 on
				if j == sel:
					GPIO.output(fndSels[j], 0)
				else :
					GPIO.output(fndSels[j], 1)

count = 0

try:
	while True:
		count += 1

		if count > 9999: # 9999 다음에 다시 0으로 순환
			count = 0

		d1000 = count / 1000
		d100 = count % 1000 / 100
		d10 = count % 100 / 10
		d1 = count % 10

		d = [d1, d10, d100, d1000] # fnd 선택 for문

		for i in range(3, -1, -1):
			fndOut(int(d[i]), i) # byte 표현 함수 호출
			time.sleep(0.001)

except KeyboardInterrupt:
	GPIO.cleanup()
