from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    #allow_credentials=False,
    allow_methods=["*"],
    #allow_headers=["*"],
)

class MoveRequest(BaseModel):
    direction: str
    action: str

@app.post("/api/move")
async def move(move: MoveRequest):
    """
    Move the character in the specified direction and perform the specified action.
    """
    # Here you would implement the logic to move the character and perform the action
    # For now, we'll just return a success message
    print(f"Moving {move.direction} and performing {move.action}")
    return {"message": f"Moved {move.direction} and performed {move.action}"}