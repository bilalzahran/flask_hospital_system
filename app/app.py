from flask import Flask
from app.model.database import db
from app.routes import api
from app.routes.employees import employee_router
from app.config import db_url

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = db_url
api.init_app(app)
db.init_app(app)

api.add_namespace(employee_router, path="/employee")

if __name__ == "__main__":
    app.run(debug=True)
