import RPi.GPIO as GPIO
import time
import requests
from dotenv import load_dotenv
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")



print("Alert button monitoring system is now active."
"\nPress Ctrl+C to stop.")

print()

button_pressed = False


data = {
    "chat_id": CHAT_ID,
    "text": "Someone pressed the alert button!"
}


try:

	while True:

		if GPIO.input(7) == GPIO.HIGH and not button_pressed:

			print("Someone pressed the alert button!")

			requests.post( "https://api.telegram.org/bot"+BOT_TOKEN+"/sendMessage", json = data )

			button_pressed = True


		elif GPIO.input(7) == GPIO.LOW:

			button_pressed = False


		time.sleep(0.1)

except KeyboardInterrupt:

	print("\nMonitoring stopped.")

	GPIO.cleanup()
