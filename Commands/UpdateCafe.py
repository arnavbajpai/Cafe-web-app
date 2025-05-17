from fastapi import HTTPException
from Database import get_session
from Models import CafeDB, UpdateCafe

def update_cafe(cafe_id: str, update_data: UpdateCafe):
    with get_session() as session:
        cafe = session.get(CafeDB, cafe_id)
        if not cafe:
            raise HTTPException(status_code=404, detail=f"Cafe {cafe_id} not found")
        update_fields = update_data.dict(exclude_unset=True)
        for key, value in update_fields.items():
            setattr(cafe, key, value)
        session.add(cafe)
        session.commit()
        session.refresh(cafe)
        return {"message": f"Cafe {cafe_id} updated successfully", "cafe": cafe}
