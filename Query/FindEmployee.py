from database import get_session
from models import EmployeeDB, EmployeeCafeDB, CafeDB
from sqlmodel import select

def find_employee_by_cafe(cafe_name: str | None):
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
        return session.exec(stmt).all()
