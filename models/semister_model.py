# app/models/term.py
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from db.base import Base

class Semester(Base):
    __tablename__ = "semesters"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))  
    # "Fall", "Spring"

    offerings: Mapped[list["CourseOffering"]] = relationship(
        back_populates="semester"
    )

