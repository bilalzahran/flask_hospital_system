from app.model.appointment import Appointment
from app.model.doctors import Doctors
from app.app import db
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime, time
from sqlalchemy import func


def get_all_appointment():
    return Appointment.query.all()


def get_appointment(id):
    return Appointment.query.filter_by(id=id).first()


def add_appointment(payload):
    try:
        doctor = Doctors.query.filter_by(id=payload["doctor_id"]).first()
        patient_time = datetime.strptime(payload["datetime"], "%Y-%m-%d %H:%M:%S")
        appointment = (
            Appointment.query.filter(Appointment.doctor_id == payload["doctor_id"])
            .filter(func.date(Appointment.datetime) == patient_time.date())
            .filter(Appointment.status == "IN_QUEUE")
            .count()
        )
        print(
            patient_time.time() >= doctor.work_start_time
            and patient_time.time() <= doctor.work_end_time
        )

        """Check appointment is still exist"""
        if appointment > 0:
            response_object = {"status": "fail", "message": "Appointment is full "}
            return response_object, 202

        """Check doctor are available at given datetime"""
        if (
            patient_time.time() >= doctor.work_start_time
            and patient_time.time() <= doctor.work_end_time
        ):
            new_appointment = Appointment(
                doctor_id=payload["doctor_id"],
                patient_id=payload["patient_id"],
                datetime=patient_time,
                status=payload["status"],
                diagnose=payload["diagnose"],
                notes=payload["notes"],
            )
            db.session.add(new_appointment)
            db.session.commit()
            return payload, 201

        response_object = {"status": "fail", "message": "Out of doctor schedule"}
        return response_object, 202

    except SQLAlchemyError as ex:
        print(ex)
        response_object = {"status": "fail", "message": "create new data failed"}
        return response_object, 202


def update_appointment(id, data):
    try:
        Appointment.query.filter_by(id=id).update(data)
        db.session.commit()
        return get_appointment(id)
    except SQLAlchemyError as ex:
        response_object = {"status": "fail", "message": "update doctor failed"}

        return response_object, 202


def delete_appointment(data):
    try:
        db.session.delete(data)
        db.session.commit()
    except SQLAlchemyError as ex:
        print(ex)
        response_object = {"status": "fail", "message": "delete doctor failed"}

        return response_object, 202
