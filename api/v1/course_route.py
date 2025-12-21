from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from crud import course_crud
from schema.course_schema import CreateCourse
from db.session import get_db

router = APIRouter(tags=['course'])

@router.post('/create_course')
async def create_course(data: CreateCourse, db: AsyncSession = Depends(get_db)):
    data = data.model_dump()

    course = await course_crud.create_course(db=db, data=data)
    return course 

@router.get('/get_course')
async def get_course(name: str, db: AsyncSession = Depends(get_db)):
    data = data.model_dump()

    course = await course_crud.get_course(name=name, db=db)
    return course


@router.get('/get_all_course')
async def get_course(db: AsyncSession = Depends(get_db)):
    return await course_crud.get_all_courses(db)


@router.delete('/delete_course')
async def get_course(name: str, db: AsyncSession = Depends(get_db)):
    return await course_crud.delete_course(db=db, name=name)