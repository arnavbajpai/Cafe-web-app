from database import get_session
from models import CafeDB

def delete_cafe(cafe_id: str):
    with get_session() as session:
        cafe = session.get(CafeDB, cafe_id)
        if not cafe:
            return {"error": "Cafe not found"}

        session.delete(cafe)
        session.commit()
        return {"message": f"Cafe {cafe_id} deleted successfully"}