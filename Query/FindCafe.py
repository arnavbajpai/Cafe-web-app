from Database import get_session
from Models import CafeDB
from sqlmodel import select

def find_cafe_by_location(location: str | None):
    with get_session() as session:
        if location:
            statement = select(CafeDB).where(CafeDB.location == location)
        else:
            statement = select(CafeDB)
        return session.exec(statement).all()
    
