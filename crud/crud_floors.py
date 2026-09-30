from models import Building,Floor
from schema import CreateFloor,UpdateFloor
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException, status


async def create_floor(db:AsyncSession,floor:CreateFloor,building_code:str):

    result=await db.execute(
        select(Building).where(Building.building_code==building_code)
    )

    building=result.scalar_one_or_none()

    if not building:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Building Not Found!"
        )


    result=await db.execute(
        select(Floor).where(
            Floor.floor_code==floor.floor_code,
            Floor.building_id==building.id)
    )

    existing_floor=result.scalar_one_or_none()

    if existing_floor:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Floor Already Exists!"
        )

    new_floor=Floor(
        floor_name=floor.floor_name,
        floor_code=floor.floor_code,
        building_id=building.id
    )

    db.add(new_floor)

    await db.commit()

    await db.refresh(new_floor)

    return new_floor

async def get_floors(db:AsyncSession,building_code:str):

    result=await db.execute(
        select(Building).where(Building.building_code==building_code)
    )

    building=result.scalar_one_or_none()

    if not building:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Building Not Found!"
        )

    result=await db.execute(
        select(Floor).where(
            Floor.building_id==building.id
                            )
    )

    floor=result.scalars().all()

    return floor

async def get_floor_by_code(
    db: AsyncSession,
    building_code: str,
    floor_code: str
):

    result = await db.execute(
        select(Building).where(
            Building.building_code == building_code
        )
    )

    building = result.scalar_one_or_none()

    if not building:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Building Not Found!"
        )

    result = await db.execute(
        select(Floor).where(
            Floor.building_id == building.id,
            Floor.floor_code == floor_code
        )
    )

    floor = result.scalar_one_or_none()

    if not floor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Floor Not Found!"
        )

    return floor


async def update_floor(
    db: AsyncSession,
    building_code: str,
    floor_code: str,
    floor: UpdateFloor
):

    result = await db.execute(
        select(Building).where(
            Building.building_code == building_code
        )
    )

    building = result.scalar_one_or_none()

    if not building:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Building Not Found!"
        )

    result = await db.execute(
        select(Floor).where(
            Floor.building_id == building.id,
            Floor.floor_code == floor_code
        )
    )

    existing_floor = result.scalar_one_or_none()

    if not existing_floor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Floor Not Found!"
        )

    existing_floor.floor_name = floor.floor_name
    existing_floor.floor_code = floor.floor_code

    await db.commit()
    await db.refresh(existing_floor)

    return existing_floor


async def delete_floor(
    db: AsyncSession,
    building_code: str,
    floor_code: str
):

    result = await db.execute(
        select(Building).where(
            Building.building_code == building_code
        )
    )

    building = result.scalar_one_or_none()

    if not building:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Building Not Found!"
        )

    result = await db.execute(
        select(Floor).where(
            Floor.building_id == building.id,
            Floor.floor_code == floor_code
        )
    )

    existing_floor = result.scalar_one_or_none()

    if not existing_floor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Floor Not Found!"
        )

    await db.delete(existing_floor)

    await db.commit()

    return {
        "message": "Floor Deleted Successfully!"
    }