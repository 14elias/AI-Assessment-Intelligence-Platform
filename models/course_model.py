# app/models/course.py
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from db.base import Base

class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    department_id: Mapped[int] = mapped_column(
        ForeignKey("departments.id"), nullable=False
    )

    code: Mapped[str] = mapped_column(String(20), nullable=False)
    name: Mapped[str] = mapped_column(String(150), nullable=False)

    department: Mapped["Department"] = relationship(back_populates="courses")
    terms: Mapped[list["Term"]] = relationship(
        back_populates="course",
        cascade="all, delete-orphan"
    )

    __table_args__ = (
        # Prevent duplicate course codes inside the same department
        {"sqlite_autoincrement": True},
    )