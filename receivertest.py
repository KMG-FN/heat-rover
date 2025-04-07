import RPi.GPIO as GPIO
import time

# Zählweise der Pins festlegen
GPIO.setmode(GPIO.BOARD)

# Pin 18 (GPIO 24) als Eingang festlegen
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# Schleifenzähler
i = 0

# Endlosschleife
while True:
    # Eingang lesen
    input = GPIO.input(18)
    print(input)
    time.sleep(0.5)

    #if GPIO.input(18) == GPIO.HIGH:
        # Wenn Eingang HIGH ist, Ausgabe im Terminal erzeugen
        
        