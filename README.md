# H.E.A.T. Rover
Code of our Rover for the [DLR Summer School Vulcano 2025](https://www.dlr.de/de/schoollab/aktuelles/ankuendigungen/2025/ausschreibung-dlr_summer_school-vulcano-2025)

- Frontend written in Svelte.
- Backend written in Python FastAPI

# Raspberry Pi PINs

Outer Side:
- 2 (5V): GPS (VIN)
- 4 (5V): Relais (Power in)
- 6 (GND): GPS (GND)
- 8 (UART TX): GPS (RX)
- 10 (UART RX): GPS (TX)
- 12: Left Forward (on low)
- 14 (GND): ---
- 16: Left Backward (on low)
- 18: Right Forward (on low)
- 20 (GND): ---
- 22: Right Backward (on low)
- 24: Vertical 
- 26:
- 28:
- 30:
- 32: Vertical
- 34 (GND): ---
- 36: 
- 38: 
- 40

Inner Side:
- 1 (3V): BME280-Sensor (VCC)
- 3 (I2C SDA): BME280-Sensor (SDA)
- 5 (I2C SCL): BME280-Sensor (SCL)
- 7: 
- 9 (GND): BME280-Sensor (GND)
- 11:
- 13:
- 15:
- 17:
- 19:
- 21:
- 23:
- 25 (GND):
- 27:
- 29:
- 31:
- 33:
- 35:
- 37:
- 39 (GND):

# How it works in the Raspi

The Python FastAPI-Code is running as System-Deamon on Startup.

We are using the Webserver NGINX to deliver the Frontend-Code or to redirect API-Requests to FastAPI, when a HTTP-request goes to /api

# Develop Frontend

- Install Node.js (we used 22)
- Go to `/frontend`
- Run `npm run dev -- --host`

# Develop Backend

- Go to `/backend`
- Python 3.11 should be installed and available via a virtual environment (automatically on our Raspberry Pi)
- Run `fastapi dev main.py --host 0.0.0.0 --port 8080`