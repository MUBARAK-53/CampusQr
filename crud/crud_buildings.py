from models import Campus, Building
from schema import CreateBuilding,UpdateBuilding
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException, status


async def create_building(
    db: AsyncSession,
    building: CreateBuilding,
    campus_code: str
):
    campus_result = await db.execute(
        select(Campus).where(
            Campus.campus_code == campus_code
        )
    )

    campus = campus_result.scalar_one_or_none()

    if not campus:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Campus not found"
        )

    result = await db.execute(
        select(Building).where(
            Building.building_code == building.building_code,
            Building.campus_id == campus.id
        )
    )

    existing_building = result.scalar_one_or_none()

    if existing_building:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Building already exists!"
        )

    new_building = Building(
        building_name=building.building_name,
        building_code=building.building_code,
        latitude=building.latitude,
        longitude=building.longitude,
        campus_id=campus.id
    )

    db.add(new_building)

    await db.commit()
    await db.refresh(new_building)

    return new_building


async def get_buildings(db:AsyncSession,campus_code:str):
    campus_result = await db.execute(
            select(Campus).where(
                Campus.campus_code == campus_code
            )
        )
    
    campus = campus_result.scalar_one_or_none()
    
    if not campus:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Campus not found"
            )
    
    result = await db.execute(
        select(Building).where(
            Building.campus_id == campus.id
        )
        )
    
    buildings = result.scalars().all()

    return buildings


async def get_building_by_code(db:AsyncSession,campus_code:str,building_code:str):
    campus_result = await db.execute(
            select(Campus).where(
                Campus.campus_code == campus_code
            )
        )
    
    campus = campus_result.scalar_one_or_none()
    
    if not campus:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Campus not found"
            )
    
    result = await db.execute(
        select(Building).where(
            Building.campus_id == campus.id,
            Building.building_code==building_code
        )
        )
    
    building= result.scalar_one_or_none()

    if not building:
         raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Building Not Found!" 
            )

    return building


async def update_building(
    db: AsyncSession,
    campus_code: str,
    building_code: str,
    building: UpdateBuilding
):
    campus_result = await db.execute(
        select(Campus).where(
            Campus.campus_code == campus_code
        )
    )

    campus = campus_result.scalar_one_or_none()

    if not campus:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Campus not found"
        )

    result = await db.execute(
        select(Building).where(
            Building.campus_id == campus.id,
            Building.building_code == building_code
        )
    )

    existing_building = result.scalar_one_or_none()

    if not existing_building:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Building not found"
        )

    existing_building.building_name = building.building_name
    existing_building.building_code = building.building_code
    existing_building.latitude = building.latitude
    existing_building.longitude = building.longitude

    await db.commit()
    await db.refresh(existing_building)

    return existing_building


async def delete_building(db:AsyncSession,campus_code:str,building_code:str):

    campus_result = await db.execute(
             select(Campus).where(
                 Campus.campus_code == campus_code
             )
         )
     
    campus = campus_result.scalar_one_or_none()
     
    if not campus:
             raise HTTPException(
                 status_code=status.HTTP_404_NOT_FOUND,
                 detail="Campus not found"
             )
     
    result = await db.execute(
             select(Building).where(
                 Building.campus_id == campus.id,
                 Building.building_code == building_code
             )
         )
     
    existing_building = result.scalar_one_or_none()

    if not existing_building:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Building Not Found!"
        )

    await db.delete(existing_building)

    await db.commit()

    return {
        "message":"Building Deleted Succesfully!"
    }
         
