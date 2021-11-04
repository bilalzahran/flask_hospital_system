from flask import Flask
from app.database import db_session
from app.routes.employees import employees_route
app = Flask(__name__)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

app.register_blueprint(employees_route)