import RPi.GPIO as GPIO
import time
# pin naming convention 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# set pin 17 as an output pin
GPIO.setup(17, GPIO.OUT)
# switch on pin 17
GPIO.output(17, True)
time.sleep(0.1)
# switch off pin 17
GPIO.output(17, False)
time.sleep(0.1)
# close/exit gpio to avoid future warnings
GPIO.cleanup()
# update the log with time garage was opened
with open('garage_log.txt', 'a') as f:
    f.write('\n' + time.ctime())
# let script time out so button doesnt get spammed
time.sleep(5)
