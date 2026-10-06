from models import Building,Floor,Locations
from schema import CreateLocation,UpdateLocation
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException, status


async def create_location(db:AsyncSession,location:CreateLocation,floor_code:str,location_code:str):
    result=await db.execute(
        select(Floor).where(
            Floor.floor_code==floor_code
        )
    )

    floor=result.scalar_one_or_none()

    if not floor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Floor NOt Found!"
    
        )

    result=await db.execute(
            select(Locations).where(
                Locations.floor_id==floor.id,
                Locations.building_id==floor.building_id,
                Locations.location_code==location_code
            )
        )
    
    existing_location=result.scalar_one_or_none()
    
    if existing_location:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Location Already Exists!"
        
        )

    new_location = Locations(
        location_name=location.location_name,
        location_code=location.location_code,
        location_type=location.location_type,
        building_id=location.building_id,
        floor_id=floor.id,
        latitude=location.latitude,
        longitude=location.longitude,
        description=location.description
    )

    db.add(new_location)

    await db.commit()

    await db.refresh(new_location)

    return new_location

async def get_locations(
    db: AsyncSession,
    building_code: str,
    floor_code: str
):
    # Find building
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

    # Find floor inside this building
    result = await db.execute(
        select(Floor).where(
            Floor.floor_code == floor_code,
            Floor.building_id == building.id
        )
    )

    floor = result.scalar_one_or_none()

    if not floor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Floor Not Found!"
        )

    # Get locations
    result = await db.execute(
        select(Locations).where(
            Locations.floor_id == floor.id,
            Locations.building_id == building.id
        )
    )

    locations = result.scalars().all()

    return locations

async def get_single_location(
    db: AsyncSession,
    floor_code: str,
    location_code: str
):
    result = await db.execute(
        select(Floor).where(
            Floor.floor_code == floor_code
        )
    )

    floor = result.scalar_one_or_none()

    if not floor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Floor Not Found!"
        )

    result = await db.execute(
        select(Locations).where(
            Locations.floor_id == floor.id,
            Locations.building_id == floor.building_id,
            Locations.location_code == location_code
        )
    )

    location = result.scalar_one_or_none()

    if not location:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Location Not Found!"
        )

    return location

async def update_location(
    db: AsyncSession,
    location: UpdateLocation,
    floor_code: str,
    location_code: str
):
    # Find floor
    result = await db.execute(
        select(Floor).where(
            Floor.floor_code == floor_code
        )
    )

    floor = result.scalar_one_or_none()

    if not floor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Floor Not Found!"
        )

    # Find location
    result = await db.execute(
        select(Locations).where(
            Locations.floor_id == floor.id,
            Locations.building_id == floor.building_id,
            Locations.location_code == location_code
        )
    )

    existing_location = result.scalar_one_or_none()

    if not existing_location:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Location Not Found!"
        )

    # Update fields
    existing_location.location_name = location.location_name
    existing_location.location_code = location.location_code
    existing_location.location_type = location.location_type
    existing_location.latitude = location.latitude
    existing_location.longitude = location.longitude
    existing_location.description = location.description

    await db.commit()
    await db.refresh(existing_location)

    return existing_location


async def delete_location(
    db: AsyncSession,
    floor_code: str,
    location_code: str
):
    # Find floor
    result = await db.execute(
        select(Floor).where(
            Floor.floor_code == floor_code
        )
    )

    floor = result.scalar_one_or_none()

    if not floor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Floor Not Found!"
        )

    # Find location
    result = await db.execute(
        select(Locations).where(
            Locations.floor_id == floor.id,
            Locations.building_id == floor.building_id,
            Locations.location_code == location_code
        )
    )

    location = result.scalar_one_or_none()

    if not location:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Location Not Found!"
        )

    await db.delete(location)
    await db.commit()

    return {
        "message": "Location Deleted Successfully!"
    }