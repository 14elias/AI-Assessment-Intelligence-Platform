from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from crud import topic_crud
from schema.topic_schema import CreateTopic
from db.session import get_db

router = APIRouter(tags=['topic'])

@router.post('/create_topic')
async def create_topic(data: CreateTopic, db: AsyncSession = Depends(get_db)):
    data = data.model_dump()

    topic = await topic_crud.create_topic(db=db, data=data)
    return topic 

@router.get('/get_topic')
async def get_topic(name: str, db: AsyncSession = Depends(get_db)):
    data = data.model_dump()

    topic = await topic_crud.get_topic(name=name, db=db)
    return topic


@router.get('/get_all_topic')
async def get_all_topic(db: AsyncSession = Depends(get_db)):
    return await topic_crud.get_all_topic(db)


@router.delete('/delete_topic')
async def delete_topic(name: str, db: AsyncSession = Depends(get_db)):
    return await topic_crud.delete_course(db=db, name=name)