# app/models/objective.py
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Text, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from db.base import Base

class Objective(Base):
    __tablename__ = "objectives"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    topic_id: Mapped[int] = mapped_column(
        ForeignKey("topics.id"), nullable=False
    )
    description: Mapped[str] = mapped_column(Text, nullable=False)

    topic: Mapped["Topic"] = relationship(back_populates="objectives")
