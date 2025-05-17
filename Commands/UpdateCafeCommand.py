from Database.Database import get_session
from Models.DatabaseModels import CafeDB
from Models.Schemas import UpdateCafe

from Utils.Messages import CAFE_UPDATED
from Utils.Exceptions import server_error_exception, cafe_not_found_exception

def update_cafe(cafe_id: str, update_data: UpdateCafe):
    with get_session() as session:
        cafe = session.get(CafeDB, cafe_id)
        if not cafe:
            cafe_not_found_exception(cafe_id)
        update_fields = update_data.dict(exclude_unset=True)
        for key, value in update_fields.items():
            setattr(cafe, key, value)
        try: 
            session.add(cafe)
            session.commit()
            session.refresh(cafe)
            return {
                "message": CAFE_UPDATED.format(cafe_id = cafe_id),
                "cafe": cafe
            }
        except Exception as e:
            session.rollback()
            server_error_exception(e)
