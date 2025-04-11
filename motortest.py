import RPi.GPIO as GPIO

# Relais-Pins definieren
pin1 = 12
pin2 = 16
pin3 = 24
pin4 = 32

# GPIO-Modus setzen
GPIO.setmode(GPIO.BOARD)

# Alle Relais-Pins als Output setzen
pins = {1: pin1, 2: pin2, 3: pin3, 4: pin4}
for pin in pins.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 1)  # Standardmäßig auf HIGH setzen (Relais aus)

def set_pin(pin_number, state):
    """Schaltet den angegebenen Pin auf HIGH oder LOW."""
    if pin_number in pins:
        GPIO.output(pins[pin_number], GPIO.HIGH if state == "high" else GPIO.LOW)
        print(f"Pin {pin_number} wurde auf {state.upper()} gesetzt.")
    else:
        print("Ungültige Pin-Nummer. Bitte 1-4 eingeben.")

try:
    while True:
        user_input = input("Eingabe (Format: pin high/low, z. B. '2 low'): ").strip().split()
        if len(user_input) == 2:
            try:
                pin = int(user_input[0])
                state = user_input[1].lower()
                if state in ["high", "low"]:
                    set_pin(pin, state)
                else:
                    print("Ungültige Eingabe. Bitte 'high' oder 'low' verwenden.")
            except ValueError:
                print("Ungültige Pin-Nummer. Bitte eine Zahl zwischen 1 und 4 eingeben.")
        else:
            print("Falsches Eingabeformat. Bitte 'pin high/low' eingeben.")

except KeyboardInterrupt:
    print("\nProgramm beendet.")
    GPIO.cleanup()  # GPIO-Pins zurücksetzen
