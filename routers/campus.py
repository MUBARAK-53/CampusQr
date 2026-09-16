from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from dependency import get_db
from schema import CreateCampus, UpdateCampus, CampusResponse
from crud import crud_campus


router = APIRouter(
    prefix="/campuses",
    tags=["Campus"]
)


@router.post("/", response_model=CampusResponse)
async def create_new_campus(
    campus: CreateCampus,
    db: AsyncSession = Depends(get_db)
):
    return await crud_campus.create_campus(db, campus)


@router.get("/", response_model=list[CampusResponse])
async def get_all_campuses(
    db: AsyncSession = Depends(get_db)
):
    return await crud_campus.get_campus(db)


@router.get("/{campus_code}", response_model=CampusResponse)
async def get_single_campus(
    campus_code: str,
    db: AsyncSession = Depends(get_db)
):
    return await crud_campus.get_campus_by_code(db, campus_code)


@router.put("/{campus_code}", response_model=CampusResponse)
async def update_existing_campus(
    campus_code: str,
    campus: UpdateCampus,
    db: AsyncSession = Depends(get_db)
):
    return await crud_campus.update_campus(db, campus_code, campus)


@router.delete("/{campus_code}")
async def delete_existing_campus(
    campus_code: str,
    db: AsyncSession = Depends(get_db)
):
    return await crud_campus.delete_campus(db, campus_code)