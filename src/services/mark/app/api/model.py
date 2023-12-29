from pydantic import BaseModel

class MarkAttendanceModel(BaseModel):
    date: str
    attendance: list