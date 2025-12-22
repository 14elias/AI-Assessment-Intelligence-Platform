from pydantic import BaseModel


class CreateObjective(BaseModel):
    topic_id: int
    description: str

class ResponseObjective(BaseModel):
    description: str