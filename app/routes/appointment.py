from flask import app, request
from flask_restx import Resource, fields
from app.routes import api
from app.service.appointment import (
    add_appointment,
    get_all_appointment,
    get_appointment,
    delete_appointment,
)
from app.routes.middleware.token_required import token_required

appointment_routes = api.namespace("appointments")

appointment = appointment_routes.model(
    "appointment",
    {
        "patient_id": fields.Integer(required=True),
        "doctor_id": fields.Integer(required=True),
        "datetime": fields.String(required=True),
        "status": fields.String(required=True),
        "diagnose": fields.String(),
        "notes": fields.String(),
    },
)

appointment_out = appointment_routes.model(
    "appointment",
    {
        "id": fields.Integer(),
        "patient_id": fields.Integer(),
        "doctor_id": fields.Integer(),
        "datetime": fields.String(),
        "status": fields.String(),
        "diagnose": fields.String(),
        "notes": fields.String(),
    },
)


@appointment_routes.route("/")
class AppointmentList(Resource):
    @appointment_routes.doc("Get all appointments")
    @appointment_routes.marshal_list_with(appointment_out, envelope="data")
    @token_required
    def get(self):
        return get_all_appointment()

    @appointment_routes.doc("Create New Appointment")
    @appointment_routes.response(201, "Appointment has been created")
    @appointment_routes.expect(appointment, validate=True)
    @token_required
    def post(self):
        payload = request.json
        return add_appointment(payload)


@appointment_routes.route("/<appointment_id>")
class Appointment(Resource):
    @appointment_routes.response(204, "employee deleted")
    @token_required
    def delete(self, appointment_id):
        appointment = get_appointment(appointment_id)
        if appointment:
            return delete_appointment(appointment)
        else:
            appointment_routes.abort(404)
