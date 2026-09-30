from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from dependency import get_db
from schema import QrResolveResponse
from crud import Qr_resolve



router = APIRouter(
    prefix="/qr",
    tags=["Qr"]
)

@router.post("/resolve")

async def resolve_qr(request:QrResolveResponse,db:AsyncSession=Depends(get_db)):
    return await Qr_resolve.resolve_qr(db,request.qr_data)

