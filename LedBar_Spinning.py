import time
import RPi.GPIO as GPIO

led_list = [17, 18, 27, 22, 23, 24, 25, 16, 20, 21]

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

for pin in led_list:
    GPIO.setup(pin,GPIO.OUT)

def LedSegOut(array):
    array=list(map(lambda n: not(n),array))
    GPIO.output(led_list, array)

def LedSegCycle():
    array=[0,0,0,0,0,0,0,0,0,1]
    while True:
        try:
            array = array[1:]+array[:1]
            LedSegOut(array)
            time.sleep(.05)
        except KeyboardInterrupt:
            GPIO.cleanup()
            sys.exit()

def LedSegPerc(n):
    thresholds=[100,90,80,70,60,50,40,30,20,10]
    array=list(map(lambda x: (1,0)[x>n],thresholds))
    LedSegOut(array)

while True:
    try:
        #LedSegOut([0,0,0,0,0,1,1,1,1,1])
        LedSegCycle()
        # LedSegPerc(81)
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()
