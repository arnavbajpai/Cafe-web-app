from typing import Annotated
from uuid import UUID
from models import Cafe, Employee, UpdateCafe, UpdateEmployee
from fastapi import FastAPI, Query, Body, Path

from Query import FindCafe
from Query import FindEmployee
from Commands import AddCafe
from Commands import AddEmployee
from Commands import UpdateCafe
from Commands import UpdateEmployee
app = FastAPI()

@app.get("/cafes/")
async def get_cafes(location: str | None = None):
    return FindCafe.find_cafe_by_location(location)


@app.get("/employees/")
async def get_employees(cafe: str | None = None):
    return FindEmployee.find_employee_by_cafe(cafe)


@app.post("/cafes/")
async def add_cafe(cafe: Annotated[Cafe, Body()]):
    return AddCafe.add_cafe(cafe)


@app.post("/employees/")
async def add_employee(employee: Annotated[Employee, Body()]):
    return AddEmployee.add_employee(employee)


@app.put("/cafes/{cafe_id}")
async def add_cafe(cafe_id: int, update_cafe: Annotated[UpdateCafe, Body()]):
    return UpdateCafe.update_cafe(cafe_id, update_cafe)


@app.put("/employees/{employee_id}")
async def add_employee(employee_id: int, update_employee: Annotated[UpdateEmployee, Body()]):
    return UpdateEmployee.update_employee(employee_id, update_employee)


@app.delete("/cafes/{cafe_id}")
async def delete_cafe(cafe_id: UUID):
    return DeleteCafe.delete_cafe(cafe_id)


@app.delete("/employees/{employee_id}")
async def delete_employee(employee_id: Annotated[str, Path(pattern=r'^UI\d{7}$')]):
    return DeleteEmployee.delete_employee(employee_id)