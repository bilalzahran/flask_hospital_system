from flask import request
from app.model.employee import Employee
from app.app import db
from app.utils.jwt_helper import encode_token, decode_token
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime


def get_all_employee():
    return Employee.query.all()


def get_employee(employee_id):
    return Employee.query.filter_by(id=employee_id).first()


def add_employee(data):
    try:
        """ "Check if username exist in database"""
        if Employee.query.filter_by(username=data["username"]).count() >= 1:
            response_object = {"status": "fail", "message": "username already exist!"}
            return response_object, 202

        new_employee = Employee(
            name=data["name"],
            username=data["username"],
            password=data["password"],
            gender=data["gender"],
            birthdate=datetime.strptime(data["birthdate"], "%Y-%m-%d"),
        )
        db.session.add(new_employee)
        db.session.commit()
        response_object = {
            "name": new_employee.name,
            "username": new_employee.username,
            "password": new_employee.password,
            "gender": new_employee.gender,
            "birthdate": datetime.strftime(new_employee.birthdate, "%Y-%m-%d"),
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


def get_logged_in_employee(payload):
    token = payload.headers.get("Authorization")
    if token:
        data = decode_token(token)
        if not isinstance(data, str):
            employee_data: Employee = Employee.query.filter_by(id=data["iss"]).first()
            response_object = {
                "status": "success",
                "data": {
                    "id": employee_data.id,
                    "username": employee_data.username,
                },
            }
            return response_object, 200
        else:
            response_object = {
                "status": "fail",
                "message": data,
            }
            return response_object, 401

    else:
        response_object = {"status": "fail", "message": "token is missing"}
        return response_object, 401
