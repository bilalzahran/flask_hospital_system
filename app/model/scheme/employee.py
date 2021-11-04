from pydantic import BaseModel

class EmployeeOut(BaseModel):
    id: str
    name: str
    username: str
    gender: str
    birthdate: str