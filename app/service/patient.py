import sqlalchemy
from app.model.database.patients import Patient
from app.app import db
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime,date

def get_all_patient():
  return Patient.query.all()

def get_patient(patient_id):
  return Patient.query.filter_by(id=patient_id).first()

def add_patient(data):
  # TODO: Add username validation
  try:
    new_patient = Patient(
      name=data['name'],
      gender=data['gender'],
      birthdate=data['birthdate'],
      no_ktp=data['no_ktp'],
      address=data['address'],      
    )
    db.session.add(new_patient)
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

def update_patient(id, data):
  try:
    Patient.query.filter_by(id=id).update(data)
    db.session.commit()
    return get_patient(id)
  except SQLAlchemyError as ex:
    response_object = {
      "status": "fail",
      "message": "update doctor failed"
    }

    return response_object, 202

def delete_patient(data):
  try:
    db.session.delete(data)
    db.session.commit()
  except SQLAlchemyError as ex:
    response_object = {
      "status": "fail",
      "message": "delete doctor failed"
    }

    return response_object, 202
