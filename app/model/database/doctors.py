from app.model.database import db


class Doctors(db.Model):
    __tablename__ = "doctors"

    id = db.Model(db.Integer, primary_key=True, autoincrement=True)
    name = db.Model(db.String)
    username = db.Model(db.String)
    password = db.Model(db.Text)
    gender = db.Model(db.String)
    birthdate = db.Model(db.Date)
    work_start_time = db.Model(db.Datetime)
    work_end_time = db.Model(db.Datetime)

    def __init__(
        self,
        name,
        username,
        password,
        gender,
        birthdate,
        work_start_time,
        work_end_stime,
    ):
        self.name = name
        self.username = username
        self.password = password
        self.gender = gender
        self.birthdate = birthdate
        self.work_start_time = work_start_time
        self.work_end_time = work_end_stime

    def __repr__(self):
        return "<Doctors %s>" % (self.name)
