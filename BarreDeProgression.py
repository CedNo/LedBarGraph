import RPi.GPIO as GPIO
import time

#Ports GPIO
ledPins = [17, 18, 27, 22, 23, 24, 25, 16, 20, 12]

#Parametres initials
def setup():
        print('Starting...')
        GPIO.setmode(GPIO.BCM)
        for pin in ledPins:
                GPIO.setup(pin, GPIO.OUT)
                GPIO.output(pin, GPIO.HIGH)

#Boucle de la barre de progression
def loop():
    while True:
        for pin in ledPins:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(pin, GPIO.LOW)
        for pin in ledPins[10:0:-1]:
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(pin, GPIO.HIGH)

#Dispose des ressources
def destroy():
    for pin in ledPins:
        GPIO.output(pin, GPIO.HIGH)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterupt:
            destroy()
