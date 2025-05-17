import os

from sqlmodel import create_engine, SQLModel, Session

MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
DATABASE_URL = f"mysql+pymysql://root:{MYSQL_PASSWORD}@localhost:3306/cafe_hub"
engine = create_engine(DATABASE_URL, echo=True)


def get_session():
    return Session(engine)


def init_db():
    from Models.DatabaseModels import CafeDB, EmployeeDB, EmployeeCafeDB
    SQLModel.metadata.create_all(engine)
