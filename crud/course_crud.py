from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException

from models.course_model import Course

async def create_course(data, db: AsyncSession):
    stmt = select(Course).where(Course.name == data.get('name'))
    result = await db.execute(stmt)

    if result.scalar_one_or_none():
        raise HTTPException(
            status_code=409, 
            detail='course with this name already exists'
        )
    
    course = Course(**data)

    db.add(course)
    await db.commit()
    await db.refresh(course)

    return course


async def get_course(name, db: AsyncSession):
    stmt = select(Course).where(Course.name == 'name')
    result = await db.execute(stmt)

    existing_course = result.scalar_one_or_none()
    if not existing_course:
        raise HTTPException(
            status_code=404, 
            detail='course with this name not exists'
        )
    return existing_course

async def get_all_courses(db: AsyncSession):
    result = await db.execute(select(Course))
    courses = result.scalars().all()

    return courses


async def delete_course(name, db: AsyncSession):
    stmt = (
        select(Course)
        .where(Course.name == name)
    )
    result = await db.execute(stmt)

    existing_course = result.scalars().first()

    if not existing_course:
        raise HTTPException(
            status_code=404, 
            detail='coursse with this name not exist'
        )
    await db.delete(existing_course)
    await db.commit()

    return (f'deleted course: {existing_course}')