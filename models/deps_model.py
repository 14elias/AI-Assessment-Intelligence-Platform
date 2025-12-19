# app/models/department.py
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase
from db.base import Base

class Department(Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)

    offerings: Mapped[list["CourseOffering"]] = relationship(
        back_populates="department",
        cascade="all, delete-orphan"
    )

