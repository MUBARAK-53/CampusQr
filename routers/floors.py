from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from dependency import get_db
from schema import CreateFloor, UpdateFloor, FloorResponse
from crud import crud_floors


router = APIRouter(
    prefix="/buildings/{building_code}/floor",
    tags=["Floors"]
)


@router.post("", response_model=FloorResponse)
async def create_floor(
    floor: CreateFloor,
    building_code: str,
    db: AsyncSession = Depends(get_db)
):
    return await crud_floors.create_floor(
        db,
        floor,
        building_code
    )


@router.get("", response_model=list[FloorResponse])
async def get_floors(
    building_code: str,
    db: AsyncSession = Depends(get_db)
):
    return await crud_floors.get_floors(
        db,
        building_code
    )


@router.get("/{floor_code}", response_model=FloorResponse)
async def get_floor_by_code(
    building_code: str,
    floor_code: str,
    db: AsyncSession = Depends(get_db)
):
    return await crud_floors.get_floor_by_code(
        db,
        building_code,
        floor_code
    )


@router.put("/{floor_code}", response_model=FloorResponse)
async def update_floor(
    building_code: str,
    floor_code: str,
    floor: UpdateFloor,
    db: AsyncSession = Depends(get_db)
):
    return await crud_floors.update_floor(
        db,
        building_code,
        floor_code,
        floor
    )


@router.delete("/{floor_code}")
async def delete_floor(
    building_code: str,
    floor_code: str,
    db: AsyncSession = Depends(get_db)
):
    return await crud_floors.delete_floor(
        db,
        building_code,
        floor_code
    )