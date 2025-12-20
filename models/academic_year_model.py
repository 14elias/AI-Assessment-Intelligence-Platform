from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer
from db.base import Base


class AcademicYear(Base):
    __tablename__ = "academic_years"

    id: Mapped[int] = mapped_column(primary_key=True)
    year: Mapped[int] = mapped_column(Integer, nullable=False)  
    # 1 = freshman, 2 = sophomore, etc.

    offerings: Mapped[list["CourseOffering"]] = relationship(
        back_populates="academic_year"
    )
 