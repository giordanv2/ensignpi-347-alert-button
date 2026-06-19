import os
import time

import RPi.GPIO as GPIO
import requests


BUTTON_PIN = 7
ALERT_TEXT = "Someone pressed the alert button!"
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "CHAT_ID")


def send_telegram_alert():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": ALERT_TEXT,
    }

    response = requests.post(url, json=data, timeout=10)
    response.raise_for_status()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

button_pressed = False

try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.HIGH and not button_pressed:
            print(ALERT_TEXT)
            send_telegram_alert()
            button_pressed = True
        elif GPIO.input(BUTTON_PIN) == GPIO.LOW:
            button_pressed = False

        time.sleep(0.1)
except KeyboardInterrupt:
    print("Stopping alert button.")
finally:
    GPIO.cleanup()
