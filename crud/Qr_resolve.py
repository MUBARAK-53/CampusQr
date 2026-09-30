from models import Campus, Building, Floor
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException, status


async def resolve_qr(db: AsyncSession, qr_data: str):

    # Step 1: Split QR data
    parts = qr_data.split(":")

    # Step 2: Check basic QR format
    if len(parts) < 3 or parts[0] != "CAMPUSQR":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid Qr Code!"
        )

    # Step 3: Get QR type
    qr_type = parts[1]

    # =========================
    # CAMPUS QR
    # =========================
    if qr_type == "CAMPUS":

        if len(parts) != 3:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid Campus Qr Code!"
            )

        campus_code = parts[2]

        result = await db.execute(
            select(Campus).where(
                Campus.campus_code == campus_code
            )
        )

        campus = result.scalar_one_or_none()

        if campus is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Campus Not Found!"
            )

        return {
            "qr_type": "CAMPUS",
            "data": {
                "id": campus.id,
                "name": campus.name,
                "address": campus.address,
                "campus_code": campus.campus_code,
                "latitude": campus.latitude,
                "longitude": campus.longitude
            }
        }

    # =========================
    # BUILDING QR
    # =========================
    elif qr_type == "BUILDING":

        if len(parts) != 3:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid Building Qr Code!"
            )

        building_code = parts[2]

        result = await db.execute(
            select(Building).where(
                Building.building_code == building_code
            )
        )

        building = result.scalar_one_or_none()

        if building is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Building Not Found!"
            )

        return {
            "qr_type": "BUILDING",
            "data": {
                "id": building.id,
                "building_name": building.building_name,
                "building_code": building.building_code,
                "latitude": building.latitude,
                "longitude": building.longitude,
                "campus_id": building.campus_id
            }
        }

    # =========================
    # FLOOR QR
    # =========================
    elif qr_type == "FLOOR":

        if len(parts) != 4:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid Floor Qr Code!"
            )

        # Get building code
        building_code = parts[2]

        # Get floor code
        floor_code = parts[3]

        # Find building
        result = await db.execute(
            select(Building).where(
                Building.building_code == building_code
            )
        )

        building = result.scalar_one_or_none()

        if building is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Building Not Found!"
            )

        # Find floor inside this building
        result = await db.execute(
            select(Floor).where(
                Floor.building_id == building.id,
                Floor.floor_code == floor_code
            )
        )

        floor = result.scalar_one_or_none()

        if floor is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Floor Not Found!"
            )

        return {
            "qr_type": "FLOOR",
            "data": {
                "id": floor.id,
                "floor_name": floor.floor_name,
                "floor_code": floor.floor_code,
                "building_id": floor.building_id
            }
        }

    # =========================
    # UNSUPPORTED QR
    # =========================
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Unsupported QR Type!"
        )