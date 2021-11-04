from sqlalchemy import Column, String, Integer, Text, Date, DateTime
from . import Base

class Doctors(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    password = Column(Text)
    gender = Column(String)
    birthdate = Column(Date)
    work_start_time = Column(DateTime)
    work_end_time = Column(DateTime)
