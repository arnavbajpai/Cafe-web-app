
from sqlmodel import select

from Database.Database import get_session
from Models.DatabaseModels import CafeDB, EmployeeCafeDB
from Models.Schemas import Cafe


def get_employee_count(session, cafe_id):
    return len(
        session.exec(
            select(EmployeeCafeDB).where(EmployeeCafeDB.cafeId == cafe_id)
        ).all()
    )


def build_cafe_data(cafe, employee_count)-> Cafe:
    cafe = Cafe(**cafe.dict(), employees=employee_count)
    return cafe



def find_cafe_by_location(location: str | None) -> list[Cafe]:
    with get_session() as session:
        if location:
            statement = select(CafeDB).where(CafeDB.location == location)
        else:
            statement = select(CafeDB)
        rows = session.exec(statement).all()
        cafes = []
        for cafe in rows:
            cafe_id = cafe.cafeId
            count = get_employee_count(session, cafe_id)
            cafe_data = build_cafe_data(cafe, count)
            cafes.append(cafe_data)
        cafes.sort(key=lambda x: x.employees, reverse=True)
        return cafes
