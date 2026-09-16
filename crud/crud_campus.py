from models import Campus
from schema import CreateCampus,UpdateCampus
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException,status


async def create_campus(db:AsyncSession,campus:CreateCampus):

    result=await db.execute(
        select(Campus).where(Campus.campus_code==campus.campus_code)
    )

    existing_campus=result.scalar_one_or_none()

    if existing_campus is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Campus Already Exists!"
        )

    new_campus=Campus(
        name=campus.name,
        address=campus.address,
        campus_code=campus.campus_code,
        latitude=campus.latitude,
        longitude=campus.longitude
    )

    db.add(new_campus)

    await db.commit()

    await db.refresh(new_campus)

    return new_campus


async def get_campus(db:AsyncSession):

    result=await db.execute(
            select(Campus)
        )
    
    existing_campus=result.scalars().all()
    
    if not existing_campus :
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Campus Not Found!"
            )

    return existing_campus
    


async def get_campus_by_code(db:AsyncSession,campus_code:str):
    result=await db.execute(
             select(Campus).where(Campus.campus_code==campus_code)
         )
     
    existing_campus=result.scalar_one_or_none()
     
    if existing_campus is None:
             raise HTTPException(
                 status_code=status.HTTP_404_NOT_FOUND,
                 detail="Campus Not Found!"
             )

    return existing_campus


async def update_campus(db:AsyncSession,campus_code:str,campus:UpdateCampus):

    result=await db.execute(
        select(Campus).where(Campus.campus_code==campus_code)
              )
          
    existing_campus=result.scalar_one_or_none()
          
    if existing_campus is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Campus Not Found!"
            )

    existing_campus.name=campus.name
    existing_campus.latitude=campus.latitude
    existing_campus.longitude=campus.longitude
    existing_campus.address=campus.address

    await db.commit()
    await db.refresh(existing_campus)

    return existing_campus


async def delete_campus(db:AsyncSession,campus_code:str):

    result=await db.execute(
                  select(Campus).where(Campus.campus_code==campus_code)
              )
          
    existing_campus=result.scalar_one_or_none()
          
    if existing_campus is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Campus Not Found!"
        )

    await db.delete(existing_campus)

    await db.commit()

    return {
        "message": "Campus deleted successfully"
         
    }
     
      
