from sqlalchemy import Column, Integer, String, Text, Date
from sqlalchemy.sql.functions import user
from . import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    username = Column(String)
    password = Column(Text)
    gender = Column(String)
    birthdate = Column(Date)

    def __init__(self, name: str, username: str, password: str, gender: str, birthdate: str):
        self.name = name
        self.username = username
        self.password = password
        self.gender = gender
        self.birthdate = birthdate

    def __repr__(self):
        return '<User %>' % (self.name)