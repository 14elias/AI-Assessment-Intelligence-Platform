from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import get_db
from crud import course_offering_crud
from schema.course_offering_schema import CreateCourseOffering, CourseOfferingResponse


router = APIRouter(tags=['course_offerings'])

@router.post('/create_course_offering')
async def create_course_offering(data: CreateCourseOffering, db: AsyncSession = Depends(get_db)):
    data = data.model_dump()

    return await course_offering_crud.create_crofferings(data=data, db=db)

@router.get('/get_all_course_offering')
async def get_all_course_offering(db: AsyncSession = Depends(get_db)):
    return await course_offering_crud.get_all_course_offering(db)


@router.get('/get_course_offering', response_model=CourseOfferingResponse)
async def get_course_offering(
    course_id, 
    dep_id, 
    academic_year_id, 
    semester_id, 
    db: AsyncSession = Depends(get_db)
):
    return await course_offering_crud.get_objectives(
        dep_id = dep_id, 
        course_id = course_id,
        academic_year_id = academic_year_id,
        semester_id = semester_id, 
        db=db
    )