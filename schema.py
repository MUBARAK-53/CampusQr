from typing import Literal
from pydantic import BaseModel,EmailStr
from datetime import datetime



class User(BaseModel):
    id:int
    username:str
    email:EmailStr
    hashed_password:str


class CreateCampus(BaseModel):
    name:str
    address:str
    campus_code:str
    latitude:float
    longitude:float


class UpdateCampus(BaseModel):
    name:str
    address:str
    latitude:float
    longitude:float

class CampusResponse(BaseModel):
    id:int
    name:str
    address:str
    campus_code:str
    latitude:float
    longitude:float
    created_at:datetime

    class Config:
        from_attributes=True
