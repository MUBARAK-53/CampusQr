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


class CreateBuilding(BaseModel):
    building_name:str
    building_code:str
    latitude:float
    longitude:float


class UpdateBuilding(BaseModel):
    building_name:str
    building_code:str
    latitude:float
    longitude:float



class BuildingResponse(BaseModel):
    id:int
    building_name:str
    building_code:str
    latitude:float
    longitude:float

    class Config:
        from_attributes=True


class CreateFloor(BaseModel):
    floor_name:str
    floor_code:str



class UpdateFloor(BaseModel):
    floor_name:str
    floor_code:str


class FloorResponse(BaseModel):
    id:int
    floor_name:str
    floor_code:str
    building_id:int

    class Config:
        from_attributes=True

class QrResolveResponse(BaseModel):
    qr_data:str


class CreateLocation(BaseModel):
    id:int
    location_name: str
    location_code: str
    location_type: str
    building_id: int
    floor_id: int
    latitude: float
    longitude: float
    description: str | None = None

class UpdateLocation(BaseModel):
    id:int
    location_name: str
    location_code: str
    location_type: str
    building_id: int
    floor_id: int
    latitude: float
    longitude: float
    description: str | None = None

class LocationResponse(BaseModel):
    id: int
    location_name: str
    location_code: str
    location_type: str
    building_id: int
    floor_id: int
    latitude: float
    longitude: float
    description: str | None
    
