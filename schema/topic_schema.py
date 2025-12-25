from pydantic import BaseModel
from .objective_schema import ResponseObjective


class CreateTopic(BaseModel):
    name:str
    course_id:int

class ResponseTopic(BaseModel):
    id:int
    name:str
    objectives:list[ResponseObjective]