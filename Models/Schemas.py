from pydantic import BaseModel, Field, EmailStr
from enum import Enum 
from uuid import UUID
class Gender(str, Enum):
    male = 'Male'
    female = 'Female'

class Employee(BaseModel):
    empId: str = Field(pattern=r'^UI\d{7}$')
    empName: str
    email: EmailStr
    phone: str = Field(pattern=r'^[89]\d{7}$')
    gender: Gender
    cafe: str | None

class Cafe(BaseModel):
    cafeId: UUID
    cafeName: str
    description: str
    location: str
    logo: str | None
    employees: int | None

class UpdateCafe(BaseModel):
    name: str | None = Field(min_length=6, max_length=10)
    description: str | None = Field(max_length=255)
    location: str | None
    logo: str | None = Field(max_size=2*1024*1024)

class UpdateEmployee(BaseModel):
    name: str | None = Field(min_length=6, max_length=10)
    email: EmailStr | None 
    phone: str | None = Field(length=8, pattern=r'^[89]\d{7}$')
    gender: Gender | None
    cafe: str | None