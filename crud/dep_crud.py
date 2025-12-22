from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

from models import deps_model


async def create_departement(data, db: AsyncSession):
    stmt =select(deps_model.Department).where(deps_model.Department.name == data.get('name'))
    result = await  db.execute(stmt)

    if result.scalar_one_or_none():
        raise HTTPException(status_code=409, detail='departement already exist')
    department = deps_model.Department(**data)

    try:
        db.add(department)
        await db.commit()
        await db.refresh(department)
        return department
    except Exception as e:
        await db.rollback()
        raise e


async def get_dep(name_dep, db: AsyncSession):
    stmt = (
        select(deps_model.Department)
        .where(deps_model.Department.name == name_dep)
    )
    result = await db.execute(stmt)
    existing_dep = result.scalars().first()

    if not existing_dep:
        raise HTTPException(
            status_code=404, 
            detail='departement with this name not exist'
        )
    return existing_dep


async def get_all_dep(db: AsyncSession):
    result = await db.execute(select(deps_model.Department))
    existing_dep = result.scalars().all()

    return existing_dep
    

async def delete_dep(name_dep, db: AsyncSession):
    stmt = (
        select(deps_model.Department)
        .where(deps_model.Department.name == name_dep)
    )
    result = await db.execute(stmt)

    existing_dep = result.scalars().first()

    if not existing_dep:
        raise HTTPException(
            status_code=404, 
            detail='departement with this name not exist'
        )
    await db.delete(existing_dep)
    await db.commit()

    return (f'deleted departement: {existing_dep}')