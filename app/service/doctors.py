from app.model.doctors import Doctors
from app.app import db
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime, time


def get_all_doctors():
    return Doctors.query.all()


def get_doctor(doctor_id):
    return Doctors.query.filter_by(id=doctor_id).first()


def add_doctor(data):
    try:
        if Doctors.query.filter_by(username=data["username"]).first():
            response_object = {"status": "fail", "message": "username already exist!"}
            return response_object, 202

        new_doctor = Doctors(
            name=data["name"],
            username=data["username"],
            password=data["password"],
            gender=data["gender"],
            birthdate=datetime.strptime(data["birthdate"], "%Y-%m-%d"),
            work_start_time=datetime.strptime(data["work_start_time"], "%H:%M:%S"),
            work_end_time=datetime.strptime(data["work_end_time"], "%H:%M:%S"),
        )
        db.session.add(new_doctor)
        db.session.commit()
        response_object = {
            "name": new_doctor.name,
            "username": new_doctor.username,
            "password": new_doctor.password,
            "gender": new_doctor.gender,
            "birthdate": datetime.strftime(new_doctor.birthdate, "%Y-%m-%d"),
            "work_start_time": time.strftime(new_doctor.work_start_time, "%H:%M:%S"),
            "work_end_time": time.strftime(new_doctor.work_end_time, "%H:%M:%S"),
        }
        return response_object, 201
    except SQLAlchemyError as ex:
        response_object = {"status": "fail", "message": "create new data failed"}
        return response_object, 202


def update_doctor(id, data):
    try:
        Doctors.query.filter_by(id=id).update(data)
        db.session.commit()
        return get_doctor(id)
    except SQLAlchemyError as ex:
        response_object = {"status": "fail", "message": "update doctor failed"}

        return response_object, 202


def delete_doctor(data):
    try:
        db.session.delete(data)
        db.session.commit()
    except SQLAlchemyError as ex:
        print(ex)
        response_object = {"status": "fail", "message": "delete doctor failed"}

        return response_object, 202
