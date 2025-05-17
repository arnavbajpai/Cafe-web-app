from Database.Database import get_session
from Models.DatabaseModels import EmployeeDB

from Utils.Messages import EMPLOYEE_DELETED
from Utils.Exceptions import server_error_exception, employee_not_found_exception


def delete_employee(employee_id: str):
    with get_session() as session:
        employee = session.get(EmployeeDB, employee_id)
        if not employee:
            employee_not_found_exception(employee_id)
        name = employee.empName
        try:
            session.delete(employee)
            session.commit()
            return {"message": EMPLOYEE_DELETED.format(name, employee_id)}
        except Exception as e:
            session.rollback()
            server_error_exception(e)
