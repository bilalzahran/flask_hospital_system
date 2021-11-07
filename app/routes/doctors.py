from flask import request
from flask_restx import Resource, fields
from app.routes import api
from app.service.doctors import (
    delete_doctor,
    get_all_doctors,
    add_doctor,
    get_doctor,
    update_doctor,
)

doctor_routes = api.namespace("doctors")

# TODO: refactor
doctor = doctor_routes.model(
    "doctor",
    {
        "name": fields.String(required=True),
        "username": fields.String(required=True),
        "password": fields.String(required=True),
        "gender": fields.String(required=True),
        "birthdate": fields.String(required=True),
        "work_start_time": fields.String(required=True),
        "work_end_time": fields.String(required=True),
    },
)

doctor_update = doctor_routes.model(
    "doctor_update",
    {
        "name": fields.String(),
        "username": fields.String(),
        "password": fields.String(),
        "gender": fields.String(),
        "birthdate": fields.String(),
        "work_start_time": fields.String(),
        "work_end_time": fields.String(),
    },
)

doctor_out = doctor_routes.model(
    "doctor_out",
    {
        "id": fields.Integer(),
        "name": fields.String(),
        "username": fields.String(),
        "password": fields.String(),
        "gender": fields.String(),
        "birthdate": fields.String(),
        "work_start_time": fields.String(),
        "work_end_time": fields.String(),
    },
)


@doctor_routes.route("/")
class DoctorList(Resource):
    @doctor_routes.doc("Get All Doctors")
    @doctor_routes.marshal_list_with(doctor_out, envelope="data")
    def get(self):
        return get_all_doctors()

    @doctor_routes.doc("Create new doctor")
    @doctor_routes.response(201, "Doctor successfully added.")
    @doctor_routes.expect(doctor, validate=True)
    def post(self):
        data = request.json
        return add_doctor(data)


@doctor_routes.route("/<doctor_id>")
@api.param("doctor_id", "the doctor identifier")
@doctor_routes.response(404, "doctor not found")
class Doctor(Resource):
    @doctor_routes.doc("get doctor")
    @doctor_routes.marshal_with(doctor_out)
    def get(self, doctor_id):
        doctor = get_doctor(doctor_id)
        if doctor:
            return doctor
        else:
            doctor_routes.abort(404)

    @doctor_routes.response(204, "employee updated")
    @doctor_routes.expect(doctor_update, validate=True)
    @doctor_routes.marshal_with(doctor_out)
    def put(self, doctor_id):
        data = request.json
        employee = get_doctor(doctor_id)
        if employee:
            return update_doctor(doctor_id, data)
        else:
            doctor_routes.abort(404)

    @doctor_routes.response(204, "employee deleted")
    def delete(self, doctor_id):
        doctor = get_doctor(doctor_id)
        if doctor:
            return delete_doctor(doctor)
        else:
            doctor_routes.abort(404)
