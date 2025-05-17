from fastapi import HTTPException
from Database import get_session
from Models import EmployeeDB, UpdateEmployee

def update_employee(employee_id: str, update_data: UpdateEmployee):
    with get_session() as session:
        employee = session.get(EmployeeDB, employee_id)
        if not employee:
            raise HTTPException(status_code=404, detail=f"Employee {employee_id} not found")
        update_fields = update_data.dict(exclude_unset=True)
        for key, value in update_fields.items():
            setattr(employee, key, value)

        session.add(employee)
        session.commit()
        session.refresh(employee)
        return {"message": f"Employee {employee_id} updated successfully", "employee": employee}