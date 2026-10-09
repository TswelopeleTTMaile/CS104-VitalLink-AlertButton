import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


print("Alert button monitoring system is now active."
"\nPress Ctrl+C to stop.")

print()

button_pressed = False


try:

	while True:

		if GPIO.input(7) == GPIO.HIGH and not button_pressed:

			print("Someone pressed the alert button!")

			button_pressed = True


		elif GPIO.input(7) == GPIO.LOW:

			button_pressed = False


		time.sleep(0.1)

except KeyboardInterrupt:

	print("\nMonitoring stopped.")

	GPIO.cleanup()
