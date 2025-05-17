from database import get_session
from models import Cafe, CafeDB

def add_cafe(cafe: Cafe):
    cafe_db = CafeDB(**cafe.dict())
    with get_session() as session:
        session.add(cafe_db)
        session.commit()
        session.refresh(cafe_db)
        return cafe_db