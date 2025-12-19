# app/models/course.py
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from db.base import Base

class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(20), unique=True)
    name: Mapped[str] = mapped_column(String(150))

    topics: Mapped[list["Topic"]] = relationship(
        back_populates="course",
        cascade="all, delete-orphan"
    )

    offerings: Mapped[list["CourseOffering"]] = relationship(
        back_populates="course"
    )


    __table_args__ = (
        # Prevent duplicate course codes inside the same department
        {"sqlite_autoincrement": True},
    )