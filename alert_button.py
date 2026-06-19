import time

import RPi.GPIO as GPIO


BUTTON_PIN = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

button_pressed = False

try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.HIGH and not button_pressed:
            print("Someone pressed the alert button!")
            button_pressed = True
        elif GPIO.input(BUTTON_PIN) == GPIO.LOW:
            button_pressed = False

        time.sleep(0.1)
except KeyboardInterrupt:
    print("Stopping alert button.")
finally:
    GPIO.cleanup()
