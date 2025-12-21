from pydantic import BaseModel



class CreateCourse(BaseModel):
    name: str
    code:str