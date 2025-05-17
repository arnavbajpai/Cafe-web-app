from Database.Database import get_session
from Models.DatabaseModels import CafeDB

from Utils.Messages import CAFE_DELETED
from Utils.Exceptions import server_error_exception, cafe_not_found_exception

def delete_cafe(cafe_id: str):
    with get_session() as session:
        cafe = session.get(CafeDB, cafe_id)
        if not cafe:
            cafe_not_found_exception(cafe_id)
        name = cafe.cafeName
        try:
            session.delete(cafe)
            session.commit()
            return {"message": CAFE_DELETED.format(cafe_name = name, cafe_id = cafe_id)}
        except Exception as e:
            session.rollback()
            server_error_exception(e)
