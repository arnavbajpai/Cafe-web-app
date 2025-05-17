from datetime import date as dt_date

from sqlmodel import select

from Database.Database import get_session
from Models.DatabaseModels import EmployeeDB, EmployeeCafeDB, CafeDB
from Models.Schemas import Employee

def get_employee_cafe(session, emp_id) -> str | None:
    cafe = session.exec(
        select(CafeDB)
        .join(EmployeeCafeDB, EmployeeCafeDB.cafeId == CafeDB.cafeId)
        .where(EmployeeCafeDB.empId == emp_id)
    ).first()
    return cafe.cafeName if cafe else None


def get_employee_cafe_start_date(session, emp_id) -> dt_date | None:

    emp_cafe = session.exec(
        select(EmployeeCafeDB).where(EmployeeCafeDB.empId == emp_id)
    ).first()
    return emp_cafe.startDate if emp_cafe else None


def get_days_passed(start_date) -> int | None:
    if not start_date:
        return None
    currentdate = dt_date.today()
    return (currentdate - start_date).days


def find_employee_by_cafe(cafe_name: str | None) -> list[EmployeeDB]:
    with get_session() as session:
        if cafe_name:
            stmt = (
                select(EmployeeDB)
                .join(EmployeeCafeDB, EmployeeCafeDB.empId == EmployeeDB.empId)
                .join(CafeDB, CafeDB.cafeId == EmployeeCafeDB.cafeId)
                .where(CafeDB.cafeName == cafe_name)
            )
        else:
            stmt = select(EmployeeDB)
        rows = session.exec(stmt).all()
        employees = []
        for emp in rows:
            id = emp.empId
            name = get_employee_cafe(session, id)
            date = get_employee_cafe_start_date(session, id)
            days_passed = get_days_passed(date)
            emp_data = Employee(**emp.dict(), cafe=name, days=days_passed)
            employees.append(emp_data)
        employees.sort(
            key=lambda x: x.days if x.days is not None else -1, reverse=True)
        return employees
