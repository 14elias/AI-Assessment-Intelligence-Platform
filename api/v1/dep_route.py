from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from schema.dep_schema import CreateDep
from crud.dep_crud import create_departement, get_dep, get_all_dep
from db.session import get_db

router = APIRouter(tags=['departement'])


@router.post('/create_dep')
async def create_department(data: CreateDep, db: AsyncSession = Depends(get_db)):
    data = data.model_dump()
    new_dep = await create_departement(data, db)
    return new_dep


@router.get('/get_dep')
async def get_departement(name, db: AsyncSession = Depends(get_db)):
    return await get_dep(name, db)


@router.get('/get_all_dep')
async def get_all_departement(db: AsyncSession = Depends(get_db)):
    return await get_all_dep(db)


@router.delete('/get_all_dep')
async def delete_departement(name, db: AsyncSession = Depends(get_db)):
    return await get_all_dep(name, db)
