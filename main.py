from typing import Annotated, Optional
from uuid import UUID

from fastapi import FastAPI, Body, Path, Form, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from Models.Schemas import Cafe, Employee, UpdateCafe, UpdateEmployee
from Database.Database import init_db
from Query.FindCafe import find_cafe_by_location
from Query.FindEmployee import find_employee_by_cafe
from Query.FetchCafeLogo import fetch_cafe_logo
from Commands.AddCafe import add_cafe
from Commands.AddEmployee import add_employee
from Commands.UpdateCafeCommand import update_cafe
from Commands.UpdateEmployeeCommand import update_employee
from Commands.DeleteCafe import delete_cafe
from Commands.DeleteEmployee import delete_employee



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
MAX_SIZE = 1024 * 1024 * 2
@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/cafes/", status_code=200)
async def get_cafes(location: str | None = None) -> list[Cafe]:
    return find_cafe_by_location(location)


@app.get("/employees/", status_code=200)
async def get_employees(cafe: str | None = None) -> list[Employee]:
    return find_employee_by_cafe(cafe)


@app.post("/cafes/", status_code=201)
async def create_cafe(cafe: Annotated[Cafe, Body()],
                      logo: Annotated[UploadFile | None, Form()] = None):
    return add_cafe(cafe, logo)


@app.post("/employees/", status_code=201)
async def create_employee(employee: Annotated[Employee, Body()]):
    return add_employee(employee)


@app.put("/cafes/{cafe_id}", status_code=200)
async def modify_cafe(cafe_id: UUID, 
                      description: Annotated[str | None, Form()] = None,
                      location: Annotated[str | None, Form()] = None,
                      cafeName: Annotated[str | None, Form()] = None, 
                      logo: bytes | None = None): #Actually unable to accept form data
    cafe = UpdateCafe(description=description, location = location, cafeName = cafeName)
    update_cafe(cafe_id, cafe, logo)



@app.put("/employees/{employee_id}", status_code=200)
async def modify_employee(employee_id: Annotated[str, Path(pattern=r'^UI\d{7}$')],
                          employee: Annotated[UpdateEmployee, Body()]):
    return update_employee(employee_id, employee)


@app.delete("/cafes/{cafe_id}", status_code=200)
async def remove_cafe(cafe_id: UUID):
    delete_cafe(cafe_id)


@app.delete("/employees/{employee_id}", status_code=200)
async def remove_employee(employee_id: Annotated[str, Path(pattern=r'^UI\d{7}$')]):
    delete_employee(employee_id)

@app.get("/cafes/{cafe_id}/logo")
def get_cafe_logo(cafe_id: UUID):
    fetch_cafe_logo(cafe_id) 