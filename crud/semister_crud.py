from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from models.semister_model import Semester


async def create_semister(name: str, db:AsyncSession):
    stmt = select(Semester).where(Semester.name == name)
    result = await db.execute(stmt)

    if result.scalar_one_or_none():
        raise HTTPException(
            status_code=409,
            detail='semister with this name already exist'
        )
    
    semister = Semester(name= name)
    db.add(semister)
    await db.commit()
    await db.refresh(semister)

    return semister

