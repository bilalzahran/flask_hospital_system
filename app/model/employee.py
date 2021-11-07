from enum import unique
from app.model import db, bcrypt
import jwt


class Employee(db.Model):
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    username = db.Column(db.String, unique=True)
    password_hash = db.Column(db.String(100))
    gender = db.Column(db.String)
    birthdate = db.Column(db.Date)

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User %>" % (self.name)
