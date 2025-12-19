# app/models/topic.py
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from db.base import Base

class Topic(Base):
    __tablename__ = "topics"

    id: Mapped[int] = mapped_column(primary_key=True)
    course_id: Mapped[int] = mapped_column(
        ForeignKey("courses.id"), nullable=False
    )
    name: Mapped[str] = mapped_column(String(150))

    course: Mapped["Course"] = relationship(back_populates="topics")
    objectives: Mapped[list["Objective"]] = relationship(
        back_populates="topic",
        cascade="all, delete-orphan"
    )

