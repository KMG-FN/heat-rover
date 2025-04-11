import asyncio
#from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import rover

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
)

stop_rover_move = {"left": None, "right": None}
stop_rover_crane = {"vertical": None, "grabber": None}

rover.init()

async def stop_rover(direction: str):
    """
    Stop the rover after 1 second of inactivity.
    """
    await asyncio.sleep(1)
    if direction == "left":
        rover.moveRoverLeft("stop")
    elif direction == "right":
        rover.moveRoverRight("stop")


async def stop_crane(direction: str):
    """
    Stop the crane after 1 second of inactivity.
    """
    await asyncio.sleep(1)
    if direction == "vertical":
        rover.moveCraneVertical("stop")
    elif direction == "grabber":
        rover.moveCraneGrabber("stop")


class MoveRequest(BaseModel):
    direction: str
    action: str

@app.post("/api/move")
async def move(move: MoveRequest):
    """
    Move the correct side of the rover forward/backword/stop.
    Includes a failsafe that stops moving if no command was received within 1 second.
    """
    global stop_rover_move

    if move.action != "stop":
        # cancel existing stop task (if existing)
        if stop_rover_move[move.direction]:
            stop_rover_move[move.direction].cancel()
        
        # start a new stop task
        stop_rover_move[move.direction] = asyncio.create_task(stop_rover(move.direction))
    
    else:
        # stop the delayed stop task
        if stop_rover_move[move.direction]:
            stop_rover_move[move.direction].cancel()

    if move.direction == "left":
        rover.moveRoverLeft(move.action)
    elif move.direction == "right":
        rover.moveRoverRight(move.action)

    return {"message": f"Moved {move.direction} and performed {move.action}"}


@app.post("/api/crane")
async def crane(move: MoveRequest):
    """
    Move the crane up/down or open/close the grabber.
    """
    
    global stop_rover_crane

    if move.action != "stop":
        # cancel existing stop task (if existing)
        if stop_rover_crane[move.direction]:
            stop_rover_crane[move.direction].cancel()
        
        # start a new stop task
        stop_rover_crane[move.direction] = asyncio.create_task(stop_crane(move.direction))

    else:
        # stop the delayed stop task
        if stop_rover_crane[move.direction]:
            stop_rover_crane[move.direction].cancel()

    if move.direction == "vertical":
        rover.moveCraneVertical(move.action)
    elif move.direction == "grabber":
        rover.moveCraneGrabber(move.action)

    #print(f"Command: {move.direction}, {move.action}")
    return {"message": f"Received {move.direction}, {move.action}"}

@app.get("/api/getSensorData")
async def getSensorData():
    return rover.get_sensor_data()