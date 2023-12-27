from pydantic import BaseModel

class Student(BaseModel):
    role_id: str
    name: str
    photoid_url: str
