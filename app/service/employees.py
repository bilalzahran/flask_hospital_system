from flask_sqlalchemy import SQLAlchemy
from app.model.database import employee
from app.model.database.employee import Employee
from app.app import db
from sqlalchemy.exc import SQLAlchemyError


def get_all_employee():
    return Employee.query.all()


def get_employee(employee_id):
    return Employee.query.filter_by(id=employee_id).first()


def add_employee(data):
    try:
        new_employee = Employee(
            name=data["name"],
            username=data["username"],
            password=data["password"],
            gender=data["gender"],
            birthdate=data["birthdate"],
        )
        db.session.add(new_employee)
        db.session.commit()
        response_object = {
            "status": "success",
            "message": "successfuly created",
        }
        return response_object, 201
    except SQLAlchemyError as ex:
        response_object = {
            "status": "fail",
            "message": "create new data failed",
        }
        return response_object, 202


def update_employee(id, data):
    try:
        employee = Employee.query.filter_by(id=id).update(data)
        db.session.commit()
        return get_employee(id)
    except SQLAlchemyError as ex:
        response_object = {
            "status": "fail",
            "message": "udpate employee failed",
        }
        return response_object, 202


def delete_employee(data):
    try:
        db.session.delete(data)
        db.session.commit()
    except SQLAlchemyError as ex:
        response_object = {
            "status": "fail",
            "message": "delete employee failed",
        }
        return response_object, 202
