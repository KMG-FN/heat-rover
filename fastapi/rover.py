import asyncio
import os
import random
import RPi.GPIO as GPIO
import bme280
import smbus2

# Rover Motors
left = [12, 16]
right = [18,22]
vertical = [24,32]

GPIO.setmode(GPIO.BOARD)

# BME280 senosor (temperature, humidity, pressure) via I2C
bme280_address = 0x76 
bme280_bus = smbus2.SMBus(1)

def init():
  """
  Inits pins and sensors
  """

  # Pins:
  for pin in left:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

  for pin in right:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

  for pin in vertical:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

  # Sensors:
  bme280.load_calibration_params(bme280_bus,bme280_address)

  print('initialized')


def moveRoverLeft(action):
  if action == 'forward':
      GPIO.output(left[0], GPIO.HIGH)
      GPIO.output(left[1], GPIO.LOW)
  elif action == 'backward':
      GPIO.output(left[0], GPIO.LOW)
      GPIO.output(left[1], GPIO.HIGH)
  else:
      GPIO.output(left[0], GPIO.HIGH)
      GPIO.output(left[1], GPIO.HIGH)


def moveRoverRight(action):
  if action == 'forward':
     GPIO.output(right[0], GPIO.HIGH)
     GPIO.output(right[1], GPIO.LOW)
  if action == 'backward':
     GPIO.output(right[0], GPIO.LOW)
     GPIO.output(right[1], GPIO.HIGH)
  else:
     GPIO.output(right[0], GPIO.HIGH)
     GPIO.output(right[1], GPIO.HIGH)


def moveCraneVertical(action):
  if action == 'up':
     GPIO.output(vertical[0], GPIO.HIGH)
     GPIO.output(vertical[1], GPIO.LOW)
  if action == 'down':
     GPIO.output(vertical[0], GPIO.LOW)
     GPIO.output(vertical[1], GPIO.HIGH)
  else:
     GPIO.output(vertical[0], GPIO.HIGH)
     GPIO.output(vertical[1], GPIO.HIGH)

def moveCraneGrabber(action):
  print("Moving crane grabber", action)


def get_sensor_data():
    bme280_data = bme280.sample(bme280_bus,bme280_address)
    humidity  = bme280_data.humidity
    pressure  = bme280_data.pressure
    ambient_temperature = bme280_data.temperature
    return {"humidity": round(humidity, 1),
            "pressure": round(pressure, 1),
            "temperature": round(ambient_temperature, 1)}

async def save_sensor_data():
    """
    Save sensor data to a file.
    """
    
    with open(f"logs/H.E.A.T.-{random.randint(1,1000)}.csv", "a") as f:
        f.write("time,humidity,pressure,temperature\n")

        while True:
          data = get_sensor_data()    
          f.write(f"{random.randint(1,1000)},{data['humidity']},{data['pressure']},{data['temperature']}\n")
          f.flush()
          await asyncio.sleep(1)

def get_list_of_logs():
    """
    Get list of log files in the logs directory.
    """
    
    logs = []
    for file in os.listdir("logs"):
        if file.endswith(".csv"):
            logs.append(file)
    
    return logs