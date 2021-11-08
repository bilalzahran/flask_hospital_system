from flask import request
from flask_restx import Resource, fields
from app.service.employees import (
    add_employee,
    delete_employee,
    get_all_employee,
    get_employee,
    update_employee,
    employee_login,
)
from app.routes.middleware.token_required import token_required

from app.routes import api

employee_routes = api.namespace("employees")
employee = employee_routes.model(
    "employee",
    {
        "name": fields.String(required=True),
        "username": fields.String(required=True),
        "password": fields.String(required=True),
        "gender": fields.String(),
        "birthdate": fields.String(),
    },
)

employee_update = employee_routes.model(
    "employee_update",
    {
        "name": fields.String(),
        "username": fields.String(),
        "password": fields.String(),
        "gender": fields.String(),
        "birthdate": fields.String(),
    },
)

employee_out = employee_routes.model(
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

employee_signin = employee_routes.model(
    "employee_login",
    {
        "username": fields.String(required=True),
        "password": fields.String(required=True),
    },
)


@employee_routes.route("/")
class EmployeeList(Resource):
    @employee_routes.doc("Get all employee")
    @token_required
    @employee_routes.marshal_list_with(employee_out, envelope="data")
    def get(self):
        return get_all_employee()

    @employee_routes.doc("Add new employee")
    @token_required
    @employee_routes.response(201, "Employee successfully added.")
    @employee_routes.expect(employee, validate=True)
    def post(self):
        data = request.json
        return add_employee(data)


@employee_routes.route("/<employee_id>")
@api.param("employee_id", "The Employee identifier")
@employee_routes.response(404, "Employee not found")
class Employee(Resource):
    @employee_routes.doc("Get Employee")
    @employee_routes.marshal_with(employee_out)
    @token_required
    def get(self, employee_id):
        employee = get_employee(employee_id)
        if employee:
            return employee
        else:
            employee_routes.abort(404)

    @employee_routes.response(204, "employee updated")
    @employee_routes.expect(employee_update, validate=True)
    @employee_routes.marshal_with(employee_out)
    @token_required
    def put(self, employee_id):
        data = request.json
        employee = get_employee(employee_id)
        if employee:
            return update_employee(employee_id, data)
        else:
            employee_routes.abort(404)

    @employee_routes.response(204, "employee deleted")
    @token_required
    def delete(self, employee_id):
        employee = get_employee(employee_id)
        if employee:
            return delete_employee(employee)
        else:
            employee_routes.abort(404)


@employee_routes.route("/login")
class EmployeeAuth(Resource):
    @employee_routes.expect(employee_signin, validate=True)
    def post(self):
        payload = request.json
        return employee_login(payload)
