from app.model import db, bcrypt


class Doctors(db.Model):
    __tablename__ = "doctors"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    username = db.Column(db.String)
    password_hash = db.Column(db.Text)
    gender = db.Column(db.String)
    birthdate = db.Column(db.Date)
    work_start_time = db.Column(db.DateTime)
    work_end_time = db.Column(db.DateTime)

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def __repr__(self):
        return "<Doctors %s>" % (self.name)
