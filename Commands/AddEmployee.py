from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from Database.Database import get_session
from Models.Schemas import Employee
from Models.DatabaseModels import EmployeeDB

from Utils.Messages import EMPLOYEE_ADDED, EMPLOYEE_EXISTS
from Utils.Exceptions import server_error_exception

from Commands.UpdateEmployeeCommand import update_relationship

def add_employee(employee: Employee):
    employee_db = EmployeeDB(**employee.dict())
    name = employee.empName
    id = employee.empId
    cafe = employee.cafe
    with get_session() as session:
        try:
            session.add(employee_db)
            session.commit()
            session.refresh(employee_db)
            update_relationship(session, cafe, id)
            return {
                "message": EMPLOYEE_ADDED.format(emp_name = name, emp_id = id), 
                "employee": employee
            }
        except IntegrityError as e:
            session.rollback()
            raise HTTPException(
                status_code=409,
                detail=EMPLOYEE_EXISTS)
        except Exception as e:
            session.rollback()
            server_error_exception(e)
