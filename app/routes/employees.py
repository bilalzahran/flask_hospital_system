from flask import request
from flask_restx import Resource, fields
from app.service.employees import (
    add_employee,
    delete_employee,
    get_all_employee,
    get_employee,
    update_employee,
)

from app.routes import api

employee_router = api.namespace("employees")
employee = employee_router.model(
    "employee",
    {
        "name": fields.String(required=True),
        "username": fields.String(required=True),
        "password": fields.String(required=True),
        "gender": fields.String(),
        "birthdate": fields.String(),
    },
)

employee_update = employee_router.model(
    "employee_update",
    {
        "name": fields.String(),
        "username": fields.String(),
        "password": fields.String(),
        "gender": fields.String(),
        "birthdate": fields.String(),
    },
)

employee_out = employee_router.model(
    "employee_out",
    {
        "id": fields.Integer(),
        "name": fields.String(),
        "username": fields.String(),
        "password": fields.String(),
        "gender": fields.String(),
        "birthdate": fields.String(),
    },
)


@employee_router.route("/")
class EmployeeList(Resource):
    @employee_router.doc("Get all employee")
    @employee_router.marshal_list_with(employee_out, envelope="data")
    def get(self):
        return get_all_employee()

    @employee_router.doc("Add new employee")
    @employee_router.response(201, "Employee successfully added.")
    @employee_router.expect(employee, validate=True)
    def post(self):
        data = request.json
        return add_employee(data)


@employee_router.route("/<employee_id>")
@api.param("employee_id", "The Employee identifier")
@employee_router.response(404, "Employee not found")
class Employee(Resource):
    @employee_router.doc("Get Employee")
    @employee_router.marshal_with(employee_out)
    def get(self, employee_id):
        employee = get_employee(employee_id)
        if employee:
            return employee
        else:
            employee_router.abort(404)

    @employee_router.response(204, "employee updated")
    @employee_router.expect(employee_update, validate=True)
    @employee_router.marshal_with(employee_out)
    def put(self, employee_id):
        data = request.json
        employee = get_employee(employee_id)
        if employee:
            return update_employee(employee_id, data)
        else:
            employee_router.abort(404)

    @employee_router.response(204, "employee deleted")
    def delete(self, employee_id):
        employee = get_employee(employee_id)
        if employee:
            return delete_employee(employee)
        else:
            employee_router.abort(404)
