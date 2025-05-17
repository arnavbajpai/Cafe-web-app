from fastapi import HTTPException

from Utils.Messages import CAFE_NOT_FOUND, EMPLOYEE_NOT_FOUND, SERVER_ERROR

def server_error_exception(e: Exception):

    raise HTTPException(
        status_code=500,
        detail=SERVER_ERROR.format(str(e))
    )
 

def cafe_not_found_exception(cafe_id: str):

    raise HTTPException(
        status_code=404,
        detail=CAFE_NOT_FOUND.format(cafe_id)
    )

def employee_not_found_exception(employee_id: str):
    raise HTTPException(
        status_code=404,
        detail=EMPLOYEE_NOT_FOUND.format(employee_id)
    )