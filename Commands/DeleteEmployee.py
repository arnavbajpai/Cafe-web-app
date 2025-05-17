from fastapi import HTTPException
from Database.Database import get_session
from Models.DatabaseModels import EmployeeDB

def delete_employee(employee_id: str):
    with get_session() as session:
        employee = session.get(EmployeeDB, employee_id)
        if not employee:
            raise HTTPException(status_code=404, detail=f"Employee {employee_id} not found")
        try: 
            session.delete(employee)
            session.commit()
            return {"message": f"Employee {employee_id} deleted successfully"}
        except Exception as e:  
            session.rollback()
            raise HTTPException(
                status_code=500,
                detail=f"Server error: {str(e)}"
            )
