from typing import List
from app.database import db_session
from app.model.postgresql import employee
from app.model.postgresql.employee import Employee
from sqlalchemy.exc import SQLAlchemyError

class EmployeeRepository:        
    def get_all(self):
        try:           
            users = db_session.query(Employee).all()
            return users
        except SQLAlchemyError as ex:
            print(ex)
    
    def get_one(self, emp_id):
        try:           
            return db_session.query(Employee).filter(Employee.id == emp_id)
        except SQLAlchemyError as ex:
            print(ex)

    def insert(self, payload: Employee):
        try:           
            db_session.add(payload)
            response = db_session.commit()
            return response
        except SQLAlchemyError as ex:
            db_session.rollback()
        finally:
            db_session.commit()

    def update(self, payload: Employee, emp_id):
        try:           
            employee = db_session.query(Employee).filter(Employee.id == emp_id)
            employee.update(payload)
            db_session.commit()
        except SQLAlchemyError as ex:
            db_session.rollback()            
        finally:
            db_session.commit()

    def delete(self, emp_id):
        try:           
            employee = db_session.query(Employee).filter(Employee.id == id)
            db_session.delete(employee)
        except SQLAlchemyError as ex:
            db_session.rollback()
        finally:
            db_session.commit()