from pydantic import BaseModel
from .topic_schema import ResponseTopic


class CreateCourse(BaseModel):
    name: str
    code:str

class ResponseCourse(BaseModel):
    id: int
    name: str
    topics:list[ResponseTopic]