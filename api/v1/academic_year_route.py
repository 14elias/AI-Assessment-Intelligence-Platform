from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from crud import academicyear_crud
from db.session import get_db

router = APIRouter(tags=['academicyear'])

@router.post('/create_ayear')
async def create_academic_year(year: int, db: AsyncSession = Depends(get_db)):
    return await academicyear_crud.create_academic_year(year=year, db=db)

@router.get('/get_academic_year')
async def get_academic_year(year: int, db: AsyncSession = Depends(get_db)):
    return await academicyear_crud.get_year(year=year, db= db)