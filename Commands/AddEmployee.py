from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from Database.Database import get_session
from Models.Schemas import Employee
from Models.DatabaseModels import EmployeeDB

def add_employee(employee: Employee):
    employee_db = EmployeeDB(**employee.dict())
    with get_session() as session:
        try:
            session.add(employee_db)
            session.commit()
            session.refresh(employee_db)
            return {
                "message": f"Employee {employee_db.name} with UUID {employee_db.id} added successfully.",
                "employee": employee
            }
        except IntegrityError as e:
            session.rollback()
            raise HTTPException(
                status_code=409,
                detail="Employee with the same id or email already exists.")
        except Exception as e:
            session.rollback()
            raise HTTPException(
                status_code=500, 
                detail=f"Server error: {str(e)}")
        