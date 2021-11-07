from flask import Flask
from app.model import db, bcrypt
from app.routes import api
from app.routes.employees import employee_routes
from app.routes.doctors import doctor_routes
from app.routes.patients import patient_routes
from app.config import db_url

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = db_url
api.init_app(app)
db.init_app(app)
bcrypt.init_app(app)

api.add_namespace(employee_routes, path="/employee")
api.add_namespace(doctor_routes, path="/doctors")
api.add_namespace(patient_routes, path="/patients")

if __name__ == "__main__":
    app.run(debug=True)
