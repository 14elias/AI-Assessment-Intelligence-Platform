from pydantic import BaseModel



class CreateTopic(BaseModel):
    name:str
    course_id:int
