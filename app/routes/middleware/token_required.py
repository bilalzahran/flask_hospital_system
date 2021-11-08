from functools import wraps
from typing import Callable
from flask import request
from app.service.employees import get_logged_in_employee


def token_required(func) -> Callable:
    @wraps(func)
    def check_token(*args, **kwargs):
        resp, status = get_logged_in_employee(request)
        data = resp.get("data")
        if not data:
            return resp, status

        return func(*args, **kwargs)

    return check_token
