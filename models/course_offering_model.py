from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from db.base import Base


class CourseOffering(Base):
    __tablename__ = "course_offerings"

    id: Mapped[int] = mapped_column(primary_key=True)

    department_id: Mapped[int] = mapped_column(
        ForeignKey("departments.id"), nullable=False
    )
    course_id: Mapped[int] = mapped_column(
        ForeignKey("courses.id"), nullable=False
    )
    academic_year_id: Mapped[int] = mapped_column(
        ForeignKey("academic_years.id"), nullable=False
    )
    semester_id: Mapped[int] = mapped_column(
        ForeignKey("semesters.id"), nullable=False
    )

    department: Mapped["Department"] = relationship(back_populates="offerings")
    course: Mapped["Course"] = relationship(back_populates="offerings")
    academic_year: Mapped["AcademicYear"] = relationship(back_populates="offerings")
    semester: Mapped["Semester"] = relationship(back_populates="offerings")
