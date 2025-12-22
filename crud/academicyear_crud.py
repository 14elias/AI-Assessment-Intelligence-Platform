from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

from models.academic_year_model import AcademicYear


async def create_academic_year(year: int, db: AsyncSession):
    stmt = select(AcademicYear).where(AcademicYear.year == year)
    result = await db.execute(stmt)

    if result.scalar_one_or_none():
        raise HTTPException(
            status_code=409, 
            detail='academic year already exist'
        )
    
    academic_year = AcademicYear(year=year)
    db.add(academic_year)
    await db.commit()
    await db.refresh(academic_year)

    return academic_year


async def get_year(year: int, db: AsyncSession):
    stmt = select(AcademicYear).where(AcademicYear.year == year)
    result = await db.execute(stmt)
    academic_year = result.scalar_one_or_none()

    if not academic_year:
        raise HTTPException(
            status_code=404, 
            detail='academic year not fund'
        )
    
    return academic_year