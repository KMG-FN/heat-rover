import asyncio
import json
import math
import os
import time
import RPi.GPIO as GPIO
import bme280
from fastapi import HTTPException
import smbus2
import adafruit_gps
import serial
import glob
import re

# GPS
uart = serial.Serial("/dev/serial0", baudrate=9600, timeout=10)
gps = adafruit_gps.GPS(uart, debug=False)
gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
gps.send_command(b"PMTK220,1000")

# Rover Motors
left = [12, 16]
right = [18, 22]
vertical = [24, 32]
grabber = [38, 40]

GPIO.setmode(GPIO.BOARD)

# BME280 senosor (temperature, humidity, pressure) via I2C
bme280_address = 0x76 
bme280_bus = smbus2.SMBus(1)
bme280_initialized = False

JSON_PATH = "logs/files_to_utc.json"

def init():
    """
    Inits pins and sensors
    """

    # Pins:
    for pin in left:
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        #GPIO.output(pin, GPIO.LOW)

    for pin in right:
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        #GPIO.output(pin, GPIO.LOW)

    for pin in vertical:
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        #GPIO.output(pin, GPIO.LOW)

    for pin in grabber:
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        #GPIO.output(pin, GPIO.LOW)

    # Sensors:  
    try: 
        bme280.load_calibration_params(bme280_bus,bme280_address)
        bme280_data = bme280.sample(bme280_bus,bme280_address)
        global bme280_initialized
        bme280_initialized = True
    except Exception as e:
        print(e)

    print('initialized')


def moveRoverLeft(action):
    print("left", action)
    if action == 'forward':
        GPIO.output(left[0], GPIO.LOW)
        GPIO.output(left[1], GPIO.HIGH)
    elif action == 'backward':
        GPIO.output(left[0], GPIO.HIGH)
        GPIO.output(left[1], GPIO.LOW)
    else:
        GPIO.output(left[0], GPIO.LOW)
        GPIO.output(left[1], GPIO.LOW)


def moveRoverRight(action):
    if action == 'forward':
        print("forward")
        GPIO.output(right[0], GPIO.LOW)
        GPIO.output(right[1], GPIO.HIGH)
    elif action == 'backward':
        print("backward")
        GPIO.output(right[0], GPIO.HIGH)
        GPIO.output(right[1], GPIO.LOW)
    else:
        print("stop")
        GPIO.output(right[0], GPIO.LOW)
        GPIO.output(right[1], GPIO.LOW)


def moveCraneVertical(action):
    print("vertical", action)
    if action == 'up':
        GPIO.output(vertical[0], GPIO.LOW)
        GPIO.output(vertical[1], GPIO.HIGH)
    elif action == 'down':
        GPIO.output(vertical[0], GPIO.HIGH)
        GPIO.output(vertical[1], GPIO.LOW)
    else:
        GPIO.output(vertical[0], GPIO.LOW)
        GPIO.output(vertical[1], GPIO.LOW)

def moveCraneGrabber(action):
    if action == "close":
       GPIO.output(grabber[0], GPIO.LOW)
       GPIO.output(grabber[1], GPIO.HIGH)
    elif action == "open":
       GPIO.output(grabber[0], GPIO.HIGH)
       GPIO.output(grabber[1], GPIO.LOW)
    else:
       GPIO.output(grabber[0], GPIO.LOW)
       GPIO.output(grabber[1], GPIO.LOW)


def get_sensor_data():
    global bme280_initialized
    
    humidity = -1
    pressure = -1
    ambient_temperature = -1
    if bme280_initialized:
        bme280_data = bme280.sample(bme280_bus,bme280_address)
        humidity  = bme280_data.humidity
        pressure  = bme280_data.pressure
        ambient_temperature = bme280_data.temperature

    gps.update()
    distance = -1
    hdop = -1
    if gps.has_fix and start_lat != -1:
      lat = dmm_to_decimal(gps.latitude_degrees, gps.latitude_minutes)
      lon = dmm_to_decimal(gps.longitude_degrees, gps.longitude_minutes)
      distance = haversine(start_lat, start_lon, lat, lon)
      hdop = gps.horizontal_dilution

    return {"humidity": round(humidity, 1),
            "pressure": round(pressure, 1),
            "temperature": round(ambient_temperature, 1),
            "distance": round(distance, 1),
            "hdop": round(hdop, 1)}

utc_formatted = None

def get_utc():
    """
    Get the current UTC time.
    """
    global utc_formatted

    utc = None
    while utc is None or utc.tm_year == 0:
        time.sleep(1)
        gps.update()
        utc = gps.timestamp_utc       

    utc_formatted = f"{utc.tm_year}-{utc.tm_mon}-{utc.tm_mday}_{utc.tm_hour}:{utc.tm_min}:{utc.tm_sec}"

file_number = 0

def get_file_number():
    """Find next highest number of csv-files"""
    csv_files = glob.glob(os.path.join("logs", "*.csv"))
   
    biggest_number = 0
    for file in csv_files:
      match = re.search(r"(\d+)", os.path.basename(file))
      if match:
         x = int(match.group(1))
         if x > biggest_number:
            biggest_number = x

    global file_number
    file_number = biggest_number + 1

async def save_sensor_data():
    """
    Save sensor data to a file.
    """
    
    # get_utc()
    get_file_number()
    global file_number

    with open(f"logs/{file_number}.csv", "a") as f:
        f.write("seconds,humidity,pressure,temperature,distance,hdop (gps accuracy)\n")

        seconds = 0
        global start_lat
        global start_lon

        while True:
            # get humidity, pressure and temperature
            data = get_sensor_data()
            
            f.write(f"{seconds},{data['humidity']},{data['pressure']},{data['temperature']},{data['distance']},{data['hdop']}\n")
            f.flush()
            seconds += 1
            await asyncio.sleep(1)
            
def dmm_to_decimal(degree, minutes):
   decimal = degree + minutes / 60.0
   return decimal

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance in meters between two points on the earth
    """
    R = 6371000  # radius of Earth in meters
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2.0)**2 + \
        math.cos(phi1) * math.cos(phi2) * \
        math.sin(delta_lambda / 2.0)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c

start_lat = -1
start_lon = -1

async def get_gps_fix():
    """
    Gets the initial GPS-fix. Takes an average of 5 samples with HDOP < 1.2 (horizontal dilution of precision).
    """
    start_fixes = []
    while True:
        await asyncio.sleep(1)
        # Check for fix every second
        gps.update()
        if not gps.has_fix:
            # Try again if we don't have a fix yet.
            continue
        # We have a fix! (gps.has_fix is true)
        if gps.horizontal_dilution < 1.1:
            start_fixes.append((dmm_to_decimal(gps.latitude_degrees, gps.latitude_minutes),dmm_to_decimal(gps.longitude_degrees, gps.longitude_minutes)))
            if len(start_fixes) >= 5:
                break
        
        # save gps-utc to json
        global utc_formatted
        if utc_formatted == None:
            get_utc()
            
            try: 
                with open(JSON_PATH, "r") as f:
                    files_to_utc = json.load(f)
            except:
                files_to_utc = {"files_to_utc": []}

            global file_number
            
            files_to_utc["files_to_utc"].append({"file": file_number, "utc": utc_formatted})

            with open(JSON_PATH, "w") as f:
               json.dump(files_to_utc, f, indent=4)

    # Calculate average
    global start_lat
    global start_lon
    start_lat = sum([fix[0] for fix in start_fixes]) / len(start_fixes)
    start_lon = sum([fix[1] for fix in start_fixes]) / len(start_fixes)

def get_list_of_logs():
    """
    Get list of log files in the logs directory.
    """
    
    with open(JSON_PATH, "r") as f:
       files_to_utc = json.load(f)

    logs = []
    for file in os.listdir("logs"):
        if file.endswith(".csv"):
            utc_found = False
            for pair in files_to_utc["files_to_utc"]:
                if str(pair["file"]) == file.split(".")[0]:
                    utc_found = True
                    logs.append(pair["utc"] + ".csv")
            if not utc_found:
                logs.append(file)
    
    return logs

def get_log_path(log: str):
    with open(JSON_PATH, "r") as f:
        files_to_utc = json.load(f)
    
    for pair in files_to_utc["files_to_utc"]:
       if pair["utc"] == log.split(".")[0]:
          return "logs/" + str(pair["file"]) + ".csv"
    
    return "logs/" + log