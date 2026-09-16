from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import engine, Base
from routers import campus,building

import models


@asynccontextmanager
async def lifespan(app: FastAPI):

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

    await engine.dispose()


app = FastAPI(
    title="CampusQr",
    version="0.1.0",
    lifespan=lifespan
)

app.include_router(campus.router)
app.include_router(building.router)

