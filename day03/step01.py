import RPi.GPIO as GPIO
import time

steps = [21 ,22, 23, 24]
GPIO.setmode(GPIO.BCM)

for stepPin in steps:
	GPIO.setup(stepPin, GPIO.OUT)
	GPIO.output(stepPin, 0)

try:
	seq = [
		(0, 0, 0, 1),
		(0, 0, 1, 1),
		(0, 0, 1, 0),
		(0, 1, 1, 0),
		(0, 1, 0, 0),
		(1, 1, 0, 0),
		(1, 0, 0, 0),
		(1, 0, 0, 1)]

	while True:
		for step in seq:
			GPIO.output(steps[0], step[0])
			GPIO.output(steps[1], step[1])
			GPIO.output(steps[2], step[2])
			GPIO.output(steps[3], step[3])
			time.sleep(0.01)

except KeyboardInterrupt:
	GPIO.cleanup()
