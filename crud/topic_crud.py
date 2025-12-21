from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

from models import topic_model, course_model



async def create_topic(data, db: AsyncSession):
    stmt = select(topic_model.Topic).where(topic_model.Topic.name == data.get('name'))
    result = await  db.execute(stmt)

    if result.scalar_one_or_none():
        raise HTTPException(status_code=409, detail='departement already exist')
    
    stmt = select(course_model.Course).where(course_model.Course.id == data.get('course_id'))
    result = await db.execute(stmt)

    if not result.scalar_one_or_none():
        raise HTTPException(status_code=409, detail='course not exist')

    topic = topic_model.Topic(**data)

    try:
        db.add(topic)
        await db.commit()
        await db.refresh(topic)
        return topic
    except Exception as e:
        await db.rollback()
        raise e


async def get_topic(name_topic, db: AsyncSession):
    stmt = (
        select(topic_model.Topic)
        .where(topic_model.Topic.name == name_topic)
    )
    result = await db.execute(stmt)
    existing_topic = result.scalars().first()

    if not existing_topic:
        raise HTTPException(
            status_code=404, 
            detail='topic with this name not exist'
        )
    return existing_topic


async def get_all_topic(db: AsyncSession):
    result = await db.execute(select(topic_model.Topic))
    existing_topic = result.scalars().all()

    return existing_topic
    

async def delete_topic(name_topic, db: AsyncSession):
    stmt = (
        select(topic_model.Topic)
        .where(topic_model.Topic.name == name_topic)
    )
    result = await db.execute(stmt)

    existing_topic = result.scalars().first()

    if not existing_topic:
        raise HTTPException(
            status_code=404, 
            detail='departement with this name not exist'
        )
    await db.delete(existing_topic)
    await db.commit()

    return (f'deleted departement: {existing_topic}')