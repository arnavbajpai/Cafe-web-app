from typing import Annotated
from uuid import UUID
from Models.Schemas import Cafe, Employee, UpdateCafe, UpdateEmployee
from fastapi import FastAPI, Query, Body, Path
from Database.Database import init_db
from Query import FindCafe
from Query import FindEmployee
from Commands import AddCafe
from Commands import AddEmployee
from Commands import UpdateCafeCommand
from Commands import UpdateEmployeeCommand
from Commands import DeleteCafe
from Commands import DeleteEmployee
app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/cafes/", status_code=200)
async def get_cafes(location: str | None = None)-> list[Cafe]:
    return FindCafe.find_cafe_by_location(location)


@app.get("/employees/", status_code=200)
async def get_employees(cafe: str | None = None)-> list[Employee]:
    return FindEmployee.find_employee_by_cafe(cafe)


@app.post("/cafes/", status_code=201)
async def add_cafe(cafe: Annotated[Cafe, Body()]):
    return AddCafe.add_cafe(cafe)


@app.post("/employees/", status_code=201)
async def add_employee(employee: Annotated[Employee, Body()]):
    return AddEmployee.add_employee(employee)


@app.put("/cafes/{cafe_id}", status_code=200)
async def update_cafe(cafe_id: int, update_cafe: Annotated[UpdateCafe, Body()]):
    return UpdateCafeCommand.update_cafe(cafe_id, update_cafe)


@app.put("/employees/{employee_id}", status_code=200)
async def update_employee(employee_id: int, update_employee: Annotated[UpdateEmployee, Body()]):
    return UpdateEmployeeCommand.update_employee(employee_id, update_employee)


@app.delete("/cafes/{cafe_id}", status_code=200)
async def delete_cafe(cafe_id: UUID):
    DeleteCafe.delete_cafe(cafe_id)


@app.delete("/employees/{employee_id}", status_code=200)
async def delete_employee(employee_id: Annotated[str, Path(pattern=r'^UI\d{7}$')]):
    DeleteEmployee.delete_employee(employee_id)