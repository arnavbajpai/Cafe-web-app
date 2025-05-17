from sqlmodel import create_engine, SQLModel, Session

DATABASE_URL = "mysql+pymysql://username:password@localhost:3306/mydatabase"
engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    return Session(engine)

def init_db():
    from models import CafeDB, EmployeeDB
    SQLModel.metadata.create_all(engine)