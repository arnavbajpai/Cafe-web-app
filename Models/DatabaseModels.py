from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4
from typing import Optional
from datetime import date
from Models.Schemas import Gender
class CafeDB(SQLModel, table=True):
    __tablename__ = "cafe"
    cafeId: UUID = Field(default_factory=uuid4, primary_key=True)
    cafeName: str
    description: str
    logo: Optional[str] = None
    location: str

class EmployeeDB(SQLModel, table=True):
    __tablename__ = "employee"
    empId: str = Field(primary_key=True)
    empName: str
    email: str
    phoneNumber: str
    gender: Gender

class EmployeeCafeDB(SQLModel, table=True):
    __tablename__ = "employee_cafe"
    empId: str = Field(primary_key=True, foreign_key="employee.empId")
    cafeId: UUID = Field(foreign_key="cafe.cafeId")
    startDate: date