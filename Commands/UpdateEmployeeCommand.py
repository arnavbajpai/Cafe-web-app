from datetime import date
from uuid import UUID

from sqlmodel import select

from Database.Database import get_session
from Models.DatabaseModels import EmployeeDB, CafeDB, EmployeeCafeDB
from Models.Schemas import UpdateEmployee

from Utils.Messages import EMPLOYEE_UPDATED
from Utils.Exceptions import server_error_exception, employee_not_found_exception, cafe_not_found_exception


def update_employee(employee_id: str, update_data: UpdateEmployee):
    with get_session() as session:
        employee = session.get(EmployeeDB, employee_id)
        if not employee:
            employee_not_found_exception(employee_id)
        update_fields = update_data.dict(exclude_unset=True)
        for key, value in update_fields.items():
            if hasattr(employee, key):
                setattr(employee, key, value)
        cafe_name = update_fields.get('cafe')
        if cafe_name:
            update_relationship(session, cafe_name, employee_id)
        try:
            session.add(employee)
            session.commit()
            session.refresh(employee)
            return {
                "message": EMPLOYEE_UPDATED.format(employee_id),
                "employee": employee
            }
        except Exception as e:
            session.rollback()
            server_error_exception(e)


def get_cafe_by_name(session, cafe_name: str):
    cafe = session.exec(select(CafeDB).where(
        CafeDB.cafeName == cafe_name)).first()
    if not cafe:
        cafe_not_found_exception(cafe_name)


def get_employee_cafe_record(session, emp_id: str):
    return session.exec(select(EmployeeCafeDB).where(EmployeeCafeDB.empId == emp_id)).first()


def update_employee_cafe(session, emp_id: str, cafe_id: UUID):
    emp_cafe = get_employee_cafe_record(session, emp_id)
    if emp_cafe:
        emp_cafe.cafeId = cafe_id
        session.add(emp_cafe)
        session.commit()
        session.refresh(emp_cafe)
        return emp_cafe
    return None


def create_employee_cafe(session, emp_id: str, cafe_id: UUID):
    new_emp_cafe = EmployeeCafeDB(
        empId=emp_id,
        cafeId=cafe_id,
        startDate=date.today()
    )
    session.add(new_emp_cafe)
    session.commit()
    session.refresh(new_emp_cafe)
    return new_emp_cafe


def update_relationship(session, cafe_name: str, emp_id: str):
    cafe = get_cafe_by_name(session, cafe_name)
    cafe_id = cafe.cafeId
    emp_cafe = get_employee_cafe_record(session, emp_id)
    if emp_cafe:
        update_employee_cafe(session, emp_id, cafe_id)
    else:
        create_employee_cafe(session, emp_id, cafe_id)
