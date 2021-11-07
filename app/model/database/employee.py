from app.model.database import db


class Employee(db.Model):
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    username = db.Column(db.String)
    password = db.Column(db.Text)
    gender = db.Column(db.String)
    birthdate = db.Column(db.Date)

    def __repr__(self):
        return "<User %>" % (self.name)
