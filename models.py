from database import Base
from sqlalchemy import Column,Integer,String,FLOAT,DateTime,func,ForeignKey

class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True,nullable=False)
    username=Column(String,nullable=False)
    email=Column(String,nullable=False,unique=True)
    hashed_password=Column(String,nullable=False)


class Campus(Base):
    __tablename__="campuses"

    id=Column(Integer,primary_key=True,nullable=False)
    name=Column(String,nullable=False)
    campus_code=Column(String,nullable=False,unique=True)
    address=Column(String,nullable=False)

    latitude = Column(
        FLOAT,
        nullable=False
    )

    longitude = Column(
        FLOAT,
        nullable=False
    )

    created_at=Column(
        DateTime,
        server_default=func.now(),
        nullable=False)


class Building(Base):
    __tablename__="buildings"

    id=Column(Integer,primary_key=True,nullable=False)
    building_name=Column(String,nullable=False)
    building_code=Column(String,nullable=False)
    latitude=Column(FLOAT,nullable=False)
    longitude=Column(FLOAT,nullable=False)
    campus_id=Column(Integer,ForeignKey("campuses.id"),nullable=False)


