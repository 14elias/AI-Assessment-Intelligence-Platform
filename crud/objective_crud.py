from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import objective_model, topic_model

async def create_objective(db: AsyncSession, data):
    stmt = select(topic_model.Topic).where(topic_model.Topic.id == data.get('topic_id'))
    result = await db.execute(stmt)

    if not result.scalar_one_or_none():
        raise HTTPException(
            status_code=404, 
            detail='topic with the given id not exist'
        )
    objective = objective_model.Objective(**data)
    db.add(objective)
    await db.commit()
    await db.refresh(objective)

    return objective


async def get_all_objectives(db: AsyncSession):
    try:
        result = await db.execute(select(objective_model.Objective))
        objectives = result.scalars().all()

        return objectives
    except Exception as e:
        return f'the error is {e}'
    

async def delete_objective(id:int, db: AsyncSession):
    stmt = select(objective_model.Objective).where(objective_model.Objective.id == id)
    result = await db.execute(stmt)

    existing_objective = result.scalar_one_or_none()
    if not existing_objective:
        raise HTTPException(
            status_code=404, 
            detail='objective not exist'
        )
    await db.delete(existing_objective)
    await db.commit()

    return f'deleted objectie: {existing_objective}'
