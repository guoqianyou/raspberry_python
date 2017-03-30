from time import sleep

from RPi import GPIO

try:
    point = 40
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(point, GPIO.OUT)
    # while True:
    #     GPIO.output(point, GPIO.HIGH)
    #     sleep(2)
    #     print("--------------")
    #     GPIO.output(point, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()

