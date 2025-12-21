# app/db/init_db.py
import asyncio
from db.session import engine
import db.base_class 
from sqlalchemy import create_engine
from core.config import settings
from db.base import Base

sync_engine = create_engine(settings.DATABASE_SYNC_URL)



async def init_db():
    Base.metadata.drop_all(sync_engine)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(init_db())
