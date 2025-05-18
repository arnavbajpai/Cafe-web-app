
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from Database.Database import get_session
from Models.Schemas import Cafe
from Models.DatabaseModels import CafeDB

from Utils.Messages import CAFE_ADDED, CAFE_EXISTS
from Utils.Exceptions import server_error_exception


def add_cafe(cafe: Cafe):
    cafe_db = CafeDB(**cafe.dict())
    name = cafe.cafeName
    cafe_id = cafe.cafeId
    with get_session() as session:
        try:
            session.add(cafe_db)
            session.commit()
            session.refresh(cafe_db)
            return {
                "message": CAFE_ADDED.format(cafe_name = name, cafe_id = cafe_id),
                "cafe": cafe
            }
        except IntegrityError as e:
            session.rollback()
            raise HTTPException(
                status_code=409,
                detail=CAFE_EXISTS)
        except Exception as e:
            session.rollback()
            server_error_exception(e)
