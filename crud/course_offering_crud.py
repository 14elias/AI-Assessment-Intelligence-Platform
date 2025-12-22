from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from models.course_offering_model import CourseOffering
from models import deps_model, course_model, academic_year_model, semister_model, topic_model

async def create_crofferings(data, db: AsyncSession):
    dep_id = data.get('department_id')
    academic_year_id = data.get('academic_year_id')
    course_id = data.get('course_id')
    semester_id = data.get('semester_id')

    stmt =select(CourseOffering).where(
        CourseOffering.department_id==dep_id,
        CourseOffering.academic_year_id==academic_year_id,
        CourseOffering.course_id==course_id,
        CourseOffering.semester_id==semester_id
    )
    result = await db.execute(stmt)

    if result.scalar_one_or_none():
        raise HTTPException(
            status_code=409,
            detail='course offering already exist'
        )
    
    stmt = (
        select(deps_model.Department)
        .where(deps_model.Department.id == dep_id)
    )
    result = await db.execute(stmt)
    if not result.scalar_one_or_none():
        raise HTTPException(
            status_code=404,
            detail='departement with this id not exist'
        )
    
    stmt = (
        select(course_model.Course)
        .where(course_model.Course.id == course_id)
    )
    result = await db.execute(stmt)
    if not result.scalar_one_or_none():
        raise HTTPException(
            status_code=404,
            detail='course with this id not exist'
        )
    
    stmt = (
        select(semister_model.Semester)
        .where(semister_model.Semester.id == semester_id)
    )
    result = await db.execute(stmt)
    if not result.scalar_one_or_none():
        raise HTTPException(
            status_code=404,
            detail='semester with this id not exist'
        )
    

    stmt = (
        select(academic_year_model.AcademicYear)
        .where(semister_model.Semester.id == academic_year_id)
    )
    result = await db.execute(stmt)
    if not result.scalar_one_or_none():
        raise HTTPException(
            status_code=404,
            detail='academic year with this id not exist'
        )
    
    course_offering= CourseOffering(**data)

    db.add(course_offering)
    await db.commit()
    await db.refresh(course_offering)

    return course_offering



async def get_all_course_offering(db: AsyncSession):
    stmt =(
        select(CourseOffering)
        .options(
            selectinload(CourseOffering.department),
            selectinload(CourseOffering.academic_year),
            selectinload(CourseOffering.semester),
            selectinload(CourseOffering.course),
        )
    )

    result = await db.execute(stmt)
    return result.scalars().all()


async def get_objectives(dep_id, academic_year_id, course_id, semester_id, db: AsyncSession):
    stmt = (
        select(CourseOffering)
        .where(
            CourseOffering.department_id == dep_id,
            CourseOffering.academic_year_id == academic_year_id,
            CourseOffering.course_id == course_id,
            CourseOffering.semester_id == semester_id
        )
        .options(
            selectinload(CourseOffering.course)
            .selectinload(course_model.Course.topics)
            .selectinload(topic_model.Topic.objectives)
        )
    )

    result = await db.execute(stmt)
    final_result = result.scalar_one_or_none()

    if not final_result:
        raise HTTPException(
            status_code=404,
            detail='not found'
        )
    return final_result