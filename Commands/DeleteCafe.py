from fastapi import HTTPException
from Database.Database import get_session
from Models.DatabaseModels import CafeDB

def delete_cafe(cafe_id: str):
    with get_session() as session:
        cafe = session.get(CafeDB, cafe_id)
        if not cafe:
            raise HTTPException(status_code=404, detail=f"Cafe {cafe_id} not found.")
        name = cafe.name
        try:
            session.delete(cafe)
            session.commit()
            return {"message": f"Cafe {name} with UUID {cafe_id} deleted successfully."}
        except Exception as e:
            session.rollback()
            raise HTTPException(
                status_code=500,
                detail=f"Server error: {str(e)}"
            )