from app.repository.employee_repo import EmployeeRepository
from app.model.scheme.employee import EmployeeOut

def get_all_data():
    employee_repo = EmployeeRepository()
    employees = employee_repo.get_all()
    return (EmployeeOut(**emp) for emp in employees)
    