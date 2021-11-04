from sqlalchemy import Column, Integer, String, Text, Date
from . import Base

class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    gender = Column(String)
    birthdate = Column(Date)
    no_ktp = Column(String)
    address = Column(Text)
    vaccine_type = Column(String)
    vaccine_count = Column(Integer)

