from flask import request
from flask_restx import Resource, fields
from app.routes import api
from app.service.patient import (
    get_patient,
    get_all_patient,
    delete_patient,
    add_patient,
    update_patient,
)

patient_routes = api.namespace("patients")

# TODO: refactor
patient = patient_routes.model(
    "patients",
    {
        "name": fields.String(required=True),
        "gender": fields.String(required=True),
        "birthdate": fields.String(required=True),
        "no_ktp": fields.String(required=True),
        "address": fields.String(required=True),
    },
)

patients_update = patient_routes.model(
    "patients_update",
    {
        "name": fields.String(),
        "gender": fields.String(),
        "birthdate": fields.String(),
        "no_ktp": fields.String(),
        "address": fields.String(),
    },
)

patients_out = patient_routes.model(
    "patients_out",
    {
        "id": fields.Integer(),
        "name": fields.String(),
        "gender": fields.String(),
        "birthdate": fields.String(),
        "no_ktp": fields.String(),
        "address": fields.String(),
        "vaccine_type": fields.String(),
        "vaccine_count": fields.Integer(),
    },
)


@patient_routes.route("/")
class PatientList(Resource):
    @patient_routes.doc("Get All Doctors")
    @patient_routes.marshal_list_with(patients_out, envelope="data")
    def get(self):
        return get_all_patient()

    @patient_routes.doc("Create new patient")
    @patient_routes.response(201, "patient successfully added.")
    @patient_routes.expect(patient, validate=True)
    def post(self):
        data = request.json
        return add_patient(data)


@patient_routes.route("/<patient_id>")
@api.param("patient_id", "the patient identifier")
@patient_routes.response(404, "patient not found")
class Patient(Resource):
    @patient_routes.doc("get patient")
    @patient_routes.marshal_with(patients_out)
    def get(self, patient_id):
        patient = get_patient(patient_id)
        if patient:
            return patient
        else:
            patient_routes.abort(404)

    @patient_routes.response(204, "patient updated")
    @patient_routes.expect(patients_update, validate=True)
    @patient_routes.marshal_with(patients_out)
    def put(self, patient_id):
        data = request.json
        patient = get_patient(patient_id)
        if patient:
            return update_patient(patient_id, data)
        else:
            patient_routes.abort(404)

    @patient_routes.response(204, "patient deleted")
    def delete(self, patient_id):
        patient = get_patient(patient_id)
        if patient:
            return delete_patient(patient)
        else:
            patient_routes.abort(404)
