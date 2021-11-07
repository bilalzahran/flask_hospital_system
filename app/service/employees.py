from flask_sqlalchemy import SQLAlchemy
from app.model.employee import Employee
from app.app import db
from app.utils.jwt_helper import encode_token
from sqlalchemy.exc import SQLAlchemyError


def get_all_employee():
    return Employee.query.all()


def get_employee(employee_id):
    return Employee.query.filter_by(id=employee_id).first()


def add_employee(data):
    # TODO: username validation
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
        Employee.query.filter_by(id=id).update(data)
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


def employee_login(data):
    try:
        employee: Employee = Employee.query.filter_by(username=data["username"]).first()
        if employee:
            if employee.check_password(data["password"]):
                token = encode_token(employee.id)
                if token:
                    response_object = {
                        "status": "success",
                        "message": "login success",
                        "authorization": token,
                    }
                    return response_object, 200
            else:
                response_object = {
                    "status": "fail",
                    "message": "username or password invalid",
                }
                return response_object, 401
        else:
            response_object = {
                "status": "fail",
                "message": "cant find any credentials",
            }
            return response_object, 401
    except Exception as ex:
        response_object = {
            "status": "fail",
            "message": "something went wrong, try again",
        }

        return response_object, 500
