from pydantic import BaseModel
from .course_schema import ResponseCourse


class CreateCourseOffering(BaseModel):
    department_id: int
    course_id: int
    academic_year_id: int
    semester_id: int

class CourseOfferingResponse(BaseModel):
    course:ResponseCourse