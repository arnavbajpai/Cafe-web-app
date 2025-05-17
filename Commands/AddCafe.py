from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from Database.Database import get_session
from Models.Schemas import Cafe
from Models.DatabaseModels import CafeDB

def add_cafe(cafe: Cafe):
    cafe_db = CafeDB(**cafe.dict())
    with get_session() as session:
        try: 
            session.add(cafe_db)
            session.commit()
            session.refresh(cafe_db)
            return {"message": f"Cafe {cafe_db.cafeName} with UUID {cafe_db.cafeId} added successfully.", "cafe": cafe_db}
        except IntegrityError as e:
            session.rollback()
            raise HTTPException(
                status_code=409,
                detail="Cafe with same name or UUID exists.")
        except Exception as e:
            session.rollback()
            raise HTTPException(
                status_code=500, 
                detail=f"Server error: {str(e)}")