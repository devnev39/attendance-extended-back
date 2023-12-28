from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    role_id: str
    name: str
    photoid_url: str
    encoding: Optional[list] = None
