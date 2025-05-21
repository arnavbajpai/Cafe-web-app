from Database.Database import get_session
from Models.DatabaseModels import CafeDB, EmployeeCafeDB
from Commands.DeleteEmployee import delete_employee

from Utils.Messages import CAFE_DELETED
from Utils.Exceptions import server_error_exception, cafe_not_found_exception


def get_employee_ids_by_cafe(session, cafe_id):
    emp_cafe_records = session.query(EmployeeCafeDB).filter(EmployeeCafeDB.cafeId == cafe_id).all()
    return [record.empId for record in emp_cafe_records]


def delete_employees_by_ids(session, emp_ids):
    for emp_id in emp_ids:
        delete_employee(emp_id)


def delete_cafe(cafe_id: str):
    with get_session() as session:
        cafe = session.get(CafeDB, cafe_id)
        if not cafe:
            cafe_not_found_exception(cafe_id)
        name = cafe.cafeName
        try:
            emp_ids = get_employee_ids_by_cafe(session, cafe_id)
            delete_employees_by_ids(session, emp_ids)
            session.delete(cafe)
            session.commit()
            return {"message": CAFE_DELETED.format(cafe_name=name, cafe_id=cafe_id)}
        except Exception as e:
            session.rollback()
            server_error_exception(e)
