from enum import Enum
from uuid import UUID
from pydantic import BaseModel, Field, EmailStr
from fastapi import File


class Gender(Enum):
    Male = 'Male'
    Female = 'Female'


class Employee(BaseModel):
    empId: str = Field(pattern=r'^UI\d{7}$')
    empName: str
    email: EmailStr
    phoneNumber: str = Field(pattern=r'^[89]\d{7}$')
    gender: Gender
    cafe: str | None
    days: int | None


class Cafe(BaseModel):
    cafeId: UUID
    cafeName: str
    description: str
    location: str
    employees: int | None
    logoUrl: str | None = None


class UpdateCafe(BaseModel):
    cafeName: str | None = Field(min_length=6, max_length=10)
    description: str | None = Field(max_length=255)
    location: str | None


class UpdateEmployee(BaseModel):
    empName: str | None = Field(min_length=6, max_length=10)
    email: EmailStr | None
    phoneNumber: str | None = Field(length=8, pattern=r'^[89]\d{7}$')
    gender: Gender | None
    cafe: str | None
