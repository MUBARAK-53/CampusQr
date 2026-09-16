from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from dependency import get_db
from schema import CreateBuilding,UpdateBuilding,BuildingResponse
from crud import crud_buildings


router = APIRouter(
    prefix="/campuses/{campus_code}/buildings",
    tags=["Building"]
)

@router.post("",response_model=BuildingResponse)

async def create_building(building:CreateBuilding,campus_code:str,db:AsyncSession=Depends(get_db),):
    return await crud_buildings.create_building(db,building,campus_code)

@router.get("", response_model=list[BuildingResponse])
async def get_buildings(
    campus_code: str,
    db: AsyncSession = Depends(get_db)
):
    return await crud_buildings.get_buildings(
        db,
        campus_code
    )


@router.get("/{building_code}", response_model=BuildingResponse)
async def get_building_by_code(
    campus_code: str,
    building_code: str,
    db: AsyncSession = Depends(get_db)
):
    return await crud_buildings.get_building_by_code(
        db,
        campus_code,
        building_code
    )


@router.put("/{building_code}", response_model=BuildingResponse)
async def update_building(
    campus_code: str,
    building_code: str,
    building: UpdateBuilding,
    db: AsyncSession = Depends(get_db)
):
    return await crud_buildings.update_building(
        db,
        campus_code,
        building_code,
        building
    )


@router.delete("/{building_code}")
async def delete_building(
    campus_code: str,
    building_code: str,
    db: AsyncSession = Depends(get_db)
):
    return await crud_buildings.delete_building(
        db,
        campus_code,
        building_code
    )