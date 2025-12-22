from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import get_db
from crud import semister_crud
router = APIRouter(tags=['semister'])

@router.post('/create_semister')
async def create_semister(name: str, db: AsyncSession = Depends(get_db)):
    return await semister_crud.create_semister(name=name, db=db)