import RPi.GPIO as GPIO
import time

# 0~9까지의 1byte hex값
fndData = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x27, 0x7f, 0x6f]
fndSegs = [21, 22, 23, 24, 25, 26, 27] #a~g led pin
fndSels = [17, 18, 19, 20]

#GPIO 설정
GPIO.setmode(GPIO.BCM)
for fndSeg in fndSegs:
	GPIO.setup(fndSeg, GPIO.OUT)
	GPIO.output(fndSeg, 0)

for fndSel in fndSels:
	GPIO.setup(fndSel, GPIO.OUT)
	GPIO.output(fndSel, 1)

def fndOut():
	for i in range(0, 7):
#		GPIO.output(fndSegs[0], 0)
#		GPIO.output(fndSegs[1], 1)
#		GPIO.output(fndSegs[2], 1)
#		GPIO.output(fndSegs[3], 0)
		GPIO.output(fndSegs[i], fndDatas[Data] & (0x01 << i))

try:
	while True:
		for i in range(0, 1):
			GPIO.output(fndSels[i], 0) # fnd 선택
			for j in range(0, 10):
				fndOut()
				time.sleep(0.5)

except KeyboardInterrupt:
	GPIO.cleanup()
