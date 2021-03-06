from operator import add
from app.model import db


class Patient(db.Model):
    __tablename__ = "patients"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    gender = db.Column(db.String)
    birthdate = db.Column(db.Date)
    no_ktp = db.Column(db.String)
    address = db.Column(db.Text)
    vaccine_type = db.Column(db.String)
    vaccine_count = db.Column(db.Integer)

    def __init__(self, name, gender, birthdate, no_ktp, address):
        self.name = name
        self.gender = gender
        self.birthdate = birthdate
        self.no_ktp = no_ktp
        self.address = address

    def __repr__(self):
        return "<Post: %r>" % (self.name)
