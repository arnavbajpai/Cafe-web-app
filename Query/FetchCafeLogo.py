
from fastapi import HTTPException
from Database.Database import get_session
from Models.DatabaseModels import CafeDB
from fastapi.responses import Response
from uuid import UUID

def fetch_cafe_logo(cafe_id: UUID):
    with get_session() as session:
        cafe = session.get(CafeDB, cafe_id)
        if not cafe:
            raise HTTPException(status_code=404, detail="Logo not found")
        return Response(content=cafe.logo, media_type="image/jpeg")