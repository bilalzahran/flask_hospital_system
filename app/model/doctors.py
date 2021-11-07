from app.model import db


class Doctors(db.Model):
    __tablename__ = "doctors"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    username = db.Column(db.String)
    password = db.Column(db.Text)
    gender = db.Column(db.String)
    birthdate = db.Column(db.Date)
    work_start_time = db.Column(db.DateTime)
    work_end_time = db.Column(db.DateTime)

    def __init__(
        self,
        name,
        username,
        password,
        gender,
        birthdate,
        work_start_time,
        work_end_time,
    ):
        self.name = name
        self.username = username
        self.password = password
        self.gender = gender
        self.birthdate = birthdate
        self.work_start_time = work_start_time
        self.work_end_time = work_end_time

    def __repr__(self):
        return "<Doctors %s>" % (self.name)
