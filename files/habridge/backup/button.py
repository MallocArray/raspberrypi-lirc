import RPi.GPIO as GPIO
import time
import sys


if sys.argv[1] == 'light':
    BCM = 27
elif sys.argv[1] == 'fanoff':
    BCM = 18
elif sys.argv[1] == 'fanhigh':
    BCM = 23
elif sys.argv[1] == 'fanlow':
    BCM = 24
elif sys.argv[1] == 'fanmed':
    BCM = 22
elif sys.argv[1] == 'toplight':
    BCM = 25
elif 1 == 1:
    BCM = int(sys.argv[1])

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(BCM,GPIO.OUT)
print("Using BCM pin " + str(BCM))
print("Button on")
GPIO.output(BCM,GPIO.HIGH)
time.sleep(0.25)
print("Button off")
GPIO.output(BCM,GPIO.LOW)
