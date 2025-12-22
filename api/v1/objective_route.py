from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from crud import objective_crud
from db.session import get_db
from schema.objective_schema import CreateObjective


router = APIRouter(tags=['objectives'])

@router.post('/create_objective')
async def create_objective(data: CreateObjective, db: AsyncSession = Depends(get_db)):
    data = data.model_dump()
    objective = await objective_crud.create_objective(db=db, data=data)
    return objective

@router.get('/get_all_objective')
async def get_all_objective(db: AsyncSession = Depends(get_db)):
    return await objective_crud.get_all_objectives(db)


@router.delete('/delete_objective')
async def delete_objective(obj_id: int, db: AsyncSession = Depends(get_db)):
    return await objective_crud.delete_objective(id=obj_id, db=db)