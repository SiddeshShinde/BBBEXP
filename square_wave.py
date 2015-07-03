import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time
pwm_pin = "P8_13"          #Square will be generated on this pin

PWM.start(pwm_pin, 50)    #Duty_Cycle from 0 to 100
time.sleep(60);           #This will wait for 1 minute
PWM.stop(pwm_pin)         #The Square wave will stop here 

