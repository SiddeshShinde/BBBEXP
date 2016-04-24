import Adafruit_BBIO.GPIO as GPIO
import time
import math

#stepper pin mapping to BBB
pin1 = "P8_7"
pin2 = "P8_8"
pin3 = "P8_9"
pin4 = "P8_10"

x=0;
i=0;
#Setup mode for leds of particular mode
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)

#Sequence of the steper motor in shifted format
def sequence(x):
	if(x==1):#5
		GPIO.output(pin1, GPIO.LOW)
		GPIO.output(pin2, GPIO.HIGH)
		GPIO.output(pin3, GPIO.LOW)
		GPIO.output(pin4, GPIO.HIGH)
	elif(x==2):#6
		GPIO.output(pin1, GPIO.LOW)
		GPIO.output(pin2, GPIO.HIGH)
		GPIO.output(pin3, GPIO.HIGH)
		GPIO.output(pin4, GPIO.LOW)
	elif(x==3):#10
		GPIO.output(pin1, GPIO.HIGH)
		GPIO.output(pin2, GPIO.LOW)
		GPIO.output(pin3, GPIO.HIGH)
		GPIO.output(pin4, GPIO.LOW)
	elif(x==4):#9
		GPIO.output(pin1, GPIO.HIGH)
		GPIO.output(pin2, GPIO.LOW)
		GPIO.output(pin3, GPIO.LOW)
		GPIO.output(pin4, GPIO.HIGH)
	
	return;

while True:
	for i in range(1,5):
		sequence(i);
		time.sleep(0.5);
