import sqlalchemy
from app.model.database.doctors import Doctors
from app.app import db
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime,date

def get_all_doctors():
  return Doctors.query.all()

def get_doctor(doctor_id):
  return Doctors.query.filter_by(id=doctor_id).first()

def add_doctor(data):
  # TODO: Add username validation
  try:
    new_doctor = Doctors(
      name=data['name'],
      username=data['username'],
      password=data['password'],
      gender=data['gender'],
      birthdate=date.strftime(data['birthdate']),
      work_start_time=datetime.strftime(data['work_start_time']),
      work_end_time=datetime.strftime(data['work_end_time'])
    )
    db.session.add(new_doctor)
    db.session.commit()
    response_object = {
      "status": "success",
      "message": "data successfuly created"
    }
    return response_object,201
  except SQLAlchemyError as ex:
    response_object = {
      "status": "fail",
      "message": "create new data failed"
    }
    return response_object, 202

def update_doctor(id, data):
  try:
    Doctors.query.filter_by(id=id).update(data)
    db.session.commit()
    return get_doctor(id)
  except SQLAlchemyError as ex:
    response_object = {
      "status": "fail",
      "message": "update doctor failed"
    }

    return response_object, 202

def delete_doctor(data):
  try:
    db.session.delete(data)
    db.session.commit()
  except SQLAlchemyError as ex:
    response_object = {
      "status": "fail",
      "message": "delete doctor failed"
    }

    return response_object, 202
