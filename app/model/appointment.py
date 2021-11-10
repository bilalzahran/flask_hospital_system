from sqlalchemy.sql.schema import ForeignKey
from app.model import db
from enum import Enum


class AppointmentStatus(Enum):
    IN_QUEUE = "IN_QUEUE"
    DONE = "DONE"
    CANCELLED = "CANCELLED"


class Appointment(db.Model):
    __tablename__ = "appointments"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    doctor_id = db.Column(db.Integer, ForeignKey("doctors.id"))
    patient_id = db.Column(db.Integer, ForeignKey("patients.id"))
    datetime = db.Column(db.DateTime)
    status = db.Column(db.String)
    diagnose = db.Column(db.Text)
    notes = db.Column(db.Text)

    def __repr__(self):
        return "<Appointment %i>" % (self.id)
