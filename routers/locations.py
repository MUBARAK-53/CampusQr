from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from dependency import get_db
from schema import CreateLocation, UpdateLocation, LocationResponse
from crud import crud_locations

router = APIRouter(
    prefix="/buildings/{building_code}/floor/{floor_code}/locations",
    tags=["Locations"]
)


@router.post("/", response_model=LocationResponse)
async def create_new_location(
    building_code: str,
    floor_code: str,
    location: CreateLocation,
    db: AsyncSession = Depends(get_db)
):
    return await crud_locations.create_location(
        db,
        location,
        floor_code,
        location.location_code
    )


@router.get("/", response_model=list[LocationResponse])
async def get_all_locations(
    building_code: str,
    floor_code: str,
    db: AsyncSession = Depends(get_db)
):
    return await crud_locations.get_locations(db, floor_code)


@router.get("/{location_code}", response_model=LocationResponse)
async def get_location(
    building_code: str,
    floor_code: str,
    location_code: str,
    db: AsyncSession = Depends(get_db)
):
    return await crud_locations.get_single_location(
        db,
        floor_code,
        location_code
    )


@router.put("/{location_code}", response_model=LocationResponse)
async def update_existing_location(
    building_code: str,
    floor_code: str,
    location_code: str,
    location: UpdateLocation,
    db: AsyncSession = Depends(get_db)
):
    return await crud_locations.update_location(
        db,
        location,
        floor_code,
        location_code
    )


@router.delete("/{location_code}")
async def delete_existing_location(
    building_code: str,
    floor_code: str,
    location_code: str,
    db: AsyncSession = Depends(get_db)
):
    return await crud_locations.delete_location(
        db,
        floor_code,
        location_code
    )