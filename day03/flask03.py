	# URL접속을 /led/on,	/let/off로 접속하면 led를 on, off 하는 웹 페이지 만들기
from flask import Flask
import RPi.GPIO as GPIO

led_pin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

app = Flask(__name__)

@app.route('/')
def hello():
    return "LED Control!"

@app.route("/led/on")
def led_on():
	GPIO.output(led_pin, False)
	return "<h1>LED is now ON</h1>"

@app.route("/led/off")
def led_off():
	GPIO.output(led_pin, True)
	return "<h1>LED is now OFF</h1>"

if __name__ == '__main__':
	try:
		while True:
			app.run(host='0.0.0.0', port="10011", debug=True)

	except KeyboardInterrupt:
		GPIO.cleanup()
