from flask import Blueprint,make_response
from app.service.employees import get_all_data
employees_route = Blueprint('employees',__name__)

@employees_route.get('/')
def get_all():
    response = get_all_data()
    return make_response(
        response,
        201,
        'Application/json'
    )